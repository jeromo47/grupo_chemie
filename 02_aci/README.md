# ACI, mapa documental operativo

Estado: borrador prudente.

## Qué parece razonablemente definido

- La base fuente es `00_fuente_drive/DOCUMENTACION/DOCUMENTACION ALMERIENSE`.
- El núcleo societario está en `ESCRITURAS`.
- Hay una combinación de sociedad + inmuebles + explotación de activos, especialmente Mojácar y nave Sierra Almijara.
- También aparecen cumplimiento básico, kit digital, notas simples y prevención.

## Bloques principales detectados

1. `ESCRITURAS`
2. `NAVE SIERRA ALMIJARA`
3. `CASA MOJACAR`
4. `NOTAS SIMPLES ACI`
5. `PREVENCION RIESGO LABORALES ACI`
6. `KIT DIGITAL`
7. `CASA BOBAR 4`

## Lectura operativa

### Núcleo empresa
- Escritura de constitución.
- Poder mercantil.
- Modelos 036, CIF, IAE, alta ROI/intracomunitario.
- Prevención y protección de datos.

### Núcleo patrimonial
- `CASA MOJACAR`, con alquiler, comunidad, electricidad, internet, registro turístico, tasación y expediente fiscal/tributario 174-2013.
- `NAVE SIERRA ALMIJARA`, con compra, agua, alarma, planos y comunidad del polígono.
- `CASA BOBAR 4`, con venta/cancelación hipotecaria y soporte catastral/registral.

### Núcleo accesorio
- Vehículos y alguna documentación suelta de transferencias o ventas.

## Clasificación operativa recomendada

### aprovechable
- Escrituras y poderes.
- CIF, IAE, intracomunitario, modelos 036.
- Notas simples por finca.
- Nave Sierra Almijara.
- Casa Mojácar, especialmente explotación, registro oficial, contratos y expediente 174-2013.
- Prevención, kit digital y protección de datos.

### sospechoso
- Duplicados de PDF, `debug.log`, `Thumbs.db`, material de cabecera/imagen sin uso jurídico.
- OCR no verificado si se genera después.

### regenerar_desde_bd
- Nóminas o facturación seriada si la base contable ya existe en otro sistema.

### otro
- Material visual, documentación de vehículo no conectada con una decisión de empresa o patrimonio.

## Observaciones útiles por bloque

### Escrituras
- Hay escritura de constitución por hojas, elevaciones a público 2000 y 2006, poder mercantil y acta de identificación de titularidad.
- Muy buena base para ficha formal de entidad y cronología societaria.

### Casa Mojácar
- Es uno de los bloques más densos y de mayor valor.
- Mezcla operación turística, comunidad, suministros, expediente fiscal y gastos/ingresos.
- Conviene tratarla como activo patrimonial con subfichas: título, explotación, suministros, comunidad, contingencias.

### Expediente 174-2013
- Hay alegaciones, recursos, resoluciones, pago y soporte de compra/préstamo.
- Merece una cronología aparte, sin interpretar el resultado final más allá de lo explícito en documentos.

### Nave Sierra Almijara
- Bloque compacto para ficha del activo: compraventa, suministros, alarma, planos, comunidad.

### Notas simples ACI
- Apuntan a varias fincas concretas: Mojácar, nave Viator, trastero, garaje y piso Bobar.
- Muy útiles para cruzar activos con mapas patrimoniales existentes.

## Pendiente prudente

- Extraer datos formales limpios de la escritura de constitución.
- Cruzar fincas de notas simples con mapa patrimonial ya generado.
- Separar ACI empresa frente a patrimonio inmobiliario de ACI.
- Redactar ficha de Mojácar y ficha de Sierra Almijara con estado, riesgos y documentos clave.
