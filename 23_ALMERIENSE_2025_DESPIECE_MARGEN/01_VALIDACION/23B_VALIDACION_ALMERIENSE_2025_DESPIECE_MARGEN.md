# 23B - Validación técnica ALMERIENSE 2025: despiece del agujero de margen

## 1. Objetivo

Este módulo analiza exclusivamente **ALMERIENSE 2025** para separar el margen estimado entre negocio operativo, capas no core y ruido técnico de datos.

Fuente principal:
- `23A1_lineas_base_almeriense_2025.csv`

La extracción trabaja con líneas de factura de venta 2025, excluyendo facturas/líneas anuladas según los campos disponibles.

---

## 2. Lectura general

| Métrica | Valor |
|---|---:|
| Líneas analizadas | 475 |
| Clientes | 24 |
| Referencias | 155 |
| Ventas sin IVA | 146.266,63 € |
| Coste estimado | 217.750,59 € |
| Margen estimado | -71.483,96 € |
| Margen estimado % | -48,87% |

La lectura bruta reproduce el problema detectado en el cierre anual 2025: **margen negativo estimado en ALMERIENSE**.

---

## 3. Metodología de capas

Se ha usado una clasificación prioritaria por línea. Si una línea encaja en varias categorías, se asigna a la primera categoría aplicable:

1. `INTRAGRUPO`
2. `PATRIMONIAL_NO_CORE`
3. `REFERENCIA_GENERICA`
4. `COSTE_CERO`
5. `COSTE_STOCK_SOSPECHOSO`
6. `MARGEN_NEGATIVO`
7. `RESTO_LIMPIO_APROX`

Esto evita doble conteo en el despiece principal. Además se entrega un archivo de flags solapados porque algunas líneas tienen varios problemas a la vez.

Archivos clave:
- `23B2_despiece_prioritario_capas.csv`
- `23B3_flags_solapados_capas.csv`
- `23B3B_solape_referencia_coste_margen.csv`

---

## 4. Resultado por capas prioritarias

| CLASIFICACION_PRIORITARIA   |   LINEAS |   VENTAS_SIN_IVA |   COSTE_ESTIMADO |   MARGEN_ESTIMADO |   MARGEN_PCT_ESTIMADO |   PESO_SOBRE_VENTAS_TOTAL_PCT |
|:----------------------------|---------:|-----------------:|-----------------:|------------------:|----------------------:|------------------------------:|
| REFERENCIA_GENERICA         |      122 |         15194.9  |        163112    |        -147917    |               -973.46 |                         10.39 |
| COSTE_STOCK_SOSPECHOSO      |        4 |           736.05 |          7808.32 |          -7072.27 |               -960.84 |                          0.5  |
| MARGEN_NEGATIVO             |        4 |           627.9  |           909.01 |           -281.11 |                -44.77 |                          0.43 |
| COSTE_CERO                  |        8 |          2015.4  |             0    |           2015.4  |                100    |                          1.38 |
| INTRAGRUPO                  |       17 |          8565.8  |          1431.5  |           7134.3  |                 83.29 |                          5.86 |
| PATRIMONIAL_NO_CORE         |       26 |         24219.4  |             0    |          24219.4  |                100    |                         16.56 |
| RESTO_LIMPIO_APROX          |      294 |         94907.2  |         44490.1  |          50417.1  |                 53.12 |                         64.89 |

---

## 5. Hallazgo principal

El agujero no parece venir del negocio operativo limpio.

La capa `RESTO_LIMPIO_APROX` queda así:

| Métrica | Valor |
|---|---:|
| Líneas | 294 |
| Ventas sin IVA | 94.907,18 € |
| Coste estimado | 44.490,12 € |
| Margen estimado | 50.417,06 € |
| Margen estimado % | 53,12% |

Por tanto, al apartar capas priorizadas como intragrupo, patrimonial/no core, referencia genérica, coste cero, coste/stock sospechoso y margen negativo residual, el resto aproximado queda con margen positivo.

---

## 6. Contaminación más relevante

La mayor distorsión está en referencias genéricas y costes sospechosos.

Resumen de flags, permitiendo solapes:

| FLAG                     |   LINEAS |   CLIENTES |   REFERENCIAS |   VENTAS_SIN_IVA |   COSTE_ESTIMADO |   MARGEN_ESTIMADO |   MARGEN_PCT_ESTIMADO |   PESO_SOBRE_VENTAS_TOTAL_PCT |
|:-------------------------|---------:|-----------:|--------------:|-----------------:|-----------------:|------------------:|----------------------:|------------------------------:|
| FLAG_INTRAGRUPO          |       17 |          4 |             6 |          8565.8  |           1431.5 |            7134.3 |                 83.29 |                          5.86 |
| FLAG_PATRIMONIAL_NO_CORE |       34 |          4 |             1 |         31419.4  |              0   |           31419.4 |                100    |                         21.48 |
| FLAG_REFERENCIA_GENERICA |      156 |         12 |             3 |         46614.3  |         163112   |         -116497   |               -249.92 |                         31.87 |
| FLAG_COSTE_CERO          |       69 |          9 |             5 |         33434.8  |              0   |           33434.8 |                100    |                         22.86 |
| FLAG_MARGEN_NEGATIVO     |       59 |          7 |             9 |          5298.1  |         168091   |         -162793   |              -3072.67 |                          3.62 |
| FLAG_COSTE_SOSPECHOSO    |       45 |          6 |             7 |          3470.35 |         164562   |         -161091   |              -4641.94 |                          2.37 |

Especialmente relevante:
- `FLAG_MARGEN_NEGATIVO`: 59 líneas, margen -162.793,02 €.
- `FLAG_COSTE_SOSPECHOSO`: 45 líneas, margen -161.091,44 €.
- `FLAG_REFERENCIA_GENERICA`: 156 líneas, margen -116.497,34 €.

El solape indica que muchas líneas negativas tienen simultáneamente referencia genérica y coste sospechoso.

---

## 7. Patrimonial / no core

La capa patrimonial/no core suma aproximadamente:
- Ventas: 31.419,40 €
- Margen: 31.419,40 €

Está dominada por alquiler vacacional Casa Macenas y alquiler de nave a Grupo Chemie.

Esta capa no debe mezclarse con margen operativo comercial.

---

## 8. Intragrupo

La capa intragrupo suma aproximadamente:
- Ventas: 8.565,80 €
- Margen: 7.134,30 €

Incluye alquiler de nave y algunas ventas puntuales a sociedades/personas vinculadas. Parte de esta capa también puede ser patrimonial, pero en la clasificación prioritaria el intragrupo va primero.

---

## 9. Estimación de resto limpio

| ESCENARIO                      |   LINEAS |   VENTAS_SIN_IVA |   COSTE_ESTIMADO |   MARGEN_ESTIMADO |   MARGEN_PCT_ESTIMADO |
|:-------------------------------|---------:|-----------------:|-----------------:|------------------:|----------------------:|
| TOTAL_ALMERIENSE_2025          |      475 |        146267    |        217751    |         -71484    |                -48.87 |
| MENOS_INTRAGRUPO               |      -17 |         -8565.8  |         -1431.5  |          -7134.3  |                 83.29 |
| MENOS_PATRIMONIAL_NO_CORE      |      -26 |        -24219.4  |            -0    |         -24219.4  |                100    |
| MENOS_REFERENCIA_GENERICA      |     -122 |        -15194.9  |       -163112    |         147917    |               -973.46 |
| MENOS_COSTE_CERO               |       -8 |         -2015.4  |            -0    |          -2015.4  |                100    |
| MENOS_COSTE_STOCK_SOSPECHOSO   |       -4 |          -736.05 |         -7808.32 |           7072.27 |               -960.84 |
| MENOS_MARGEN_NEGATIVO          |       -4 |          -627.9  |          -909.01 |            281.11 |                -44.77 |
| RESTO_LIMPIO_APROX_PRIORITARIO |      294 |         94907.2  |         44490.1  |          50417.1  |                 53.12 |

Esta estimación no pretende ser contabilidad oficial. Es una aproximación de gestión para separar ruido del negocio más interpretable.

---

## 10. Conclusión técnica

La lectura más razonable es:

**Mezcla de ruido técnico + capas no core, con predominio del ruido técnico en el agujero de margen.**

No parece correcto concluir que ALMERIENSE 2025 haya tenido una pérdida operativa real de 71.483,96 € sin validar antes:

1. referencias genéricas, especialmente `999999`;
2. costes medios absurdos o importes de coste desproporcionados;
3. líneas con coste cero;
4. líneas patrimoniales/no core;
5. intragrupo y alquileres;
6. stock y maestro de artículos.

El negocio aparentemente limpio sale con margen positivo estimado. La prioridad no es interpretar directamente la pérdida, sino depurar maestro, costes y clasificación core/no core.

---

## 11. Límites del dato

- El coste es estimado usando `CANTIDAD * PRECIOMEDIOCOMPRA`.
- No equivale a margen contable definitivo.
- La clasificación es heurística y depende de textos, clientes y referencias.
- Una línea puede tener varios flags; el despiece principal usa prioridad para evitar doble conteo.
- Las referencias genéricas pueden agrupar productos distintos y contaminar coste/margen.
- El stock real físico no queda validado por este módulo.

---

## 12. Archivos generados

- `23B0_control_general_almeriense_2025.csv`
- `23B1_lineas_clasificadas_almeriense_2025.csv`
- `23B2_despiece_prioritario_capas.csv`
- `23B3_flags_solapados_capas.csv`
- `23B3B_solape_referencia_coste_margen.csv`
- `23B4_referencias_genericas_y_sospechosas.csv`
- `23B5A_margen_negativo_top_lineas.csv`
- `23B5B_margen_negativo_top_referencias.csv`
- `23B6_coste_cero_y_coste_anomalo.csv`
- `23B7_patrimonial_no_core.csv`
- `23B8_intragrupo.csv`
- `23B9_estimacion_resto_limpio.csv`
