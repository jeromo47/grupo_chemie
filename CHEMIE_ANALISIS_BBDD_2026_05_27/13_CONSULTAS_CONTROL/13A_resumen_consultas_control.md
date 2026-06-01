# 13A - Resumen consultas control

Fuente principal usada: `/home/jero/cloud/02_proyectos/grupo_familiar/CHEMIE_ANALISIS_BBDD_2026_05_27/00_INPUT/CHEMIE_AGENT_INPUT/11_BASE_LOCAL/chemie_grupo.duckdb`

## CSV generados en Fase 2 y Fase 2B

- `13B_control_tablas_cargadas.csv`
- `13C_control_recuento_por_empresa_ventas_lineas.csv`
- `13C_control_recuento_por_empresa_ventas_lineas_CORREGIDO.csv`
- `13D_control_clientes_pendientes_empresa.csv`
- `13E_control_proveedores_pendientes_empresa.csv`
- `13F_control_bancos_deuda_por_empresa_cuenta.csv`
- `13G_control_diario_sensible_flags.csv`
- `13H_control_vinculadas_resumen.csv`
- `13I_control_iva_resumen.csv`
- `13J01_ventas_por_empresa_y_anio.csv`
- `13J02_compras_por_empresa_y_anio.csv`
- `13J03_stock_por_empresa.csv`
- `13J04_top25_clientes_pendientes.csv`
- `13J05_top_proveedores_pendientes_gestion.csv`
- `13J06B_resumen_margen_negativo_por_producto.csv`
- `13J06_productos_margen_negativo.csv`
- `13J07B_resumen_ventas_sin_coste_por_producto.csv`
- `13J07_ventas_sin_coste.csv`
- `13J08_articulos_pvp_menor_coste.csv`
- `13J09_lotes_caducados_cantidad_positiva.csv`
- `13J10_operaciones_intragrupo.csv`
- `13J11_diferencias_iva_facturas_vs_diario.csv`
- `13J12_inmovilizado_resumen.csv`
- `13J13_movimientos_sensibles_551_752_758.csv`

## Incidencias principales detectadas en la capa de control
- La lógica de flags de ventas se ha corregido tratándolos como texto/booleano compatible (`1`, `T`, `TRUE`, variantes en minúscula), no solo como número.
- Los importes llegan como texto y requieren conversión segura antes de agregarse.
- La presencia de líneas sin coste o con margen negativo depende de la calidad previa del maestro, del coste medio y del tipo de línea cargada en origen.

## Limitaciones de los datos
- Las tablas cargadas en DuckDB proceden de exports previos y no equivalen por sí mismas a contabilidad oficial o inventario físico definitivo.
- Los importes numéricos se convierten con `TRY_CAST`, por lo que valores no parseables pasan a nulos y no deben confundirse con cero real.
- Los resultados de control no sustituyen validación documental o contable posterior.

## Archivos que sirven para pasar a informes
- `13C_control_recuento_por_empresa_ventas_lineas_CORREGIDO.csv`
- `13D_control_clientes_pendientes_empresa.csv`
- `13E_control_proveedores_pendientes_empresa.csv`
- `13F_control_bancos_deuda_por_empresa_cuenta.csv`
- `13G_control_diario_sensible_flags.csv`
- `13H_control_vinculadas_resumen.csv`
- `13I_control_iva_resumen.csv`
- `13J06B_resumen_margen_negativo_por_producto.csv`
- `13J07B_resumen_ventas_sin_coste_por_producto.csv`

## Nota
- Este resumen no constituye informe final ni conclusión estratégica; deja la evidencia ordenada para la siguiente fase.