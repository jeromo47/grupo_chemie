# 22A - Validación cierre anual 2024 Grupo Familiar

## Alcance

Paquete generado desde BBDD/MasterSQL para el ejercicio 2024, con las sociedades CHEMIE, ALMERIENSE/ACI y ECOCLEAN.

El paquete es comparable con el cierre anual 2025 y con el cierre mensual mayo 2026.

## Archivos incluidos

- `GRUPO_22A1_ventas_empresa_2024.csv`
- `GRUPO_22A10_ventas_clasificacion_simple_2024.csv`
- `GRUPO_22A2_top_clientes_2024.csv`
- `GRUPO_22A3_ventas_coste_margen_empresa_2024.csv`
- `GRUPO_22A4_top_familias_2024.csv`
- `GRUPO_22A5_compras_empresa_2024.csv`
- `GRUPO_22A6_top_proveedores_2024.csv`
- `GRUPO_22A7_clientes_pendientes_cierre_2024.csv`
- `GRUPO_22A8_proveedores_pendientes_cierre_2024.csv`
- `GRUPO_22A9_bancos_deuda_intereses_cierre_2024.csv`

## Resumen económico 2024

| Empresa | Ventas s/IVA | Coste estimado | Margen estimado | Margen % | Compras s/IVA |
|---|---:|---:|---:|---:|---:|
| CHEMIE | 586.346,17 € | 308.196,93 € | 278.149,24 € | 47,44% | 421.194,10 € |
| ALMERIENSE | 145.361,86 € | 75.183,41 € | 70.178,43 € | 48,28% | 92.526,94 € |
| ECOCLEAN | 92.370,34 € | 54.911,43 € | 37.458,91 € | 40,55% | 33.538,40 € |
| **TOTAL GRUPO** | **824.078,37 €** | **438.291,77 €** | **385.786,58 €** | **46,81%** | **547.259,44 €** |

## Comprobaciones de coherencia

### Ventas cabecera vs líneas

| Empresa | Ventas cabecera | Ventas líneas | Diferencia | Lectura |
|---|---:|---:|---:|---|
| CHEMIE | 586.346,17 € | 586.346,17 € | 0,00 € | OK |
| ALMERIENSE | 145.361,86 € | 145.361,84 € | -0,02 € | OK |
| ECOCLEAN | 92.370,34 € | 92.370,34 € | 0,00 € | OK |

Lectura: las ventas cuadran razonablemente. La pequeña diferencia en ALMERIENSE es de redondeo/céntimos.

### Compras

Las compras se han extraído desde `GENERALFACTUP`. Sirven como primer corte anual por factura/proveedor. No sustituyen a una revisión contable/fiscal cerrada.

## Clasificación simple de ventas 2024

| Empresa | Clasificación | Ventas s/IVA | Coste estimado | Margen estimado |
|---|---|---:|---:|---:|
| ALMERIENSE | INTRAGRUPO_VINCULADA | 9.417,60 € | 1.522,12 € | 7.895,48 € |
| ALMERIENSE | MERCADO_OPERATIVO | 114.341,35 € | 73.661,29 € | 40.680,06 € |
| ALMERIENSE | PATRIMONIAL_NO_CORE | 21.602,89 € | 0,00 € | 21.602,89 € |
| CHEMIE | INTRAGRUPO_VINCULADA | 1.976,00 € | 1.742,79 € | 233,21 € |
| CHEMIE | MERCADO_OPERATIVO | 584.370,17 € | 306.454,15 € | 277.916,02 € |
| CHEMIE | PATRIMONIAL_NO_CORE | 0,00 € | 0,00 € | 0,00 € |
| ECOCLEAN | MERCADO_OPERATIVO | 92.370,34 € | 54.911,43 € | 37.458,91 € |

Advertencia: la clasificación `MERCADO_OPERATIVO / PATRIMONIAL_NO_CORE / INTRAGRUPO_VINCULADA` es una heurística simple por razón social y descripción de línea. Es útil para primer control, pero no debe tomarse como clasificación contable definitiva.

## Clientes y proveedores pendientes a 31/12/2024

| Empresa | Clientes pendientes estimados top 30 | Proveedores pendientes estimados top 30 |
|---|---:|---:|
| ALMERIENSE | 185.925,52 € | 88.588,25 € |
| CHEMIE | 239.720,38 € | 145.275,88 € |
| ECOCLEAN | 16.529,06 € | 4.837,50 € |

Hay saldos con vencimientos muy antiguos. Deben tratarse como cartera estimada a revisar, no como cobrable/pagable limpio.

Ejemplos de antigüedad máxima detectada:

| Empresa | Cliente | Pendiente | Vto más antiguo | Días vencido |
|---|---|---:|---|---:|
| ECOCLEAN | EMILIO MALPICA EXPOSITO, S.L. | 271,28 € | 2022-04-15 | 991 |
| ALMERIENSE | AGRUPA ADRA, S.A. | 11.423,48 € | 2022-07-30 | 885 |
| CHEMIE | AGRUPA ADRA, S.A. | 3.989,31 € | 2022-07-30 | 885 |
| ALMERIENSE | FRIO MAGO, S.L. | 18,56 € | 2003-06-30 | 7855 |
| ALMERIENSE | FRANCISCO MARTINEZ ESPINOSA | 370,26 € | 2024-10-15 | 77 |

## Bancos, deuda e intereses

| Empresa | Tipo cuenta | Saldo interpretado | Debe acumulado | Haber acumulado |
|---|---|---:|---:|---:|
| ALMERIENSE | BANCO_572 | 2.200,45 € | 6.864.298,08 € | 6.862.097,63 € |
| ALMERIENSE | DEUDA_CP_520 | 0,00 € | 215.386,21 € | 215.386,21 € |
| ALMERIENSE | DEUDA_LP_170 | 0,00 € | 4.815.025,45 € | 4.815.025,45 € |
| ALMERIENSE | INTERESES_662 | 0,00 € | 955,43 € | 955,43 € |
| CHEMIE | BANCO_572 | 0,00 € | 11.487.762,89 € | 11.487.762,89 € |
| CHEMIE | DEUDA_CP_520 | 0,00 € | 177.992,79 € | 177.992,79 € |
| CHEMIE | DEUDA_LP_170 | 0,00 € | 1.574.260,79 € | 1.574.260,79 € |
| CHEMIE | INTERESES_662 | 0,00 € | 4.615,05 € | 4.615,05 € |
| ECOCLEAN | BANCO_572 | 0,00 € | 751.041,89 € | 751.041,89 € |

Advertencia específica: el bloque de bancos/deuda/intereses no debe leerse como certificado financiero. En varias cuentas 170/520/572 el saldo interpretado sale cero por acumulación de debe/haber, cierres o movimientos históricos. Para saldo financiero definitivo conviene contrastar con balance, extractos bancarios, cuadros de amortización y/o `SALDOSCONTABILIDAD`.

Para intereses `662`, el saldo neto puede salir a cero si se incluyen asientos de cierre/regularización. El gasto financiero real del ejercicio debe revisarse por el Debe acumulado o mediante una extracción excluyendo cierre/regularización.

## Lectura por empresa

### CHEMIE

- Ventas 2024: 586.346,17 €.
- Margen estimado: 278.149,24 € (47,44%).
- Las ventas y líneas cuadran. El margen parece razonablemente coherente como estimación operativa.

### ALMERIENSE / ACI

- Ventas 2024: 145.361,86 €.
- Margen estimado: 70.178,43 € (48,28%).
- En 2024 el margen estimado sale positivo, a diferencia del problema fuerte detectado en 2025. Aun así, debe leerse con cautela por referencias genéricas, patrimonial/no core y calidad del maestro.

### ECOCLEAN

- Ventas 2024: 92.370,34 €.
- Margen estimado: 37.458,91 € (40,55%).
- Las ventas y margen estimado son razonables como primer corte operativo. Revisar con las advertencias ya vistas en lotes, stock e IVA si se cruza con módulos anteriores.

## Qué cuadra

- El paquete contiene los 10 bloques solicitados.
- Las ventas de cabecera y ventas por líneas cuadran razonablemente.
- Compras, top clientes, top proveedores y familias se han generado de forma consistente.
- El paquete es comparable con el cierre anual 2025 y el cierre mensual mayo 2026.

## Qué no debe darse por definitivo

- Margen bruto: estimado por coste medio/precio medio de compra en líneas. No es margen contable auditado.
- Pendientes: pueden incluir saldos históricos, vencimientos antiguos y efectos no depurados.
- Bancos/deuda: primer corte operativo, no saldo bancario/deuda certificado.
- Clasificación mercado/patrimonial/intragrupo: heurística simple, útil para análisis inicial pero no para cierre formal.

## Próximo uso recomendado

Pasar al agente:

- `22A_PAQUETE_CIERRE_ANUAL_2024_CSV_LIMPIO.zip`
- `22A_VALIDACION_CIERRE_ANUAL_2024.md`

Objetivo posterior: cargar 2024, 2025 y mayo 2026 en un mismo módulo comparativo para montar dashboard histórico mínimo.