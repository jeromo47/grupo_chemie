# 10J - Índice técnico de extracciones BBDD Grupo CHEMIE

## Objetivo

Este documento recoge el estado final de las extracciones realizadas desde las bases de datos Firebird/MasterSQL de:

- CHEMIE
- ALMERIENSE / ACI
- ECOCLEAN

Periodo principal analizado:

- 2024
- 2025

El objetivo ha sido extraer información auditable, reutilizable y estructurada para análisis, agente documental, base local y preparación de entrada de Jero en septiembre.

---

# 1. Fase inicial de validación

## Archivos base

- 01_validacion_total_grupo.txt
- 02_margen_clientes_proveedores_grupo.txt
- 03_cobros_bancos_deuda_grupo.txt
- 04_pyg_patrimonio_grupo.txt
- 05_incidencias_grupo.txt
- 06_productos_costes_y_anomalias_grupo.txt

## Uso

Estos archivos sirven como diagnóstico inicial y validación general.

Cubren:

- ventas
- compras
- facturas
- líneas
- clientes
- proveedores
- PYG
- patrimonio
- deuda
- bancos
- márgenes estimados
- primeras incidencias

---

# 2. Exports estructurados principales

## 07A - Ventas por línea

Archivo válido:

- 07A_ventas_lineas_grupo_2024_2025_LIMPIO.psv

Uso:

- análisis de ventas por línea
- producto
- familia
- cliente
- margen estimado
- líneas sin coste
- referencias genéricas
- líneas no core

Estado:

- válido
- usar versión LIMPIO

---

## 07B - Clientes pendientes

Archivo válido:

- 07B_clientes_pendientes_grupo_2025_LIMPIO.psv

Uso:

- cartera de clientes pendiente
- antigüedad
- deuda vencida
- deuda ajustada
- saldos dudosos
- clientes problemáticos

Estado:

- válido
- usar versión LIMPIO

Incidencia relevante:

- CANALEX en ALMERIENSE concentra pendiente relevante.
- Hay saldos antiguos que no deben tomarse automáticamente como cobrables.

---

## 07C - Proveedores pendientes

Archivo válido:

- 07C_proveedores_pendientes_grupo_2025_LIMPIO.psv

Uso:

- deuda real de proveedores
- separación bruto vs gestión
- vencimientos anulados

Estado:

- válido
- usar versión LIMPIO

Incidencia relevante:

- El bruto de proveedores estaba inflado por anulados.
- El pendiente real de gestión es bajo.

---

## 07D - Bancos y deuda

Archivo válido:

- 07D_bancos_deuda_grupo_2024_2025_LIMPIO.psv

Uso:

- bancos 572
- deuda 170/520
- intereses 662
- saldos de cierre
- movimientos financieros

Estado:

- válido
- usar versión LIMPIO

Incidencia relevante:

- La posición financiera mejora en 2025.
- Falta cruzar con contratos bancarios y cuadros de amortización.

---

## 07E - Diario sensible

Archivo válido:

- 07E_diario_sensible_grupo_2024_2025_LIMPIO.psv

Uso:

- cuentas 430
- 400
- 410
- 551
- 555
- 560
- 752
- 758
- 671
- 681
- 682
- 472
- 477

Estado:

- válido
- usar versión LIMPIO

Incidencias relevantes:

- ECOCLEAN tiene cuenta 758 recurrente.
- ALMERIENSE tiene alquileres 752 relevantes.
- Existen saldos 551 sensibles en las tres sociedades.

---

# 3. Maestros

## 07G - Artículos

Archivo válido:

- 07G_articulos_maestro_grupo_LIMPIO.psv

Uso:

- maestro de artículos
- familias
- referencias
- desuso
- control stock

Estado:

- válido

Incidencia:

- ALMERIENSE tiene referencias genéricas y duplicadas.

---

## 07H - Clientes

Archivo válido:

- 07H_clientes_maestro_grupo_LIMPIO.psv

Uso:

- maestro básico de clientes
- población
- provincia
- riesgo
- forma de pago
- cuenta contable

Estado:

- válido

---

## 07I - Proveedores

Archivo válido:

- 07I_proveedores_maestro_grupo_LIMPIO.psv

Uso:

- maestro básico de proveedores
- forma de pago
- cuenta contable
- datos base

Estado:

- válido

---

## 07J - Familias

Archivo válido:

- 07J_familias_maestro_grupo_LIMPIO.psv

Uso:

- familias comerciales
- clasificación de producto

Estado:

- válido

---

## 07K - Validación ventas vs maestro

Archivos válidos:

- 07K_validacion_ventas_vs_maestros_grupo_2024_2025.psv
- 07K_resumen_validacion_ventas_vs_maestros.psv

Uso:

- detectar referencias no existentes
- referencias duplicadas
- genéricas
- ventas sin coste
- ventas sin familia

Estado:

- válido

Incidencia:

- ALMERIENSE presenta el mayor problema de maestro.
- CHEMIE y ECOCLEAN tienen incidencias menores asociadas a líneas manuales/no core.

---

# 4. Registro de incidencias y roadmap

Archivos válidos:

- 08A_registro_incidencias_prioritarias.psv
- 08B_resumen_incidencias_para_septiembre.md
- 09_ROADMAP_ENTRADA_JERO.md

Uso:

- control de preguntas para septiembre
- priorización
- hoja de ruta de entrada
- incidencias por empresa
- foco mensual

Estado:

- válido

---

# 5. Módulos avanzados de extracción

## 10A - Descubrimiento avanzado

Archivos:

- 10A_descubrimiento_avanzado_grupo.psv
- 10A2_schema_recuento_candidatas_grupo.psv

Uso:

- descubrir tablas reales
- localizar módulos de stock, compras, precios, inmovilizado, comercial y lotes
- validar qué tablas tienen datos

Estado:

- válido

---

## 10B - Compras

Archivos válidos:

- 10B1_compras_cabecera_grupo_2024_2025_LIMPIO.psv
- 10B2_compras_lineas_grupo_2024_2025_LIMPIO.psv

Uso:

- compras por cabecera
- compras por proveedor
- compras de producto
- líneas de compra
- cobertura de compras por línea

Estado:

- válido

Criterio:

- GENERALFACTUP = compras totales.
- GENERALCOMPRAS = compras de producto / almacén.
- GENERALCOMPRAS no cubre el 100% de compras.

---

## 10C - Stock y movimientos de almacén

Archivos válidos:

- 10C1_stock_actual_grupo_LIMPIO.psv
- 10C2_movimientos_almacen_grupo_2024_2025_LIMPIO.psv
- 10C3_resumen_stock_grupo_LIMPIO.psv
- 10C4_anomalias_stock_grupo.psv

Uso:

- stock actual
- stock negativo
- stock cero
- stock bajo mínimo
- coste medio
- valoración de stock
- movimientos de almacén
- entradas/salidas

Estado:

- válido con advertencia

Incidencia:

- El stock no debe usarse como inventario real sin depuración.
- ALMERIENSE está muy contaminada por referencias genéricas y stock negativo.
- ECOCLEAN también tiene stock negativo relevante.
- CHEMIE es utilizable con depuración.

---

## 10D - Precios y descuentos

Archivos válidos:

- 10D1_precios_base_articulos_grupo_LIMPIO.psv
- 10D2_descuentos_cliente_articulo_grupo_LIMPIO.psv
- 10D3_resumen_precios_grupo_LIMPIO.psv
- 10D4_anomalias_precios_grupo.psv

Uso:

- PVP por artículo
- coste medio
- margen teórico
- descuentos cliente-artículo
- precios especiales
- anomalías de precio

Estado:

- válido

Incidencias:

- CHEMIE y ECOCLEAN comparten prácticamente la misma tabla de descuentos cliente-artículo.
- Existen precios especiales aparentemente por debajo de coste, pendiente de revisar unidades/cajas/formato/coste.

---

## 10E - Inmovilizado y amortizaciones

Archivos válidos:

- 10E1_amortizaciones_grupo_LIMPIO.psv
- 10E2_diario_inmovilizado_grupo_2024_2025_LIMPIO.psv
- 10E3_resumen_inmovilizado_grupo.psv
- 10E4_incidencias_inmovilizado_grupo.psv

Uso:

- activos amortizables
- vehículos
- naves
- viviendas
- amortización contable
- bajas de inmovilizado
- beneficios/pérdidas por venta de activos

Estado:

- válido

Incidencias:

- CHEMIE tiene movimientos relevantes de bajas/ventas de inmovilizado.
- ALMERIENSE tiene componente patrimonial claro.
- ECOCLEAN no tiene inmovilizado registrado en las tablas extraídas.

---

## 10F - Comercial y zonas

Archivos válidos:

- 10F1_clientes_comercial_grupo_LIMPIO.psv
- 10F2_zonas_grupo_LIMPIO.psv
- 10F3_zonas_bares_tarifas_grupo_LIMPIO.psv
- 10F4_resumen_comercial_grupo_LIMPIO.psv
- 10F5_resumen_validacion_comercial_grupo.psv

Uso:

- clientes comerciales
- zonas
- comerciales
- gestión comercial
- validación contra maestro de clientes

Estado:

- válido

Incidencia:

- ECOCLEAN no tiene clientes en CLIENTESCOMERCIAL.
- CHEMIE y ALMERIENSE sí tienen módulo comercial operativo.

---

## 10G - Lotes y caducidades

Archivos válidos:

- 10G1_lotes_grupo_LIMPIO.psv
- 10G2_etiquetas_lotes_grupo_LIMPIO.psv
- 10G3_resumen_lotes_caducidad_grupo_LIMPIO.psv
- 10G4_series_grupo_LIMPIO.psv
- 10G5_anomalias_lotes_caducidad_grupo.psv
- 10G6_resumen_validacion_lotes_grupo.psv

Uso:

- lotes
- caducidades
- etiquetas
- series
- lotes caducados
- lotes con cantidad positiva

Estado:

- válido con advertencia

Incidencia:

- CHEMIE y ECOCLEAN tienen muchos lotes caducados con cantidad positiva.
- No debe usarse como control sanitario real sin depurar.
- ALMERIENSE prácticamente no usa lotes.

---

## 10H - Operaciones vinculadas / intragrupo

Archivos válidos:

- 10H1_ventas_vinculadas_grupo_2024_2025_LIMPIO.psv
- 10H2_compras_vinculadas_grupo_2024_2025_LIMPIO.psv
- 10H3_diario_vinculadas_sensible_grupo_2024_2025_LIMPIO.psv
- 10H4_resumen_intragrupo_vinculadas.psv
- 10H5_falsos_positivos_excluidos.psv

Uso:

- ventas vinculadas
- compras vinculadas
- movimientos sensibles
- operaciones con sociedades/personas vinculadas
- falsos positivos excluidos

Estado:

- válido usando versiones limpias

Incidencia:

- Volumen facturado intragrupo detectado es bajo.
- Lo relevante está en alquileres, cuentas 551, inmovilizado/personas vinculadas y saldos.

---

## 10I - Fiscal / IVA

Archivos válidos:

- 10I1_iva_ventas_facturas_grupo_2024_2025_LIMPIO.psv
- 10I2_iva_compras_facturas_grupo_2024_2025_LIMPIO.psv
- 10I3_diario_iva_472_477_grupo_2024_2025_LIMPIO.psv
- 10I4_resumen_iva_grupo_2024_2025_LIMPIO.psv
- 10I5_resumen_diferencias_iva_facturas_vs_diario.psv

Uso:

- IVA ventas
- IVA compras
- cuentas 472 y 477
- diferencias facturación vs contabilidad

Estado:

- válido como control de coherencia
- no usar como liquidación fiscal oficial

Incidencias:

- CHEMIE 477 cuadra con ventas incluyendo anuladas.
- ALMERIENSE tiene diferencias relevantes entre facturas y 477.
- ECOCLEAN no presenta movimientos 472/477 en diario aunque sí tiene IVA en facturas.

---

# 6. Conclusión técnica

La extracción de BBDD está suficientemente avanzada para:

- análisis financiero
- análisis comercial
- análisis de stock
- análisis de compras
- análisis de precios
- análisis de clientes/proveedores
- análisis de inmovilizado
- análisis de IVA
- análisis intragrupo
- preparación de preguntas para septiembre
- carga en agente documental
- carga en base local DuckDB/SQLite

No se recomienda seguir sacando más tablas sin una necesidad concreta.

---

# 7. Próximo paso recomendado

Crear una base local estructurada con:

- ventas_lineas
- compras_cabecera
- compras_lineas
- stock_actual
- movimientos_almacen
- precios_base
- descuentos_cliente_articulo
- amortizaciones
- diario_inmovilizado
- clientes
- proveedores
- articulos
- familias
- clientes_pendientes
- proveedores_pendientes
- bancos_deuda
- diario_sensible
- iva_ventas
- iva_compras
- diario_iva
- lotes
- etiquetas_lotes
- intragrupo_ventas
- intragrupo_compras

Formato recomendado:

- DuckDB
- o SQLite

Prioridad recomendada:

- DuckDB para análisis.
- SQLite si se quiere compatibilidad máxima.