# Guía rápida Excel / Power BI para dashboard histórico v1

## Archivo base recomendado
- `dashboard_historico_minimo_grupo_v2.csv`

---

## 1. Qué haría yo en Excel primero
### Hoja 1 - Tabla base
Importar el CSV tal cual, sin tocar columnas originales.

### Hoja 2 - Resumen visual
Hacer 4 bloques simples:
1. ventas por empresa y periodo
2. margen % por empresa y periodo
3. top cliente % por empresa y periodo
4. top proveedor % por empresa y periodo

### Hoja 3 - Alertas
Mostrar solo:
- filas con `fiabilidad_operativa = baja`
- pendientes altos
- concentración alta de cliente/proveedor

---

## 2. Gráficos que sí haría
### A. Barras de ventas por empresa
- eje X: periodo
- series: empresa
- valor: `ventas_sin_iva`

### B. Barras de margen % por empresa
- eje X: periodo
- series: empresa
- valor: `margen_pct_estimado`

### C. Concentración cliente principal
- eje X: periodo
- series: empresa
- valor: `top_cliente_pct`

### D. Concentración proveedor principal
- eje X: periodo
- series: empresa
- valor: `top_proveedor_pct`

### E. Pendientes top 30
- usarlo mejor como tabla o semáforo que como gráfico grande

---

## 3. Qué pondría arriba del dashboard
### KPIs visibles
- ventas del último corte
- margen % del último corte
- cliente principal del último corte
- proveedor principal del último corte
- comentario corto / alerta

---

## 4. Cómo leerlo bien
### Orden de lectura recomendado
1. ventas
2. margen
3. concentración cliente
4. concentración proveedor
5. pendientes
6. nota de lectura

---

## 5. Qué no haría todavía
- no meter bancos/deuda hasta limpiar mejor esa capa
- no hacer 20 gráficos
- no automatizar demasiado pronto
- no perder la nota cualitativa de lectura

---

## 6. Si lo llevas a Power BI
### Modelo mínimo
Una sola tabla basta para empezar:
- `dashboard_historico_minimo_grupo_v2`

### Segmentadores útiles
- periodo
- escala
- empresa
- fiabilidad_operativa

### Visuales mínimos
- tabla resumen
- barras ventas
- barras margen
- tarjetas de top cliente / top proveedor
- matriz de pendientes

---

## 7. Evolución futura razonable
### v2 del dashboard
Añadir:
- top cliente nombre + peso
- top proveedor nombre + peso
- más meses 2026

### v3 del dashboard
Añadir, si se limpia bien:
- bancos finales reales
- deuda final real
- mejor separación de pendientes recientes vs fósiles

---

## Conclusión
La forma buena de empezar no es hacer un Power BI enorme.
Es montar un cuadro simple, legible y repetible sobre una tabla que ya tenga criterio dentro.
