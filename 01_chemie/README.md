# Chemie, mapa documental operativo

Estado: borrador de trabajo, prudente.

## Qué parece razonablemente definido

- La carpeta fuente principal es `00_fuente_drive/DOCUMENTACION/DOCUMENTACION CHEMIE`.
- Hay un núcleo societario claro en `ESCRITURA PDF`.
- Según OCR previo de la escritura de constitución, la sociedad se constituyó como `GRUPO CHEMIE LA JUAIDA, S.L.` el 13-12-2002.
- Según ese mismo OCR, el capital inicial identificado es de 3.100 EUR, representado por 310 participaciones de 10 EUR.
- El OCR también apunta a administrador único inicial vinculado a Jerónimo Molina Cantón.
- Según OCR de la ampliación de 2016, existe aumento de capital, pérdida del carácter de unipersonalidad y entrada de nuevas participaciones al menos de la 311 a la 370. Esto sugiere una ampliación mínima de 600 EUR, pendiente de validación fina contra la escritura original.
- El domicilio social aparece asociado a Sierra Almijara, Polígono La Juaida, Viator (extraído de OCR de 2016, conviene confirmar redacción exacta).
- El objeto aparente mezcla comercio mayorista de droguería, pinturas, maquinaria, repuestos y artículos industriales.

## Bloques con más valor documental

1. `ESCRITURA PDF`
2. `LICENCIA APERTURA GCH`
3. `REGISTRO BIOCIDAS`
4. `REGISTRO SANITARIO`
5. `REGISTRO ECOLOGICO CAEE`
6. `SANIDAD`
7. `PRESTAMOS-RENTING`
8. `CONTRATO TELEFONIA`, `CONTRATO ELECTRICIDAD 2022`, `KIT DIGITAL`

## Clasificación operativa recomendada

### aprovechable
- Escrituras, poderes, CIF, modelo 036, alta ROI, CNAE.
- Licencia de apertura, protección contra incendios, revisión eléctrica.
- Registros de sanidad, biocidas, ecológico CAAE, INTCF.
- Prevención, protección de datos, kit digital, suministros.
- Préstamos y renting ligados a activos o estructura financiera.

### sospechoso
- Duplicados, ficheros con nombres genéricos, `debug.log`, materiales de marca repetidos, `Thumbs.db`.
- OCR con baja fiabilidad donde el texto sale roto.

### regenerar_desde_bd
- No prioritario aquí. En Chemie, esta etiqueta aplica mejor a facturación masiva fuera de esta carpeta principal.

### otro
- Branding, logotipos, cabeceras, documentación de vehículos periféricos si no alimenta decisiones actuales.

## Subbloques revisados con observaciones útiles

### Escrituras
- `ESCRITURA CONSTIT G CHEMIE.pdf`, `ESCRITURA AMPLIACION CAPITAL 10-11-16.pdf`, `ACTA VINCULACION JURIDICA GCH.pdf`, `PODER MERCANTIL CHEMIE.pdf`.
- Ya existe OCR previo en `13_conocimiento_generado/pipeline_extraccion_documental/textos/`.
- Recomendación: usar estos OCR como base de resumen, pero no dar por cerrada ninguna cifra o literal sin validación final de pasajes concretos.

### Licencia apertura
- Aparecen licencia, revisión eléctrica, relación para proyecto, planos y certificados contra incendios.
- Útil para reconstruir obligaciones de nave, instalaciones y requisitos de actividad.

### Registro biocidas
- Hay memoria, plano, ampliación de expediente y normativa de referencia.
- Esto sugiere un expediente operativo y no solo informativo.

### Registro sanitario y sanidad
- Hay material sobre cancelación, AESAN, normativa, auditoría 2016 y envío de FDS.
- Puede servir para separar: registro sanitario histórico, revisión regulatoria y cumplimiento documental con clientes.

### Registro ecológico CAAE
- OXISAN aparece como eje principal.
- Hay trazabilidad, albaranes, FDS, certificaciones por renovación y normativa UE.
- Bloque muy valioso para una ficha de producto/ecológico con evidencia documental.

### Préstamos y renting
- Poca cantidad de archivos, pero alta relación señal/ruido.
- Parece útil para una ficha de pasivos y activos asociados, mejor que tratarlo solo como archivo suelto.

## Pendiente prudente

- Confirmar capital social vigente tras la ampliación de 2016.
- Confirmar redacción exacta del objeto social y domicilio social.
- Separar vehículos claramente corporativos de vehículos posiblemente personales o mixtos.
- Ver si la cancelación de registro sanitario fue total, parcial o solo comunicada.
- Extraer una cronología compacta de hitos regulatorios.
