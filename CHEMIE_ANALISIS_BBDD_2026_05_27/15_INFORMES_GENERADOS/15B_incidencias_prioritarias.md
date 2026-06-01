# 15B_incidencias_prioritarias

## CHEMIE | prioridad alta
- **Evidencia concreta:** Mejora core 2025 coexistiendo con no core con sin coste y margen negativo
- **Riesgo:** Riesgo de mezclar mejora operativa con líneas especiales/no core
- **Archivo CSV origen:** `13C_control_recuento_por_empresa_ventas_lineas_CORREGIDO.csv`
- **Pregunta exacta para septiembre:** ¿Qué parte de la mejora 2025 de CHEMIE es negocio core limpio y qué parte está contaminada por no core?
- **Acción recomendada de validación:** Separar core, no core e inmovilizado en revisión de detalle.

## CHEMIE | prioridad alta
- **Evidencia concreta:** artículos stock negativo=218, stock cero=235, valor stock coste medio=176.851,44 €
- **Riesgo:** Riesgo de inventario de control no fiable sin depuración
- **Archivo CSV origen:** `13J03_stock_por_empresa.csv`
- **Pregunta exacta para septiembre:** ¿Qué parte del stock negativo de CHEMIE es error de sistema y qué parte operativa real?
- **Acción recomendada de validación:** Cruce con movimientos de almacén y validación física selectiva.

## ALMERIENSE | prioridad crítica
- **Evidencia concreta:** Margen 2025 core con 69 líneas sin coste y 59 con margen negativo
- **Riesgo:** Riesgo alto de margen 2025 distorsionado
- **Archivo CSV origen:** `13C_control_recuento_por_empresa_ventas_lineas_CORREGIDO.csv`
- **Pregunta exacta para septiembre:** ¿Qué peso tienen las referencias genéricas y el maestro en la distorsión del margen 2025 de ALMERIENSE?
- **Acción recomendada de validación:** Depuración prioritaria de maestro/coste/referencias genéricas.

## ALMERIENSE | prioridad alta
- **Evidencia concreta:** artículos stock negativo=594, stock cero=573, valor stock coste medio=-17.570.893,15 €
- **Riesgo:** Riesgo de stock contaminado y no utilizable como base económica
- **Archivo CSV origen:** `13J03_stock_por_empresa.csv`
- **Pregunta exacta para septiembre:** ¿Puede usarse el stock de ALMERIENSE como dato económico o solo como incidencia?
- **Acción recomendada de validación:** Excluir de cierres sin depuración adicional.

## ALMERIENSE | prioridad alta
- **Evidencia concreta:** Pendiente clientes=61.576,65 €; foco CANALEX pendiente de detalle
- **Riesgo:** Riesgo de concentración de saldos viejos o dudosos
- **Archivo CSV origen:** `13D_control_clientes_pendientes_empresa.csv / 13J04_top25_clientes_pendientes.csv`
- **Pregunta exacta para septiembre:** ¿Qué parte del pendiente de ALMERIENSE corresponde a CANALEX u otros clientes estructuralmente dudosos?
- **Acción recomendada de validación:** Bajar al detalle de top pendientes y validarlo con administración.

## ALMERIENSE | prioridad media
- **Evidencia concreta:** Parte patrimonial relevante (Piso Bobar, Vivienda Macenas, Nave Sierra Almijara) no cerrable solo con estos CSV
- **Riesgo:** Riesgo de sobrerresumir el componente patrimonial sin soporte documental
- **Archivo CSV origen:** `13J12_inmovilizado_resumen.csv`
- **Pregunta exacta para septiembre:** ¿Qué soporte patrimonial/documental existe sobre Bobar, Macenas y Sierra Almijara?
- **Acción recomendada de validación:** Cruzar con documentación patrimonial externa y soporte contable.

## ECOCLEAN | prioridad alta
- **Evidencia concreta:** artículos stock negativo=300, stock cero=259, valor stock coste medio=-232.917,94 €; lotes caducados con cantidad positiva=780
- **Riesgo:** Riesgo operativo de stock/lotes no fiables
- **Archivo CSV origen:** `13J03_stock_por_empresa.csv / 13J09_lotes_caducados_cantidad_positiva.csv`
- **Pregunta exacta para septiembre:** ¿Qué parte del stock y lotes de ECOCLEAN es utilizable y qué parte es residuo o error?
- **Acción recomendada de validación:** Cruce con almacén y limpieza de lotes.

## ECOCLEAN | prioridad media
- **Evidencia concreta:** Existe IVA en facturas, pero la lectura del diario exige contraste adicional
- **Riesgo:** Riesgo de incoherencia entre facturación e IVA diario sin cierre fiscal
- **Archivo CSV origen:** `13I_control_iva_resumen.csv / 13J11_diferencias_iva_facturas_vs_diario.csv`
- **Pregunta exacta para septiembre:** ¿Cómo se explica la relación entre facturas con IVA y diario 472/477 en ECOCLEAN?
- **Acción recomendada de validación:** Revisión con administración y asesoría sin conclusión fiscal cerrada.

## GRUPO | prioridad alta
- **Evidencia concreta:** Las facturas intragrupo son bajas; lo relevante está en 551, 752, 758, inmovilizado y saldos
- **Riesgo:** Riesgo de infravalorar la capa intragrupo real si se mira solo la facturación
- **Archivo CSV origen:** `13J10_operaciones_intragrupo.csv / 13J13_movimientos_sensibles_551_752_758.csv / 13J12_inmovilizado_resumen.csv`
- **Pregunta exacta para septiembre:** ¿Qué parte del riesgo intragrupo del grupo está fuera de las facturas?
- **Acción recomendada de validación:** Priorizar revisión de movimientos sensibles y saldos.

## GRUPO | prioridad media
- **Evidencia concreta:** Stock y lotes sirven como control, no como inventario real fiable
- **Riesgo:** Riesgo de usar datos de control como cierre real
- **Archivo CSV origen:** `13J03_stock_por_empresa.csv / 13J09_lotes_caducados_cantidad_positiva.csv`
- **Pregunta exacta para septiembre:** ¿Qué módulos del grupo pueden usarse ya para control y cuáles exigen depuración?
- **Acción recomendada de validación:** Etiquetar stock/lotes como capa de control mientras no se depuren.
