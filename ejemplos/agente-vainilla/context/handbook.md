# Manual metodológico mínimo

## Contrato de datos

El archivo es sintético: un ejercicio, sin datos de ninguna empresa ni de personas reales.
Unidad de análisis: un usuario elegible en una única fecha índice t0.
Debe haber exactamente una fila por user_id. Todos los usuarios tienen seguimiento
completo durante los 30 días posteriores; no hay censura en este ejercicio.

| Campo | Definición | Momento |
|---|---|---|
| user_id | Identificador único del usuario | t0 |
| city | Ciudad del usuario: Montevideo, Canelones, Maldonado, Salto o Rivera | t0 |
| platform | Plataforma desde la que pide: android, ios o web | t0 |
| frequency_pre | high = al menos 5 pedidos; low = menos de 5, en los 30 días anteriores | Antes de t0 |
| promo_received | 1 = recibió una promoción en t0; 0 = no recibió | t0 |
| retained_30d | 1 = al menos un pedido entre t0+1 y t0+30 días; 0 = ninguno | Después de t0 |

## Protocolo

1. Inspecciona los datos. Detente si hay duplicados, faltantes o valores inválidos;
   no dedupliques ni imputes sin una regla justificada.
2. Calcula retención por grupo de promoción. Expón denominador, retenidos y tasa.
3. Compara también dentro de frequency_pre. Revisa la composición de los grupos.
4. Distingue diferencia de tasas en puntos porcentuales de cambio porcentual relativo.
5. La promoción no fue asignada aleatoriamente. Estos conteos describen asociaciones.
   Una diferencia agregada no identifica el efecto de la promoción.
6. Lo que muestre la comparación dentro de frequency_pre tampoco identifica el efecto causal,
   sea cual sea. Ajustar una sola variable no garantiza intercambiabilidad ni ausencia de sesgo.
7. No uses retained_30d como predictor de una decisión tomada en t0. En futuras
   extensiones predictivas, define el momento de disponibilidad de cada variable y
   separa entrenamiento y evaluación antes de seleccionar modelos.
8. No inventes intervalos, valores p, bibliografía o resultados de métodos no ejecutados.
9. Que una diferencia aparezca en todas las ciudades o plataformas no la vuelve causal ni
   robusta: si los grupos difieren en composición dentro de cada segmento, la diferencia se repite.
10. Desconfía de los segmentos chicos: una tasa sobre 20 usuarios puede ser ruido. Informa
    siempre el denominador antes de destacar un segmento.

## Entrega

Presenta: evidencia numérica; comparación por frecuencia; conclusión que permiten
los datos; limitación causal; siguiente evidencia necesaria. Una recomendación de
experimento debe especificar población, asignación, resultado y horizonte. Abstenerse
de una conclusión causal no impide informar resultados descriptivos útiles.

Este manual es contexto explícito agregado al prompt. No modifica los pesos del modelo
y no demuestra por sí solo que el agente obedezca o que el análisis sea válido.
