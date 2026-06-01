# Auditoría del sistema documental

## Objetivo
Tener una capa de control de calidad sobre el trabajo de ingesta, clasificación y generación de conocimiento del proyecto `grupo_familiar`.

## Escala de calidad
- **SÓLIDO**: sustentado en documentos revisados o evidencia fuerte, con baja ambigüedad.
- **ACEPTABLE**: útil y razonablemente fiable, aunque no completamente validado documento a documento.
- **PROVISIONAL**: útil para avanzar, pero apoyado en heurísticas o revisión parcial.
- **DUDOSO**: contiene ambigüedad relevante o evidencia insuficiente.
- **NO FIABLE**: no debe usarse como base de decisión sin rehacer o validar.
- **PENDIENTE DE VALIDACIÓN**: existe, pero aún no ha pasado control suficiente.

## Tipos de soporte admitidos
- **Documento leído**
- **Dato confirmado por documento**
- **Dato confirmado por Jero**
- **Dato inferido**
- **Dato conflictivo**

## Módulos auditados
Ver `auditoria_modulos.csv` para visión tabular.

## Criterios de auditoría
1. Cobertura real frente al universo documental.
2. Calidad de extracción y trazabilidad.
3. Separación entre hechos, inferencias y dudas.
4. Riesgo de error acumulado.
5. Utilidad operativa actual.

## Observaciones generales iniciales
- La base del sistema está bien planteada: fuente bruta separada, conocimiento generado separado y ficheros vivos de proyecto.
- La parte patrimonial tiene una base útil, pero mezcla distintos niveles de certeza, por lo que debe mantenerse como trabajo estructural preliminar, no como verdad cerrada.
- La parte empresa/documentación Chemie está en mejor posición para consolidarse con rigor porque ya existe un bloque formal claro y ya está operativo el pipeline de extracción PDF con OCR.
- Las áreas financieras/exportadas desde sistemas externos deben seguir tratándose como material potencialmente no fiable hasta validación adicional o regeneración desde fuente adecuada.


## Regla operativa de activación de auditorías

### Cómo pedir una auditoría
Jero puede activarla con lenguaje natural. Frases válidas típicas:
- "lanza auditoría"
- "haz una auditoría de lo que llevamos"
- "audita Chemie"
- "auditoría global"
- "pásale control de calidad"

No hace falta usar una fórmula exacta.

### Activación proactiva por parte de Minion
Minion debe proponer o ejecutar una auditoría cuando detecte alguno de estos casos:
1. cierre de un bloque importante de trabajo
2. acumulación de material provisional o inferido
3. antes de usar un bloque como base para decisiones
4. antes de cambiar de línea principal de investigación
5. al acercarse hitos relevantes del proyecto

### Política recomendada
- Auditoría por hitos, no por calendario rígido.
- Jero puede pedirla en cualquier momento.
- Minion debe sugerirla cuando vea riesgo de error acumulado o necesidad de consolidación.
