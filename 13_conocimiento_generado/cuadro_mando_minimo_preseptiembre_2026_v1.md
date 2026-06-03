# Cuadro de mando mínimo pre-septiembre 2026 v1

## Objetivo
Definir, antes de la incorporación presencial de Jero, un cuadro de mando mínimo útil para gobernar el grupo desde septiembre sin empezar desde cero.

Este documento no construye todavía el dashboard final.
Congela:
- qué indicadores importan
- por qué importan
- de qué fuente deberían salir
- qué periodicidad tendría sentido
- qué alerta o lectura básica deben activar

---

## Principio general
El cuadro de mando mínimo no debe intentar medirlo todo.
Debe responder a una pregunta muy concreta:

> **qué 8-12 señales necesito mirar con regularidad para no gobernar a ciegas**

---

## 1. Bloque ventas / cartera
## KPI 1. Ventas por empresa y periodo
### Qué mide
- evolución básica de ventas por empresa
- Chemie / ACI-ALMERIENSE / Ecoclean

### Fuente orientativa
- `t_07a_ventas_lineas_grupo_2024_2025`
- y resúmenes tipo `13J01` / derivados futuros

### Frecuencia ideal
- semanal resumida
- mensual formal

### Alerta útil
- caída brusca en una empresa
- crecimiento raro no explicado
- desajuste entre volumen y margen

---

## KPI 2. Concentración de clientes
### Qué mide
- peso del top 1 / top 3 / top 5 / top 10 por empresa

### Fuente orientativa
- `13J15_resumen_concentracion_clientes.csv`
- `13J31_clientes_dependencia_critica.csv`

### Frecuencia ideal
- mensual

### Alerta útil
- ALMERIENSE con dependencia excesiva de pocos clientes
- Chemie concentrándose más de lo razonable

---

## KPI 3. Top clientes críticos
### Qué mide
- clientes clave por empresa
- volumen
- tendencia
- margen orientativo

### Fuente orientativa
- `13J14_top10_clientes_concentracion_por_empresa_anio.csv`
- `13J18_top_clientes_detalle_cartera.csv`
- `13J19_top_clientes_maestro_enriquecido.csv`

### Frecuencia ideal
- mensual

### Alerta útil
- pérdida o deterioro de cliente clave
- cliente que pesa mucho pero deja poco margen o mucho ruido

---

## 2. Bloque margen / calidad comercial
## KPI 4. Margen total y margen por empresa
### Qué mide
- margen bruto estimado por empresa
- evolución mensual

### Fuente orientativa
- `t_07a_ventas_lineas_grupo_2024_2025`
- resúmenes actuales y futuros específicos

### Frecuencia ideal
- mensual

### Alerta útil
- mejora o deterioro no explicados
- casos como ALMERIENSE donde el dato debe leerse con cautela

---

## KPI 5. Margen por familias troncales
### Qué mide
- de dónde sale el dinero real
- qué familias sostienen cada empresa

### Fuente orientativa
- `13J20_margen_por_familia_empresa_anio.csv`
- `13J21_top_familias_ventas_y_margen.csv`
- `13J22_productos_top_margen_y_peor_margen.csv`

### Frecuencia ideal
- mensual

### Alerta útil
- caída de familias núcleo de Chemie
- crecimiento de ventas en familias que no dejan margen

---

## KPI 6. Incidencias de calidad comercial
### Qué mide
- líneas sin coste
- líneas con margen negativo
- referencias genéricas
- líneas sin familia

### Fuente orientativa
- `t_07a_ventas_lineas_grupo_2024_2025`
- `13J22_productos_top_margen_y_peor_margen.csv`

### Frecuencia ideal
- mensual

### Alerta útil
- crecimiento del ruido comercial
- empeoramiento de calidad de maestro o coste

---

## 3. Bloque compras / abastecimiento
## KPI 7. Compras por empresa y periodo
### Qué mide
- volumen básico de compras por empresa

### Fuente orientativa
- `t_10b1_compras_cabecera_grupo_2024_2025`
- resúmenes ya existentes y derivados

### Frecuencia ideal
- mensual

### Alerta útil
- subidas o bajadas no explicadas
- tensión rara de abastecimiento

---

## KPI 8. Concentración de proveedores
### Qué mide
- top 1 / top 3 / top 5 / top 10 de proveedores

### Fuente orientativa
- `13J24_resumen_concentracion_proveedores.csv`
- `13J32_proveedores_dependencia_critica.csv`

### Frecuencia ideal
- mensual

### Alerta útil
- dependencia excesiva de proveedor crítico
- fragilidad de abastecimiento en Chemie o Ecoclean

---

## KPI 9. Proveedores estratégicos
### Qué mide
- seguimiento de proveedores que sostienen el corazón del negocio

### Fuente orientativa
- `13J25_top_proveedores_maestro_enriquecido.csv`
- `13J26_compras_por_proveedor_y_familia.csv`

### Frecuencia ideal
- mensual

### Alerta útil
- caída de suministro, tensión comercial o exceso de dependencia

---

## 4. Bloque clientes/proveedores pendientes y tesorería
## KPI 10. Clientes pendientes ajustados
### Qué mide
- bolsa real de pendiente de clientes

### Fuente orientativa
- `t_07b_clientes_pendientes_grupo_2025`
- salidas ya generadas del módulo

### Frecuencia ideal
- mensual

### Alerta útil
- crecimiento raro de pendiente
- concentración excesiva en pocos nombres
- mezcla entre mora real y residuos históricos

---

## KPI 11. Proveedores pendientes / pagos
### Qué mide
- bolsa de pagos pendientes de gestión

### Fuente orientativa
- `t_07c_proveedores_pendientes_grupo_2025`
- salidas ya generadas del módulo

### Frecuencia ideal
- mensual

### Alerta útil
- tensión de tesorería
- deterioro de disciplina de pagos

---

## KPI 12. Bancos / deuda / tesorería
### Qué mide
- posición básica de bancos
- deuda CP/LP
- tensión financiera

### Fuente orientativa
- `t_07d_bancos_deuda_grupo_2024_2025`
- resúmenes de control de deuda y bancos

### Frecuencia ideal
- semanal resumida
- mensual formal

### Alerta útil
- deterioro de caja
- aumento raro de deuda
- subida de intereses

---

## 5. Bloque ACI / ALMERIENSE específico
## KPI 13. Separación por capas de ALMERIENSE
### Qué mide
- peso de mercado
- peso patrimonial / Booking-Macenas
- peso intragrupo
- ruido comercial/stock/coste

### Fuente orientativa
- `13J27_aci_almeriense_desglose_clientes_especiales.csv`
- `13J28_aci_almeriense_resumen_por_tipo_lectura.csv`
- `13J29_aci_almeriense_stock_anomalias_detalle.csv`
- `13J30_aci_almeriense_productos_ruido_top.csv`

### Frecuencia ideal
- mensual, al menos al principio

### Alerta útil
- seguir leyendo ALMERIENSE como una comercial limpia cuando no lo es

---

## 6. Bloque señales especiales
## KPI 14. Señales de vigilancia predefinidas
### Qué mide
- alertas rojas ya conocidas antes de entrar

### Fuente orientativa
- `13J33_senales_vigilancia_septiembre.csv`

### Frecuencia ideal
- revisión fija mensual
- y checklist al inicio de septiembre

### Alertas incluidas ya
- concentración extrema en ALMERIENSE
- margen mercado ACI/ALMERIENSE distorsionado
- stock contaminado
- concentración relevante de clientes/proveedores en Chemie

---

## 7. Qué no metería todavía en el cuadro de mando mínimo
- demasiados KPIs fiscales finos
- indicadores históricos de poco uso operativo inmediato
- detalle excesivo de inmovilizado salvo casos concretos
- métricas complejas no entendidas aún por la oficina

La idea es que el cuadro de mando nazca gobernable, no barroco.

---

## 8. Orden práctico de implantación
### Fase 1 - Imprescindibles desde septiembre
1. ventas por empresa
2. concentración de clientes
3. top clientes críticos
4. margen por empresa
5. compras por empresa
6. concentración de proveedores
7. clientes pendientes
8. bancos / deuda

### Fase 2 - Muy recomendable poco después
9. margen por familias
10. incidencias de calidad comercial
11. separación por capas de ALMERIENSE
12. señales especiales

---

## 9. Juicio final
El cuadro de mando mínimo ya puede definirse con bastante sentido antes de septiembre.

No porque todo esté cerrado al milímetro,
sino porque ya sabemos lo bastante sobre:
- qué empresas sostienen el grupo
- dónde están las concentraciones
- qué datos son fiables
- qué piezas están contaminadas
- y qué señales pueden hacer más daño si no se miran

### Traducción práctica
Lo difícil ya no es “qué mirar”.
Lo difícil será:
- disciplinarse para mirarlo cada mes
- no volver a improvisar
- y conectar el cuadro de mando con la realidad de oficina, comercial y tesorería cuando Jero entre.
