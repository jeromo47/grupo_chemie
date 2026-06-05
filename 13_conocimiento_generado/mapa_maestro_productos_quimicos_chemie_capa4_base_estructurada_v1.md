# Mapa maestro de productos químicos Chemie - capa 4 base estructurada v1

## Objetivo
Transformar el trabajo previo en una base estructurada, casi tabular, que sirva como cimiento para:
- aprendizaje personal del catálogo
- futura base de datos documental
- ampliación producto por producto
- y consultas operativas más rápidas

Esta capa ya no está pensada solo para leer en prosa.
Está pensada para **normalizar criterios**.

---

## Esquema de campos
Cada producto queda resumido con estos campos:

- `producto`
- `familia_funcional`
- `subfamilia`
- `intervencion_principal`
- `contacto_genero`
- `tipo_contacto`
- `logica_residuo`
- `logica_funcional`
- `industria_alimentaria`
- `contacto_alimentario_tecnico`
- `eco_si_consta`
- `soporte_documental`
- `documento_mejor`
- `dosificacion_consta`
- `estado_confianza`
- `dudas_clave`

---

## Base estructurada v1

### OXISAN
- `producto`: OXISAN
- `familia_funcional`: oxidante / higienizante industrial
- `subfamilia`: línea oxidante ácida de proceso
- `intervencion_principal`: agua de proceso / agua de lavado
- `contacto_genero`: indirecta probable
- `tipo_contacto`: indirecto / auxiliar sensible
- `logica_residuo`: no consta con cierre fino; posible relevancia alta de control de residuo/proceso
- `logica_funcional`: tratamiento de proceso + higienización oxidante
- `industria_alimentaria`: sí
- `contacto_alimentario_tecnico`: probable sí, por contexto de proceso
- `eco_si_consta`: sí, conexión fuerte con eje CAAE/ecológico en el proyecto
- `soporte_documental`: alto
- `documento_mejor`: FDS real propia de Chemie
- `dosificacion_consta`: no
- `estado_confianza`: alto
- `dudas_clave`: cierre exacto del marco operativo; formulación/comercialización actual

### CHEMGRAS DS
- `producto`: CHEMGRAS DS
- `familia_funcional`: desengrasante / limpiador industrial
- `subfamilia`: desengrase técnico de superficies
- `intervencion_principal`: superficie / equipo
- `contacto_genero`: solo entorno/equipo
- `tipo_contacto`: directo
- `logica_residuo`: probable aclarado o control de uso, no cerrado aquí
- `logica_funcional`: limpieza + desengrase
- `industria_alimentaria`: no consta expresamente como eje principal en lo resumido
- `contacto_alimentario_tecnico`: no consta
- `eco_si_consta`: no
- `soporte_documental`: alto
- `documento_mejor`: FDS real propia
- `dosificacion_consta`: no
- `estado_confianza`: alto
- `dudas_clave`: sectores/clientes concretos; vigencia formulación actual

### HIDROBRILL
- `producto`: HIDROBRILL
- `familia_funcional`: auxiliar de lavado / secante-abrillantador
- `subfamilia`: postlavado hortofrutícola
- `intervencion_principal`: producto alimentario / fase final de lavado
- `contacto_genero`: directa probable o muy próxima al género tratado
- `tipo_contacto`: directo probable / de acabado
- `logica_residuo`: punto crítico; no consta cierre fino, pero la lógica de acabado lo vuelve muy sensible
- `logica_funcional`: acabado + secado + abrillantado
- `industria_alimentaria`: sí
- `contacto_alimentario_tecnico`: sí probable
- `eco_si_consta`: no
- `soporte_documental`: medio-bajo
- `documento_mejor`: ficha técnica / hoja comercial CLP
- `dosificacion_consta`: no
- `estado_confianza`: medio
- `dudas_clave`: FDS completa; encaje exacto como auxiliar tecnológico

### V-80
- `producto`: V-80
- `familia_funcional`: aceite blanco medicinal / auxiliar técnico alimentario
- `subfamilia`: lubricante técnico apto para contacto alimentario
- `intervencion_principal`: proceso auxiliar / maquinaria / contacto técnico
- `contacto_genero`: auxiliar técnico sin contacto directo principal
- `tipo_contacto`: auxiliar
- `logica_residuo`: no aplica como limpiador; prima compatibilidad técnica/contacto alimentario
- `logica_funcional`: lubricación + auxiliar técnico + protección
- `industria_alimentaria`: sí
- `contacto_alimentario_tecnico`: sí
- `eco_si_consta`: no
- `soporte_documental`: medio-alto
- `documento_mejor`: ficha técnica fuerte / especificación técnica
- `dosificacion_consta`: no
- `estado_confianza`: medio-alto
- `dudas_clave`: FDS completa; relación exacta con IBERFARM L; peso comercial real

### ACTIV CLOR
- `producto`: ACTIV CLOR
- `familia_funcional`: blanqueante clorado / limpiador clorado
- `subfamilia`: hipoclorito para limpieza y blanqueo profesional
- `intervencion_principal`: superficie / equipo
- `contacto_genero`: solo entorno/equipo
- `tipo_contacto`: directo
- `logica_residuo`: probable aclarado o manejo controlado; no detallado aquí
- `logica_funcional`: limpieza + blanqueo + cloración
- `industria_alimentaria`: no consta aquí como eje principal, aunque puede entrar en entornos técnicos
- `contacto_alimentario_tecnico`: no consta
- `eco_si_consta`: no
- `soporte_documental`: alto
- `documento_mejor`: FDS completa
- `dosificacion_consta`: no
- `estado_confianza`: alto
- `dudas_clave`: usos sectoriales concretos; posición frente a otras líneas cloradas

### ALICLOR COMPLET
- `producto`: ALICLOR COMPLET
- `familia_funcional`: limpiador-desinfectante clorado alcalino
- `subfamilia`: detergente bactericida/fungicida clorado profesional
- `intervencion_principal`: superficie / equipo / utensilio
- `contacto_genero`: solo entorno/superficie/equipo
- `tipo_contacto`: directo
- `logica_residuo`: probable manejo controlado con lógica de limpieza-desinfección; no forzar detalle fino aquí
- `logica_funcional`: limpieza + desinfección + desengrase
- `industria_alimentaria`: sí
- `contacto_alimentario_tecnico`: no directo; sí de entorno alimentario
- `eco_si_consta`: no
- `soporte_documental`: alto
- `documento_mejor`: FDS completa + soporte registral/técnico
- `dosificacion_consta`: no
- `estado_confianza`: alto
- `dudas_clave`: vigencia exacta del registro; coincidencia con formulación viva actual

### TUNELIMP
- `producto`: TUNELIMP
- `familia_funcional`: detergente alcalino técnico de lavado industrial
- `subfamilia`: limpiador cáustico de proceso / túnel de lavado
- `intervencion_principal`: superficie / equipo / línea de lavado
- `contacto_genero`: solo entorno/línea/equipo
- `tipo_contacto`: directo
- `logica_residuo`: presupone proceso técnico controlado y probable aclarado
- `logica_funcional`: limpieza + lavado técnico cáustico
- `industria_alimentaria`: probable sí por contexto, aunque aquí pesa más la lógica de línea/equipo
- `contacto_alimentario_tecnico`: sí de entorno de proceso
- `eco_si_consta`: no
- `soporte_documental`: alto
- `documento_mejor`: FDS completa + hoja previa de apoyo
- `dosificacion_consta`: no
- `estado_confianza`: alto
- `dudas_clave`: si TUNELIMP CL es variante distinta; posición comercial actual

### DERGEL SO
- `producto`: DERGEL SO
- `familia_funcional`: higiene de manos profesional sin residuo
- `subfamilia`: jabón líquido para industria alimentaria
- `intervencion_principal`: mano
- `contacto_genero`: no contacto principal con género
- `tipo_contacto`: directo
- `logica_residuo`: sin residuo / no residuo según lógica declarada
- `logica_funcional`: higiene de manos + lavado
- `industria_alimentaria`: sí
- `contacto_alimentario_tecnico`: no; es higiene personal en entorno alimentario
- `eco_si_consta`: no
- `soporte_documental`: medio
- `documento_mejor`: ficha técnica / hoja CLP
- `dosificacion_consta`: no
- `estado_confianza`: medio
- `dudas_clave`: FDS completa; peso comercial; relación con LICOGEL y otras referencias de manos

### BRINET BQ
- `producto`: BRINET BQ
- `familia_funcional`: limpiador general de superficies / fregasuelos
- `subfamilia`: limpieza de mantenimiento base bioalcohol
- `intervencion_principal`: superficie / suelo / pared
- `contacto_genero`: solo entorno/superficie
- `tipo_contacto`: directo
- `logica_residuo`: no consta con limpieza suficiente
- `logica_funcional`: limpieza + mantenimiento
- `industria_alimentaria`: sí, pero de forma secundaria o no nuclear en lo revisado
- `contacto_alimentario_tecnico`: no consta
- `eco_si_consta`: no
- `soporte_documental`: medio-bajo
- `documento_mejor`: ficha técnica / hoja comercial CLP
- `dosificacion_consta`: no
- `estado_confianza`: medio-bajo
- `dudas_clave`: FDS completa; significado práctico de uso en industria alimentaria; peso comercial real

### BRINET AML
- `producto`: BRINET AML
- `familia_funcional`: limpiador general amoniacal
- `subfamilia`: limpieza y desodorización de mantenimiento
- `intervencion_principal`: superficie / suelo
- `contacto_genero`: solo entorno/superficie
- `tipo_contacto`: directo
- `logica_residuo`: no consta con limpieza suficiente
- `logica_funcional`: limpieza + desodorización + mantenimiento
- `industria_alimentaria`: no como eje claro
- `contacto_alimentario_tecnico`: no consta
- `eco_si_consta`: no
- `soporte_documental`: medio-bajo
- `documento_mejor`: ficha técnica / hoja comercial CLP
- `dosificacion_consta`: no
- `estado_confianza`: medio-bajo
- `dudas_clave`: FDS completa; peso comercial; vigencia actual

### NETIND
- `producto`: NETIND
- `familia_funcional`: limpiador-disolvente profesional
- `subfamilia`: limpieza técnica por disolvente
- `intervencion_principal`: superficie / pieza / zona técnica
- `contacto_genero`: solo entorno/pieza/superficie técnica
- `tipo_contacto`: directo
- `logica_residuo`: no consta aquí; lógica más de disolución/evaporación técnica que de enjuague alimentario
- `logica_funcional`: limpieza técnica + disolución
- `industria_alimentaria`: no consta como eje principal
- `contacto_alimentario_tecnico`: no consta
- `eco_si_consta`: no
- `soporte_documental`: alto
- `documento_mejor`: FDS completa
- `dosificacion_consta`: no
- `estado_confianza`: alto
- `dudas_clave`: usos sectoriales concretos; peso real de esta familia en catálogo activo

### TR-20
- `producto`: TR-20
- `familia_funcional`: auxiliar técnico para aguas de lavado / postcosecha
- `subfamilia`: aditivo funcional de proceso hortofrutícola
- `intervencion_principal`: agua de lavado / proceso hortofrutícola
- `contacto_genero`: indirecta probable con posible efecto funcional sobre género tratado
- `tipo_contacto`: indirecto / auxiliar de proceso
- `logica_residuo`: punto crítico; muy relevante para entender bien el proceso
- `logica_funcional`: tratamiento de agua/proceso + mejora de lavado + mejora de acabado
- `industria_alimentaria`: sí
- `contacto_alimentario_tecnico`: sí probable
- `eco_si_consta`: no consta expresamente
- `soporte_documental`: medio
- `documento_mejor`: ficha técnica fuerte con anexo explicativo
- `dosificacion_consta`: no
- `estado_confianza`: medio-alto
- `dudas_clave`: FDS completa; encaje regulatorio exacto; peso comercial frente a OXISAN e HIDROBRILL

### CHEMGRAS BAC
- `producto`: CHEMGRAS BAC
- `familia_funcional`: detergente desengrasante higienizante
- `subfamilia`: higienizante no clorado con amonios cuaternarios
- `intervencion_principal`: superficie / equipo
- `contacto_genero`: solo entorno/superficie/equipo
- `tipo_contacto`: directo
- `logica_residuo`: probable manejo con aclarado/control
- `logica_funcional`: limpieza + desengrase + higienización no clorada
- `industria_alimentaria`: probable según uso, no cerrada aquí
- `contacto_alimentario_tecnico`: no directo; sí posible en entorno técnico
- `eco_si_consta`: no
- `soporte_documental`: alto
- `documento_mejor`: FDS completa
- `dosificacion_consta`: no
- `estado_confianza`: alto
- `dudas_clave`: peso comercial real; usos concretos; vigencia actual

### IBERFARM L
- `producto`: IBERFARM L
- `familia_funcional`: aceite blanco técnico de alta pureza / lubricante alimentario
- `subfamilia`: lubricante, antiadherente, desmoldante y abrillantador atóxico
- `intervencion_principal`: proceso auxiliar / maquinaria / contacto técnico alimentario
- `contacto_genero`: auxiliar técnico sin contacto directo principal
- `tipo_contacto`: auxiliar
- `logica_residuo`: prima compatibilidad técnica y pureza, no lógica clásica de enjuague
- `logica_funcional`: lubricación + antiadherencia + desmoldeo + abrillantado técnico
- `industria_alimentaria`: sí
- `contacto_alimentario_tecnico`: sí
- `eco_si_consta`: no
- `soporte_documental`: medio-alto
- `documento_mejor`: ficha técnica fuerte / especificación técnica
- `dosificacion_consta`: no
- `estado_confianza`: medio-alto
- `dudas_clave`: FDS completa; relación exacta con V-80; peso real en ventas

### LICOGEL
- `producto`: LICOGEL
- `familia_funcional`: gel sanitizante hidroalcohólico
- `subfamilia`: sanitización directa de manos/superficies de uso rápido
- `intervencion_principal`: mano / superficie / utensilio
- `contacto_genero`: solo indirecta respecto al género; directa sobre mano/superficie
- `tipo_contacto`: directo
- `logica_residuo`: consta lógica de uso directo sin aclarado sobre superficies
- `logica_funcional`: sanitización + higiene rápida
- `industria_alimentaria`: sí
- `contacto_alimentario_tecnico`: no directo; sí en entorno alimentario
- `eco_si_consta`: no
- `soporte_documental`: medio
- `documento_mejor`: ficha técnica fuerte
- `dosificacion_consta`: parcialmente sí
- `estado_confianza`: medio
- `dudas_clave`: FDS completa; clasificación CLP completa; soporte adicional de usos sobre superficies

### TUNELIMP CL
- `producto`: TUNELIMP CL
- `familia_funcional`: detergente clorado técnico para túneles de lavado
- `subfamilia`: variante clorada e higienizante de proceso alimentario
- `intervencion_principal`: línea de túnel / cajas / material alimentario
- `contacto_genero`: solo entorno/línea/material
- `tipo_contacto`: directo
- `logica_residuo`: probable proceso con aclarado y control técnico
- `logica_funcional`: limpieza + higienización + cloración técnica de túnel
- `industria_alimentaria`: sí
- `contacto_alimentario_tecnico`: sí de entorno/proceso
- `eco_si_consta`: no
- `soporte_documental`: medio
- `documento_mejor`: ficha técnica / hoja CLP fuerte
- `dosificacion_consta`: no
- `estado_confianza`: medio-alto
- `dudas_clave`: FDS completa específica; relación exacta con TUNELIMP; peso real en ventas

---

## Cómo usar esta base

### 1. Para aprender el catálogo
La forma buena de leerla no es solo por nombre, sino preguntando:
- ¿sobre qué actúa?
- ¿deja o no deja residuo?
- ¿es limpieza, proceso, acabado, sanitización o lubricación?
- ¿toca el género o solo el entorno?

### 2. Para construir una futura base de datos real
Esta pieza ya se puede convertir casi directamente en:
- CSV
- Airtable/Notion
- SQLite/DuckDB
- o tabla Markdown más compacta

### 3. Para futuras preguntas a tu tío o revisión documental
Los mejores huecos a cerrar suelen ser:
- `dosificacion_consta`
- `dudas_clave`
- `contacto_genero`
- `eco_si_consta`
- `logica_residuo`

---

## Conclusión ejecutiva
Esta capa 4 ya sirve bastante bien como **base estructurada de aprendizaje**.

La idea central sería esta:

> **La base buena no consiste en memorizar nombres de productos, sino en saber dónde intervienen, qué lógica funcional tienen, qué sensibilidad documental/regulatoria arrastran y si afectan al entorno, al agua, a la mano, al género o al proceso técnico.**

---

## Siguiente paso recomendado
A partir de aquí, veo dos opciones muy buenas:

### Opción A
Convertir esta capa 4 en una **tabla compacta de control** todavía más manejable.

### Opción B
Abrir una **capa 5** con preguntas de negocio y aprendizaje por producto, por ejemplo:
- qué riesgo de error conceptual tiene cada uno
- con qué otros se puede confundir
- cuándo se elegiría uno frente a otro
- qué pregunta exacta conviene hacer para cerrar sus dudas

### Mi recomendación real
Yo haría primero la **opción A**.
Porque te dejaría una base muy limpia para consultar y ampliar sin perderte en tanto texto.
