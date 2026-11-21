"""Offline checks. These do not measure the quality of a real model's answers."""
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import agent


class AgentChecks(unittest.TestCase):
    def setUp(self):
        self.rows = agent.read_rows(agent.ROOT / "data" / "retention.csv")

    def test_known_descriptive_answer(self):
        groups = agent.summarize(self.rows, "overall")["groups"]
        self.assertEqual([(g["n_rows"], g["retained"], g["retention_pct"]) for g in groups],
                         [(200, 64, 32.0), (200, 136, 68.0)])
        stratified = agent.summarize(self.rows, "frequency_pre")["groups"]
        self.assertEqual([(g["n_rows"], g["retained"], g["retention_pct"]) for g in stratified],
                         [(40, 32, 80.0), (160, 128, 80.0), (160, 32, 20.0), (40, 8, 20.0)])

    def test_quality_rejects_duplicates_and_missing_values(self):
        self.assertTrue(agent.inspect_rows(self.rows)["passed"])
        self.assertFalse(agent.inspect_rows(self.rows + [self.rows[0]])["passed"])
        row = dict(self.rows[0], retained_30d="")
        self.assertFalse(agent.inspect_rows([row])["passed"])

    def test_dispatch_rejects_unknown_tool_and_invalid_arguments(self):
        for call in [{"function": {"name": "exec", "arguments": {"code": "print(1)"}}},
                     {"function": {"name": "summarize_retention", "arguments": {"breakdown": "city"}}},
                     {"function": {"name": "inspect_data", "arguments": {"path": "/tmp"}}},
                     {"function": {"name": "inspect_data", "arguments": "not json"}}]:
            self.assertIn("error", agent.dispatch(call, self.rows))

    def test_two_tool_results_reach_the_model(self):
        seen = []
        def request(endpoint, payload):
            seen.append(json.loads(json.dumps(payload)))
            if len(seen) == 1:
                return {"message": {"role": "assistant", "content": "", "tool_calls": [
                    {"function": {"name": "inspect_data", "arguments": {}}},
                    {"function": {"name": "summarize_retention", "arguments": {"breakdown": "overall"}}}]}}
            self.assertEqual([m["tool_name"] for m in payload["messages"] if m["role"] == "tool"],
                             ["inspect_data", "summarize_retention"])
            return {"message": {"role": "assistant", "content": "Respuesta de prueba; no generada por un modelo."}}
        trace = {"events": []}
        result = agent.run_loop([{"role": "user", "content": "test"}], self.rows, agent.MODEL, trace, request, False)
        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["tool_calls"], 2)
        self.assertEqual(len(seen[0]["messages"]), 1)
        self.assertEqual(len(trace["events"][0]["payload"]["messages"]), 1)

    def test_loop_limit_and_truncated_output(self):
        def endless(endpoint, payload):
            return {"message": {"role": "assistant", "content": "", "tool_calls": [
                {"function": {"name": "inspect_data", "arguments": {}}}]}}
        result = agent.run_loop([], self.rows, agent.MODEL, {"events": []}, endless, False, 2)
        self.assertEqual(result["status"], "budget_exceeded")
        def truncated(endpoint, payload):
            return {"done_reason": "length", "message": {"role": "assistant", "content": "partial"}}
        result = agent.run_loop([], self.rows, agent.MODEL, {"events": []}, truncated, False)
        self.assertEqual(result["status"], "truncated")

    def test_checked_mode_blocks_before_model_call_and_saves_trace(self):
        with tempfile.TemporaryDirectory() as folder, patch("agent.local_model_info") as mock:
            result = agent.run(mode="checked", data=agent.ROOT / "data" / "retention_duplicates.csv",
                               verbose=False, output_dir=folder)
            mock.assert_not_called()
            self.assertEqual(result["status"], "blocked")
            trace = json.loads(Path(result["trace_file"]).read_text(encoding="utf-8"))
            self.assertEqual(trace["data_quality"]["duplicate_user_rows"], 1)
            self.assertEqual(trace["events"], [])

    def test_cloud_models_not_accepted(self):
        with self.assertRaises(ValueError):
            agent.run(model="anything-cloud", verbose=False)

    def test_check_needs_the_model_and_one_reply(self):
        def server(endpoint, payload=None):
            if endpoint == "/tags":
                return {"models": [{"name": agent.MODEL, "size": 3.4e9, "digest": "abc123def4567890"}]}
            if endpoint == "/version":
                return {"version": "test"}
            self.assertEqual(payload["options"]["num_ctx"], agent.OPTIONS["num_ctx"])
            return {"message": {"role": "assistant", "content": "Montevideo"}}
        with patch("sys.stdout", new_callable=io.StringIO) as out:
            self.assertTrue(agent.check(agent.MODEL, server))
        self.assertIn("Todo listo", out.getvalue())
        with patch("sys.stdout", new_callable=io.StringIO) as out:
            self.assertFalse(agent.check("qwen3.5:2b", server))
        self.assertIn("ollama pull qwen3.5:2b", out.getvalue())

    def test_live_output_shows_each_request_and_table(self):
        replies = iter([
            {"message": {"role": "assistant", "content": "", "tool_calls": [
                {"function": {"name": "summarize_retention", "arguments": {"breakdown": "overall"}}}]}},
            {"message": {"role": "assistant", "content": "Respuesta de prueba; no generada por un modelo."}}])
        with patch("sys.stdout", new_callable=io.StringIO) as out:
            agent.run_loop([{"role": "user", "content": "test"}], self.rows, agent.MODEL, {"events": []},
                           lambda endpoint, payload: next(replies), True)
        shown = out.getvalue()
        self.assertIn('El modelo pide: summarize_retention(breakdown="overall")', shown)
        self.assertIn("68.0%", shown)
        self.assertIn("32.0%", shown)


if __name__ == "__main__":
    unittest.main()
