# 21A - Validación cierre anual 2025 Grupo Familiar

## Estado del paquete

El paquete `21A_PAQUETE_CIERRE_ANUAL_2025_CSV.zip` se ha leído correctamente y se ha limpiado:

- se han eliminado cabeceras repetidas por empresa;
- se han eliminado líneas en blanco;
- se han normalizado decimales a 2 posiciones;
- se mantiene el separador `;` para uso directo en Excel/Power BI;
- se genera paquete limpio: `21A_PAQUETE_CIERRE_ANUAL_2025_CSV_LIMPIO.zip`.

## Archivos incluidos

1. `GRUPO_21A1_ventas_empresa_2025.csv`
2. `GRUPO_21A2_top_clientes_2025.csv`
3. `GRUPO_21A3_ventas_coste_margen_empresa_2025.csv`
4. `GRUPO_21A4_top_familias_2025.csv`
5. `GRUPO_21A5_compras_empresa_2025.csv`
6. `GRUPO_21A6_top_proveedores_2025.csv`
7. `GRUPO_21A7_clientes_pendientes_cierre_2025.csv`
8. `GRUPO_21A8_proveedores_pendientes_cierre_2025.csv`
9. `GRUPO_21A9_bancos_deuda_intereses_cierre_2025.csv`
10. `GRUPO_21A10_ventas_clasificacion_simple_2025.csv`

---

## 1. Ventas 2025 por empresa

| EMPRESA    |   FACTURAS |   CLIENTES_CON_VENTA | VENTAS_SIN_IVA   | TOTAL_CON_IVA   |
|:-----------|-----------:|---------------------:|:-----------------|:----------------|
| CHEMIE     |        532 |                   57 | 630.692,76 €     | 759.263,84 €    |
| ALMERIENSE |        136 |                   24 | 146.266,63 €     | 172.765,49 €    |
| ECOCLEAN   |        433 |                   87 | 89.077,75 €      | 107.784,20 €    |

**Ventas grupo 2025 sin IVA:** 866.037,14 €.

## 2. Compras 2025 por empresa

| EMPRESA    |   FACTURAS |   PROVEEDORES_CON_COMPRA | COMPRAS_SIN_IVA   | TOTAL_CON_IVA   |
|:-----------|-----------:|-------------------------:|:------------------|:----------------|
| CHEMIE     |        530 |                       77 | 433.441,08 €      | 518.235,00 €    |
| ALMERIENSE |        395 |                       81 | 83.534,85 €       | 100.931,08 €    |
| ECOCLEAN   |         81 |                       12 | 27.924,11 €       | 34.231,47 €     |

**Compras grupo 2025 sin IVA:** 544.900,04 €.

## 3. Ventas, coste estimado y margen bruto 2025

| EMPRESA    |   LINEAS | VENTAS_LINEAS_SIN_IVA   | COSTE_ESTIMADO   | MARGEN_BRUTO_ESTIMADO   | MARGEN_PCT_ESTIMADO   |
|:-----------|---------:|:------------------------|:-----------------|:------------------------|:----------------------|
| CHEMIE     |     3849 | 630.692,76 €            | 327.336,56 €     | 303.356,20 €            | 48,10%                |
| ALMERIENSE |      475 | 146.266,63 €            | 217.750,59 €     | -71.483,96 €            | -48,87%               |
| ECOCLEAN   |     1704 | 89.077,75 €             | 47.384,81 €      | 41.692,94 €             | 46,81%                |

### Lectura

- CHEMIE muestra margen estimado positivo y coherente.
- ECOCLEAN muestra margen estimado positivo y coherente.
- ALMERIENSE muestra margen estimado negativo. No debe interpretarse automáticamente como pérdida real: ya se había detectado contaminación por referencias genéricas, costes medios o líneas no operativas. Hay que validar el maestro/coste de ALMERIENSE antes de usar este margen como dato de gestión.

## 4. Clasificación simple de ventas 2025

| EMPRESA    | CLASIFICACION        |   LINEAS | VENTAS_SIN_IVA   | COSTE_ESTIMADO   | MARGEN_BRUTO_ESTIMADO   |
|:-----------|:---------------------|---------:|:-----------------|:-----------------|:------------------------|
| CHEMIE     | INTRAGRUPO_VINCULADA |        5 | 5.868,00 €       | 736,31 €         | 5.131,69 €              |
| CHEMIE     | MERCADO_OPERATIVO    |     3826 | 624.824,76 €     | 326.600,25 €     | 298.224,51 €            |
| CHEMIE     | PATRIMONIAL_NO_CORE  |       18 | 0,00 €           | 0,00 €           | 0,00 €                  |
| ALMERIENSE | INTRAGRUPO_VINCULADA |       17 | 8.565,80 €       | 1.431,50 €       | 7.134,30 €              |
| ALMERIENSE | MERCADO_OPERATIVO    |      432 | 113.481,43 €     | 216.319,09 €     | -102.837,66 €           |
| ALMERIENSE | PATRIMONIAL_NO_CORE  |       26 | 24.219,40 €      | 0,00 €           | 24.219,40 €             |
| ECOCLEAN   | MERCADO_OPERATIVO    |     1704 | 89.077,75 €      | 47.384,81 €      | 41.692,94 €             |

### Lectura

- La clasificación es una primera aproximación por texto/contraparte.
- En ALMERIENSE se detectan ventas patrimoniales/no core por 24.219,40 €.
- No debe usarse como clasificación definitiva fiscal/contable. Sirve para separar primera capa operativa / patrimonial / intragrupo.

## 5. Clientes pendientes estimados a 31/12/2025

Importe agregado dentro del top 30 por empresa:

| EMPRESA    | PENDIENTE_ESTIMADO_CIERRE   |
|:-----------|:----------------------------|
| ALMERIENSE | 186.009,80 €                |
| CHEMIE     | 255.497,29 €                |
| ECOCLEAN   | 25.520,91 €                 |

### Saldos antiguos destacados

| EMPRESA    | RAZON_SOCIAL                             | PENDIENTE_ESTIMADO_CIERRE   | VTO_MAS_ANTIGUO   |   DIAS_MAX_VENCIDO |
|:-----------|:-----------------------------------------|:----------------------------|:------------------|-------------------:|
| ALMERIENSE | FRIPACK LOPEZ BENAVIDES, S.L.            | 1.080,54 €                  | 0207-10-30        |             664074 |
| ALMERIENSE | FRIO MAGO, S.L.                          | 18,56 €                     | 2003-06-30        |               8220 |
| CHEMIE     | CANALEX, S.A.T.                          | 13.954,87 €                 | 2004-05-10        |               7905 |
| ALMERIENSE | S.A. DE VEHICULOS, REPUESTOS Y SERVICIOS | 59.073,36 €                 | 2006-08-11        |               7082 |
| CHEMIE     | JUAN JOSE MARTINEZ NAHARRO               | 60.000,00 €                 | 2007-04-02        |               6848 |

### Advertencia

Los clientes pendientes incluyen saldos muy antiguos. Deben tratarse como **cartera estimada a revisar**, no como saldo cobrable limpio. Hay importes con vencimientos de 2007/2019 que requieren validación documental.

## 6. Proveedores pendientes estimados a 31/12/2025

Importe agregado dentro del top 30 por empresa:

| EMPRESA    | PENDIENTE_ESTIMADO_CIERRE   |
|:-----------|:----------------------------|
| ALMERIENSE | 89.002,52 €                 |
| CHEMIE     | 138.597,72 €                |
| ECOCLEAN   | 3.346,86 €                  |

### Saldos antiguos destacados

| EMPRESA    | RAZON_SOCIAL                            | PENDIENTE_ESTIMADO_CIERRE   | VTO_MAS_ANTIGUO   |   DIAS_MAX_VENCIDO |
|:-----------|:----------------------------------------|:----------------------------|:------------------|-------------------:|
| ALMERIENSE | INDUSTRIAS TAYG, S.L.                   | 156,74 €                    | 2004-02-28        |               7977 |
| ALMERIENSE | OBRAS Y CONSTRUCCIONES BERJAMAR, S.L.   | 18.618,00 €                 | 2004-04-01        |               7944 |
| ALMERIENSE | MAGO SELECCION ALMERIA, S.L.            | 784,62 €                    | 2005-08-17        |               7441 |
| ALMERIENSE | FERBA AUTOMATISMOS, S.L.                | 7.650,34 €                  | 2005-11-15        |               7351 |
| ALMERIENSE | S.A.DE VEHICULOS, REPUESTOS Y SERVICIOS | 173,13 €                    | 2006-05-02        |               7183 |

### Advertencia

Los proveedores pendientes incluyen efectos antiguos y saldos históricos. Deben validarse contra gestión real, banco y asesoría antes de usarse como deuda real.

## 7. Bancos, deuda e intereses

Resumen por tipo de cuenta:

| EMPRESA    | TIPO_CUENTA   | SALDO_INTERPRETADO   |
|:-----------|:--------------|:---------------------|
| ALMERIENSE | BANCO_572     | 2.200,45 €           |
| ALMERIENSE | DEUDA_CP_520  | 0,00 €               |
| ALMERIENSE | DEUDA_LP_170  | 0,00 €               |
| ALMERIENSE | INTERESES_662 | 0,00 €               |
| CHEMIE     | BANCO_572     | 0,00 €               |
| CHEMIE     | DEUDA_CP_520  | 0,00 €               |
| CHEMIE     | DEUDA_LP_170  | 0,00 €               |
| CHEMIE     | INTERESES_662 | 0,00 €               |
| ECOCLEAN   | BANCO_572     | 0,00 €               |

### Advertencia crítica

Este bloque debe tratarse con cautela. En CHEMIE y ECOCLEAN aparecen saldos interpretados a cero en bancos/deuda, lo que puede deberse a asientos de cierre/apertura o a la forma de acumular diario. Para un saldo financiero fiable a 31/12/2025 conviene contrastar con:

- `SALDOSCONTABILIDAD`;
- extractos bancarios;
- balance oficial;
- cuadros de préstamos/leasing;
- cuentas 572/170/520 excluyendo asientos de cierre si aplica.

El bloque `21A9` sirve como **primer corte de control**, no como certificado de deuda bancaria.

## 8. Coherencias detectadas

- Ventas por cabecera y ventas por líneas cuadran por empresa.
- Compras por cabecera 2025 salen completas por empresa.
- Top clientes/proveedores se calcula contra el total de ventas/compras de cada empresa.
- El paquete es comparable en estructura con el cierre mensual de mayo 2026.
- El margen sigue siendo **estimado por coste medio de línea**, no margen contable cerrado.

## 9. Límites del dato

1. No es cierre contable oficial.
2. Margen de ALMERIENSE está contaminado y debe validarse.
3. Pendientes de clientes/proveedores incluyen saldos antiguos.
4. Bancos/deuda requieren validación adicional.
5. La clasificación operativo/patrimonial/intragrupo es textual y aproximada.
6. IVA, fiscalidad y operaciones vinculadas no deben concluirse solo con este paquete.

## 10. Uso recomendado

Este paquete sí sirve para:

- montar un primer cierre anual 2025;
- alimentar un dashboard histórico mínimo;
- comparar 2025 con cierres mensuales 2026;
- preparar preguntas para administración/asesoría;
- detectar principales clientes, proveedores, familias y márgenes estimados.

No sirve todavía para:

- liquidación fiscal;
- cierre contable definitivo;
- decisión de reparto de beneficios;
- valoración exacta de deuda bancaria;
- análisis laboral o nóminas.
