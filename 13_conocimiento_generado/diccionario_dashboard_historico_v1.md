# Diccionario dashboard histórico v1

## Objetivo
Explicar qué significa cada columna del dashboard histórico mínimo y con qué prudencia debe leerse.

Archivo principal asociado:
- `dashboard_historico_minimo_grupo_v2.csv`

---

## Columnas

### `periodo`
Periodo del dato.
Ejemplos:
- `2024`
- `2025`
- `2026-05`

### `escala`
Tipo de corte:
- `anual`
- `mensual`

### `empresa`
Sociedad analizada:
- `CHEMIE`
- `ALMERIENSE`
- `ECOCLEAN`

### `ventas_sin_iva`
Ventas netas del periodo sin IVA.

### `compras_sin_iva`
Compras netas del periodo sin IVA.

### `margen_bruto_estimado`
Margen bruto estimado a partir de coste medio/precio medio de compra por línea.

### `margen_pct_estimado`
Porcentaje estimado de margen bruto sobre ventas.

### `clientes_con_venta`
Número de clientes con venta en ese periodo.

### `proveedores_con_compra`
Número de proveedores con compra en ese periodo.

### `pendiente_clientes_top30`
Suma de pendiente estimado dentro del top 30 por importe a cierre del periodo.

### `pendiente_proveedores_top30`
Suma de pendiente estimado dentro del top 30 por importe a cierre del periodo.

### `clasificacion_dominante`
Lectura simplificada del tipo de actividad predominante.
Ejemplos:
- `MERCADO_OPERATIVO`
- `MIXTO_MERCADO_PATRIMONIAL_INTRAGRUPO`

### `top_cliente_principal`
Cliente con mayor peso en el periodo.

### `top_cliente_pct`
Porcentaje del principal cliente sobre ventas del periodo.

### `top_proveedor_principal`
Proveedor con mayor peso en compras del periodo.

### `top_proveedor_pct`
Porcentaje del principal proveedor sobre compras del periodo.

### `fiabilidad_operativa`
Juicio práctico sobre cuánto puede usarse ese corte para gestión operativa.

Valores orientativos:
- `alta`
- `media`
- `baja`

### `nota_lectura`
Comentario corto para no leer la fila en bruto sin contexto.

---

## Fiabilidad por tipo de dato

### Alta
- ventas
- compras
- clientes con venta
- proveedores con compra
- top cliente y top proveedor
- porcentajes de concentración básicos

### Media
- margen bruto estimado
- clasificación dominante

### Baja o solo señal operativa
- pendientes clientes
- pendientes proveedores

### No incluidos como KPI serio todavía
- bancos finales
- deuda final
- intereses finales

---

## Reglas de prudencia
1. **No tratar el margen estimado como margen contable auditado.**
2. **No tratar pendientes como saldo limpio cobrable/pagable.**
3. **No leer Almeriense sin contexto de mezcla de capas.**
4. **No comparar un mes con un año como si fueran magnitudes equivalentes; comparar patrones, no solo cifras absolutas.**

---

## Uso bueno
Este dashboard sirve para:
- control histórico mínimo
- comparación rápida entre empresas
- seguimiento de concentración
- lectura ejecutiva periódica

No sirve todavía para:
- cierre contable oficial
- caja/deuda final fiable
- decisión fiscal o societaria formal
