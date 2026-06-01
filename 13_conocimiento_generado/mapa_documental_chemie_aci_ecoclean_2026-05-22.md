# Mapa documental consolidado, Chemie + ACI + Ecoclean

Fecha de trabajo: 2026-05-22
Criterio: prudente, sin afirmar como hecho lo no verificado en documento legible.

## Resumen ejecutivo

He priorizado Chemie y he dejado una base utilizable también para ACI y Ecoclean.
No se ha borrado material fuente.
Se han creado mapas operativos en:

- `01_chemie/README.md`
- `02_aci/README.md`
- `03_ecoclean/README.md`

Además se generó inventario transversal:
- `13_conocimiento_generado/inventario_entidades_chemie_aci_ecoclean.csv`

## Clasificación global

### aprovechable
- Carpetas societarias, registrales, regulatorias y de activos claros.
- Chemie: escrituras, licencia, biocidas, sanitario, CAAE, sanidad, INTCF, préstamos-renting.
- ACI: escrituras, nave Sierra Almijara, Mojácar, notas simples, prevención, kit digital.
- Ecoclean: constitución, cambios de comuneros, arrendamientos, locales, seguros.

### sospechoso
- `CHEMIE\ACI_Análisis conjunto ` ya estaba marcado como sospechoso en clasificación previa.
- Duplicados, `debug.log`, `Thumbs.db`, material visual repetido, OCR roto.

### regenerar_desde_bd
- Facturación masiva y series administrativas repetitivas, especialmente fuera de estas tres carpetas foco.
- No he re-trabajado esa capa, porque el valor marginal esta noche era bajo frente a estructura y mapa documental.

### otro
- Branding, logos, material accesorio y vehículos periféricos sin decisión actual asociada.

## Chemie, definido

### Hechos con apoyo razonable
- Existe escritura de constitución OCRizada de `GRUPO CHEMIE LA JUAIDA, S.L.` fechada el 13-12-2002.
- El OCR previo refleja capital inicial de 3.100 EUR y 310 participaciones de 10 EUR.
- El OCR previo refleja administrador único inicial asociado a Jerónimo Molina Cantón.
- Hay escritura de 2016 de aumento de capital, cese de unipersonalidad y modificación estatutaria.
- El OCR de 2016 sugiere nuevas participaciones 311 a 370, lo que apunta al menos a una ampliación de 600 EUR. Esto queda marcado como pendiente de validación fina.
- El núcleo regulatorio y de actividad está muy bien representado por licencia, biocidas, sanitario, CAAE y sanidad.

### Bloques más útiles detectados
- `ESCRITURA PDF`
- `LICENCIA APERTURA GCH`
- `REGISTRO BIOCIDAS`
- `REGISTRO SANITARIO`
- `REGISTRO ECOLOGICO CAEE`
- `SANIDAD`
- `PRESTAMOS-RENTING`

### Decisión tomada
- Tratar Chemie primero como entidad societaria y regulada, no como carpeta mixta de vehículos/logos.
- Dejar separado lo central de lo periférico.

## ACI, definido

- El corazón documental está en `DOCUMENTACION ALMERIENSE`.
- Hay un doble eje claro: entidad mercantil + patrimonio/inmuebles.
- Los bloques con más retorno documental son escrituras, nave Sierra Almijara, Casa Mojácar y notas simples.
- Mojácar merece tratamiento como activo con explotación, comunidad, suministros y expediente fiscal propio.
- Sierra Almijara merece ficha separada por tratarse de nave con compra, suministros y planos.

### Decisión tomada
- No mezclar ACI solo como empresa operativa. La documentación pide modelo mixto empresa + patrimonio.

## Ecoclean, definido

- La documentación está más acotada y es manejable.
- El valor principal está en constitución/comuneros y en la secuencia de locales y arrendamientos.
- Aparecen tres focos operativos: Parador, Viator y Almería.
- Hay base suficiente para una futura cronología de ubicaciones.

### Decisión tomada
- No bajar a detalle factura a factura de alquiler ahora.
- Priorizar estructura de comuneros, locales y contratos.

## Qué queda pendiente

### Chemie
- Validar capital social vigente tras ampliación 2016.
- Confirmar literal de objeto social y domicilio social.
- Determinar si el registro sanitario quedó cancelado total, parcial o solo comunicado.
- Construir cronología regulatoria compacta.

### ACI
- Extraer datos limpios de escritura y poder mercantil.
- Cruzar notas simples con mapa patrimonial existente.
- Redactar ficha de Mojácar y ficha de Sierra Almijara.
- Separar mejor patrimonio vs operación.

### Ecoclean
- Confirmar comuneros por periodo.
- Determinar secuencia temporal de locales y contratos vigentes o últimos conocidos.
- Revisar si Viator sustituyó a Parador o coexistieron.

## Próximos pasos recomendados

1. Chemie: ficha formal societaria + cronología regulatoria.
2. Chemie: ficha OXISAN/CAAE y ficha sanitario-biocidas.
3. ACI: ficha de activo `Casa Mojácar`.
4. ACI: ficha de activo `Nave Sierra Almijara`.
5. Ecoclean: ficha de comuneros y ubicaciones.
6. Solo después, bajar a materiales secundarios o series repetitivas.

## Archivos creados o actualizados en esta pasada

- `01_chemie/README.md`
- `02_aci/README.md`
- `03_ecoclean/README.md`
- `13_conocimiento_generado/inventario_entidades_chemie_aci_ecoclean.csv`
- `13_conocimiento_generado/mapa_documental_chemie_aci_ecoclean_2026-05-22.md`
