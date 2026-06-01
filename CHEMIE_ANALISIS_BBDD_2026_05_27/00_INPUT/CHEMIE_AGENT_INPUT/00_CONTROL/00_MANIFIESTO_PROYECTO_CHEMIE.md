# MANIFIESTO PROYECTO CHEMIE

## Objetivo

Este paquete contiene la extracción y análisis inicial 2024-2025 del grupo CHEMIE, formado por:

- CHEMIE
- ACI / Almeriense
- ECOCLEAN

El objetivo es conservar memoria documental, técnica y financiera para análisis posterior.

## Archivos principales válidos

- 00_schema_tablas_clave_grupo.txt
- 01_validacion_total_grupo.txt
- 02_margen_clientes_proveedores_grupo.txt
- 03_cobros_bancos_deuda_grupo.txt
- 04_pyg_patrimonio_grupo.txt
- 05_incidencias_grupo.txt

Archivo Bloque 06 generado y válido:

- 06_productos_costes_y_anomalias_grupo.txt

Conclusión del Bloque 06:
- CHEMIE mejora margen depurado en 2025.
- ACI/Almeriense tenía el margen 2025 distorsionado por referencias genéricas, especialmente 999999. Al excluir genéricas, el margen depurado 2025 pasa a ser positivo.
- ECOCLEAN baja ventas, pero mejora margen depurado.
- Sigue pendiente explicar la cuenta 758 de ECOCLEAN desde contabilidad.

## Reglas

1. No inventar datos.
2. No inventar tablas ni columnas.
3. No asumir relaciones no demostradas.
4. Separar siempre CHEMIE, ACI/Almeriense, ECOCLEAN y GRUPO.
5. Separar ventas core, no core, operaciones intragrupo, alquileres, vehículos, extraordinarios y vinculadas.
6. Si un dato no está en los archivos, responder: “no consta en la documentación disponible”.
7. El margen de Almeriense 2025 no debe usarse como real sin depurar referencias genéricas.
8. Las ventas sin coste medio de CHEMIE 2025 parecen estar explicadas principalmente por vehículos/repercusiones, no por producto ordinario.
9. La cuenta 758 de ECOCLEAN debe aclararse antes de interpretar su resultado como margen operativo real.
10. Este agente solo archiva, resume y mantiene memoria; no dirige el análisis.

## Incidencias prioritarias

### CHEMIE

- Ventas sin coste medio en 2025.
- Principalmente operaciones no core: vehículos/repercusiones.
- Separar del negocio ordinario.

### ACI / Almeriense

- Margen 2025 distorsionado.
- Referencia genérica 999999 provoca costes medios irreales.
- Recalcular margen real excluyendo/corrigiendo referencias genéricas.

### ECOCLEAN

- Cuenta 758 con importes relevantes.
- Falta saber qué representa.
- No interpretar resultado como margen comercial puro hasta aclararlo.

### GRUPO

- Hay operaciones intragrupo.
- Hay alquiler nave ACI → CHEMIE.
- Hay saldos antiguos de clientes.
- Hay que separar negocio real, patrimonio, vinculadas y extraordinarios.

## Próximo paso pendiente

Generar Bloque 06 definitivo:

- productos
- artículos
- costes
- márgenes por referencia
- referencias genéricas
- artículos sin familia
- productos sin coste
- productos con margen negativo
## Archivos estructurados añadidos

Se han generado exports estructurados para uso documental, base local o agente:

- 07A_ventas_lineas_grupo_2024_2025_LIMPIO.psv
- 07B_clientes_pendientes_grupo_2025_LIMPIO.psv
- 07C_proveedores_pendientes_grupo_2025_LIMPIO.psv
- 07D_bancos_deuda_grupo_2024_2025_LIMPIO.psv
- 07E_diario_sensible_grupo_2024_2025_LIMPIO.psv
- 07G_articulos_maestro_grupo_LIMPIO.psv
- 07H_clientes_maestro_grupo_LIMPIO.psv
- 07I_proveedores_maestro_grupo_LIMPIO.psv
- 07J_familias_maestro_grupo_LIMPIO.psv
- 07K_validacion_ventas_vs_maestros_grupo_2024_2025.psv
- 07K_resumen_validacion_ventas_vs_maestros.psv
- 08A_registro_incidencias_prioritarias.psv
- 08B_resumen_incidencias_para_septiembre.md

## Estado actual

El paquete ya contiene:

1. Análisis general 2024-2025.
2. Incidencias detectadas.
3. Ventas por línea.
4. Clientes pendientes.
5. Proveedores pendientes.
6. Bancos, deuda e intereses.
7. Diario sensible.
8. Maestros de artículos, clientes, proveedores y familias.
9. Validación de ventas contra maestro.
10. Registro de incidencias para septiembre.

## Próximo trabajo pendiente

- Preparar preguntas ordenadas para reuniones internas.
- Crear roadmap de entrada de Jero.
- Crear base local en CSV/DuckDB/SQLite si se quiere explotación más avanzada.
- Añadir documentación externa: catálogo, tarifas, fichas técnicas, FDS, contratos, alquiler nave, cuadros bancarios.