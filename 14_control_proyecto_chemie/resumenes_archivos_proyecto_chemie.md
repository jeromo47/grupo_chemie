# Resúmenes de archivos del proyecto CHEMIE

## Regla
Cada resumen debe distinguir:
- **qué es**
- **qué contiene**
- **para qué sirve**
- **límites o riesgos**

---

## 01_validacion_total_grupo.txt
- **Qué es**: exporte fuente de validación global del paquete 2024-2025.
- **Qué contiene**: cifras generales comparadas por sociedad, especialmente ventas, compras y validaciones básicas del núcleo.
- **Para qué sirve**: fijar la jerarquía económica gruesa del núcleo y validar que Chemie es la tractora.
- **Límites**: no sustituye el detalle de cartera, deuda, vinculadas ni margen fino.

## 02_margen_clientes_proveedores_grupo.txt
- **Qué es**: exporte fuente de margen, clientes, proveedores y movimientos relacionados.
- **Qué contiene**: top de clientes/proveedores, señales de margen, y evidencia documental literal útil para operaciones como Ducati y alquiler ACI-Chemie.
- **Para qué sirve**: analizar concentración comercial, margen y vinculadas visibles por concepto.
- **Límites**: puede mezclar lectura comercial con extractos parciales no suficientes para control de gestión definitivo.

## 03_cobros_bancos_deuda_grupo.txt
- **Qué es**: exporte fuente de cobros, bancos y deuda.
- **Qué contiene**: saldos, movimientos, cuentas de deuda e intereses, y detalle suficiente para inferir desapalancamiento 2025.
- **Para qué sirve**: explicar la mejora financiera de Chemie y preparar futuras extracciones desde BD.
- **Límites**: no garantiza identificación perfecta de cada operación financiera sin cruce adicional con BD o listados manuales.

## 04_pyg_patrimonio_grupo.txt
- **Qué es**: exporte fuente de PYG, patrimonio y movimientos vinculados.
- **Qué contiene**: resultados aproximados, señales patrimoniales, y asientos ligados a operaciones especiales o vinculadas.
- **Para qué sirve**: separar negocio base, extraordinarios y operaciones patrimoniales.
- **Límites**: requiere cautela para no sobreinterpretar asientos aislados.

## 05_incidencias_grupo.txt
- **Estado**: pendiente de confirmación de ruta/ingesta efectiva en el sistema documental.
- **Uso previsto**: registrar anomalías, incidencias y posibles señales de revisión adicional.
- **Límite**: no consta en los archivos disponibles dentro de esta sesión si no se incorpora expresamente.

## 06_productos_costes_y_anomalias_grupo.txt
- **Estado**: pendiente de confirmación de ruta/ingesta efectiva en el sistema documental.
- **Uso previsto**: profundizar en mix de producto, costes y anomalías comerciales o de margen.
- **Límite**: no consta en los archivos disponibles dentro de esta sesión si no se incorpora expresamente.

## 00_schema_tablas_clave_grupo.txt
- **Estado**: pendiente de confirmación de ruta/ingesta efectiva.
- **Uso previsto**: mapa técnico de tablas clave para extracción Firebird.
- **Límite**: no consta en los archivos disponibles dentro de esta sesión si no se incorpora expresamente.


## Entrega estructurada CHEMIE_AGENT_INPUT (2026-05-27)
- **Qué es**: paquete de entrega estructurada con fuentes, exports PSV, control documental, índice técnico y base local DuckDB.
- **Qué contiene**: una capa mucho más madura que la del paquete inicial, incluyendo módulos 07A-10I, registro de incidencias, roadmap de entrada y base local cargada.
- **Para qué sirve**: conservación, indexación, explotación analítica local y continuidad del proyecto sin depender de una sola conversación.
- **Límites**: el manifiesto y el índice técnico incluyen interpretaciones operativas hechas fuera de este agente; deben conservarse como material fuente/derivado, no como hecho automáticamente revalidado aquí.

## 05_incidencias_grupo.txt
- **Estado actualizado**: fuente confirmada en entrega 2026-05-27.
- **Uso previsto**: bloque de incidencias del grupo para alimentar control, preguntas y revisión por hitos.
- **Límite**: pendiente de lectura analítica específica dentro del sistema actual.

## 06_productos_costes_y_anomalias_grupo.txt
- **Estado actualizado**: fuente confirmada en entrega 2026-05-27.
- **Uso previsto**: soporte de producto, coste, margen depurado y anomalías por referencia.
- **Límite**: debe distinguirse siempre entre negocio core y no core, referencias genéricas y operaciones especiales.

## 10J_INDICE_TECNICO_EXTRACCIONES.md
- **Qué es**: índice técnico maestro de la extracción Firebird/MasterSQL ya realizada.
- **Qué contiene**: catálogo razonado de bloques 07A-10I, usos, incidencias y recomendaciones de explotación local.
- **Para qué sirve**: guía maestra de qué archivo usar para cada frente de análisis o almacenamiento.
- **Límite**: es guía técnica derivada; no sustituye validación puntual cuando se tome una conclusión concreta.

## 09_ROADMAP_ENTRADA_JERO.md
- **Qué es**: roadmap operativo de entrada de Jero en el grupo CHEMIE.
- **Qué contiene**: fases, prioridades, foco por empresa, preguntas y secuencia temporal hasta 12 meses.
- **Para qué sirve**: organizar aprendizaje, validación y futura implantación de controles.
- **Límite**: documento de orientación estratégica, no hecho documental sobre la realidad económica por sí mismo.
