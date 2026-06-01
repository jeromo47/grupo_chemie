# 15A_resumen_ejecutivo_grupo

## Dato confirmado
- Base exclusiva: CSV de `13_CONSULTAS_CONTROL`.
- La referencia de ventas válida es `13C_control_recuento_por_empresa_ventas_lineas_CORREGIDO.csv`.

## Grupo - focos principales
- Las operaciones intragrupo por facturas aparecen en volumen bajo en `13J10_operaciones_intragrupo.csv`.
- Lo más sensible del grupo se concentra en 551, 752, 758, inmovilizado y saldos.
- Las diferencias IVA facturas vs diario deben leerse como control de coherencia, no como conclusión fiscal definitiva.
- Stock y lotes no deben usarse como inventario real sin depuración.

## Resumen por empresa

### CHEMIE
| foco | evidencia concreta | archivo origen |
|---|---|---|
| mejora de ventas/core 2025 | ventas core 2024=584.507,02 €; 2025=598.215,05 €; margen core 2024=281.609,71 €; 2025=286.569,37 € | `13C_control_recuento_por_empresa_ventas_lineas_CORREGIDO.csv` |
| ventas sin coste en NO_CORE | no core 2025: sin coste=157, margen negativo=14 | `13C_control_recuento_por_empresa_ventas_lineas_CORREGIDO.csv` |
| bajas/ventas de inmovilizado 2025 | altas=25.938,22 €, bajas=67.405,07 €, pérdida 671=17.127,20 €, beneficio 771=1.357,46 € | `13J12_inmovilizado_resumen.csv` |
| stock con negativos | artículos stock negativo=218, stock cero=235, valor stock coste medio=176.851,44 € | `13J03_stock_por_empresa.csv` |
| operaciones con vinculadas/personas | movimientos sensibles=49, intragrupo facturas=5 | `13J13_movimientos_sensibles_551_752_758.csv`, `13J10_operaciones_intragrupo.csv` |

### Interpretación prudente
- La mejora core 2025 es visible en la capa de control, pero no debe confundirse automáticamente con mejora limpia de todo el negocio si no se separan no core e inmovilizado.

### Pendiente de validar
- Detalle documental de bajas/ventas de inmovilizado 2025 y del contenido exacto de movimientos sensibles con personas o vinculadas.

### ALMERIENSE / ACI
| foco | evidencia concreta | archivo origen |
|---|---|---|
| margen 2025 core distorsionado | ventas=113.542,53 €, sin coste=7, margen negativo=59 | `13C_control_recuento_por_empresa_ventas_lineas_CORREGIDO.csv` |
| stock totalmente contaminado | artículos stock negativo=594, stock cero=573, valor stock coste medio=-17.570.893,15 € | `13J03_stock_por_empresa.csv` |
| referencia genérica / maestro | la existencia de margen negativo y ventas sin coste exige depuración del maestro y de referencias genéricas | `13J06B_resumen_margen_negativo_por_producto.csv`, `13J07B_resumen_ventas_sin_coste_por_producto.csv` |
| CANALEX y clientes pendientes | pendiente ajustado total=61.576,65 €; el detalle fino de CANALEX debe validarse en top pendientes | `13D_control_clientes_pendientes_empresa.csv`, `13J04_top25_clientes_pendientes.csv` |
| parte patrimonial | Piso Bobar, Vivienda Macenas y Nave Sierra Almijara requieren soporte documental adicional; no constan cerrados solo con estos CSV | `13J12_inmovilizado_resumen.csv` como apoyo parcial |
| alquileres 752 si aparecen / relación con CHEMIE por nave | movimientos sensibles detectados=89; la relación por nave requiere soporte adicional | `13J13_movimientos_sensibles_551_752_758.csv`, `13J10_operaciones_intragrupo.csv` |

### Interpretación prudente
- ALMERIENSE/ACI es la entidad con más señales de distorsión en margen, maestro y stock dentro de esta capa de control.

### Pendiente de validar
- Qué parte del margen 2025 core es utilizable tras depurar referencias genéricas, maestro y stock; y qué soporte documental patrimonial existe sobre Bobar, Macenas y Sierra Almijara.

### ECOCLEAN
| foco | evidencia concreta | archivo origen |
|---|---|---|
| ventas estables pero menor volumen | ventas core 2024=91.760,40 €; 2025=88.655,85 € | `13C_control_recuento_por_empresa_ventas_lineas_CORREGIDO.csv` |
| stock negativo | artículos stock negativo=300, stock cero=259, valor stock coste medio=-232.917,94 € | `13J03_stock_por_empresa.csv` |
| lotes caducados con cantidad positiva | registros detectados=780 | `13J09_lotes_caducados_cantidad_positiva.csv` |
| ausencia de 472/477 en diario aunque hay IVA en facturas | requiere contraste adicional; no cerrar lectura fiscal | `13J11_diferencias_iva_facturas_vs_diario.csv`, `13I_control_iva_resumen.csv` |
| sin módulo comercial CLIENTESCOMERCIAL | no consta en los archivos disponibles de control directo | no consta en los archivos disponibles |
| dependencia operativa/comercial del grupo | intragrupo facturas=1, movimientos sensibles=894 | `13J10_operaciones_intragrupo.csv`, `13J13_movimientos_sensibles_551_752_758.csv` |

### Interpretación prudente
- ECOCLEAN presenta una escala menor y señales de dependencia del grupo más visibles que CHEMIE.

### Pendiente de validar
- Qué significa exactamente la capa IVA/diario y qué parte del stock/lotes es operativamente fiable.