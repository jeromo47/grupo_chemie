# Mapa de archivos del proyecto CHEMIE

## Estado
Mapa maestro de archivos y artefactos usados en la capa económica, documental y de extracción del proyecto CHEMIE.

## Reglas de clasificación
- **FUENTE**: archivo primario recibido o extraído.
- **DERIVADO**: resumen, informe o export generado a partir de fuente.
- **CONTROL**: índice, incidencia, roadmap, preguntas, versionado.
- **SQL**: script de extracción o descubrimiento.

## Entradas iniciales conocidas

### Fuentes principales del paquete 2024-2025
- `Informe_Grupo_CHEMIE_2024_2025_Estilo_Consultoria.pdf` — FUENTE
- `Informe_Grupo_CHEMIE_2024_2025_Estilo_Consultoria.docx` — FUENTE
- `01_validacion_total_grupo.txt` — FUENTE
- `02_margen_clientes_proveedores_grupo.txt` — FUENTE
- `03_cobros_bancos_deuda_grupo.txt` — FUENTE
- `04_pyg_patrimonio_grupo.txt` — FUENTE
- `05_incidencias_grupo.txt` — FUENTE si existe en carpeta efectiva; si no, PENDIENTE DE INCORPORAR
- `06_productos_costes_y_anomalias_grupo.txt` — FUENTE si existe en carpeta efectiva; si no, PENDIENTE DE INCORPORAR
- `00_schema_tablas_clave_grupo.txt` — FUENTE/CONTROL si existe en carpeta efectiva; si no, PENDIENTE DE INCORPORAR

### SQL / extracción técnica Firebird
- `00_schema_tablas_clave_chemie.sql` — SQL
- `00_schema_tablas_clave_almeriense.sql` — SQL
- `00_schema_tablas_clave_ecoclean.sql` — SQL
- `01_validacion_total_chemie.sql` — SQL
- `01_validacion_total_almeriense.sql` — SQL
- `01_validacion_total_ecoclean.sql` — SQL
- `02_margen_clientes_proveedores_chemie.sql` — SQL
- `02_margen_clientes_proveedores_almeriense.sql` — SQL
- `02_margen_clientes_proveedores_ecoclean.sql` — SQL
- `03_cobros_bancos_deuda_chemie.sql` — SQL
- `03_cobros_bancos_deuda_almeriense.sql` — SQL
- `03_cobros_bancos_deuda_ecoclean.sql` — SQL
- `04_pyg_patrimonio_chemie.sql` — SQL
- `04_pyg_patrimonio_almeriense.sql` — SQL
- `04_pyg_patrimonio_ecoclean.sql` — SQL
- `05_incidencias_chemie.sql` — SQL
- `05_incidencias_almeriense.sql` — SQL
- `05_incidencias_ecoclean.sql` — SQL

### Derivados analíticos ya consolidados
- `validacion_economica_nucleo_v1.md` — DERIVADO
- `revision_alertas_contables_nucleo_v1.md` — DERIVADO
- `auditoria_saldos_antiguos_clientes_chemie_v1.md` — DERIVADO
- `auditoria_vinculadas_nucleo_v1.md` — DERIVADO
- `mini_auditoria_operacion_chemie_jeronimo_molina_caparros_v1.md` — DERIVADO
- `mini_auditoria_mejora_financiera_chemie_2025_v1.md` — DERIVADO
- `mini_auditoria_desapalancamiento_chemie_2025_v1.md` — DERIVADO
- `mini_auditoria_saldos_viejos_chemie_v2.md` — DERIVADO
- `mini_auditoria_pendiente_real_clientes_chemie_v1.md` — DERIVADO
- `auditoria_economica_corta_chemie_v1.md` — DERIVADO
- `mapa_priorizado_extraccion_bd_chemie_v1.md` — DERIVADO/CONTROL
- `soporte_documental_alquiler_aci_chemie_v1.md` — DERIVADO
- `confirmacion_documental_operacion_ducati_chemie_jero_v1.md` — DERIVADO
- `cruce_economico_patrimonial_nucleo_v1.md` — DERIVADO
- `sintesis_integrada_nucleo_v1.md` — DERIVADO MAESTRO
- `sintesis_cierre_fase_nucleo_v1.md` — DERIVADO DE CIERRE

## Pendientes de completar en este mapa
- rutas exactas efectivas de `05_incidencias_grupo.txt`, `06_productos_costes_y_anomalias_grupo.txt` y `00_schema_tablas_clave_grupo.txt`
- artefactos concretos generados en el descubrimiento Firebird de mayo 2026 para CHEMIE
- separación explícita entre archivos provisionales, operativos y definitivos en la rama SQL/exportes


## Ingesta 2026-05-27 - CHEMIE_AGENT_INPUT

### Carpeta de entrada
- `/home/jero/cloud/02_proyectos/grupo_familiar/00_inbox/2026-05-27_chemie_agent_input/CHEMIE_AGENT_INPUT` — FUENTE AGRUPADA / ENTREGA ESTRUCTURADA

### Control de entrega
- `00_CONTROL/00_MANIFIESTO_PROYECTO_CHEMIE.md` — CONTROL/FUENTE DESCRIPTIVA
- `00_CONTROL/01_MAPA_ARCHIVOS_ENTREGA.txt` — CONTROL
- `00_CONTROL/08B_resumen_incidencias_para_septiembre.md` — CONTROL/DERIVADO
- `00_CONTROL/09_ROADMAP_ENTRADA_JERO.md` — CONTROL/DERIVADO
- `00_CONTROL/10J_ARCHIVOS_VALIDOS_ENTREGA_AGENTE.txt` — CONTROL
- `00_CONTROL/10J_INDICE_TECNICO_EXTRACCIONES.md` — CONTROL TÉCNICO MAESTRO

### Fuentes textuales y estructuradas añadidas
- `01_TXT_FUENTE/05_incidencias_grupo.txt` — FUENTE ya confirmada en esta entrega
- `01_TXT_FUENTE/06_productos_costes_y_anomalias_grupo.txt` — FUENTE ya confirmada en esta entrega
- `01_TXT_FUENTE/00_schema_tablas_clave_grupo.txt` — FUENTE/CONTROL ya confirmada en esta entrega
- `01_TXT_FUENTE/07A_ventas_lineas_grupo_2024_2025_LIMPIO.psv` — FUENTE ESTRUCTURADA
- `01_TXT_FUENTE/07B_clientes_pendientes_grupo_2025_LIMPIO.psv` — FUENTE ESTRUCTURADA
- `01_TXT_FUENTE/07C_proveedores_pendientes_grupo_2025_LIMPIO.psv` — FUENTE ESTRUCTURADA
- `01_TXT_FUENTE/07D_bancos_deuda_grupo_2024_2025_LIMPIO.psv` — FUENTE ESTRUCTURADA
- `01_TXT_FUENTE/07E_diario_sensible_grupo_2024_2025_LIMPIO.psv` — FUENTE ESTRUCTURADA
- `01_TXT_FUENTE/07G_...` a `10I5_...` — FUENTES ESTRUCTURADAS adicionales ya listadas y validadas por el índice técnico `10J`

### Base local incluida en la entrega
- `11_BASE_LOCAL/chemie_grupo.duckdb` — DERIVADO OPERATIVO / BASE LOCAL
- `11_BASE_LOCAL/11A_log_carga_duckdb.txt` — CONTROL TÉCNICO

### Basura técnica a ignorar
- `__MACOSX/...` — NO USAR / BASURA DE EMPAQUETADO
