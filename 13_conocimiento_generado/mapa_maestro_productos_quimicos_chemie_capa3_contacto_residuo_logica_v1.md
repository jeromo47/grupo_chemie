# Mapa maestro de productos químicos Chemie - capa 3 contacto, residuo y lógica funcional v1

## Objetivo
Construir una tercera capa de aprendizaje sobre el catálogo químico de Chemie para distinguir, con más cabeza de negocio y proceso:
- si el producto toca o no **género alimentario**
- si su lógica normal es de **residuo tolerado, no residuo o necesidad de aclarado/enjuague**
- qué papel funcional cumple realmente:
  - limpieza
  - higienización
  - tratamiento
  - acabado
  - lubricación
  - sanitización
- y qué señales documentales importantes constan sobre:
  - **uso profesional**
  - **industria alimentaria**
  - **contacto alimentario**
  - **eco / CAAE**

Esta capa no pretende dar una conclusión legal definitiva producto por producto.
Pretende construir una **gramática útil de aprendizaje** para no mezclar referencias que, aunque estén en el mismo catálogo, pertenecen a lógicas muy distintas.

---

## Regla clave de prudencia
Hay cuatro cosas que conviene no confundir:

1. **producto que toca el género directamente**
2. **producto que entra en el agua o circuito que afecta al género**
3. **producto que solo actúa sobre superficies/equipos**
4. **producto auxiliar de maquinaria o proceso sin función limpiadora directa sobre género**

Además, “uso en industria alimentaria” no significa automáticamente:
- contacto directo con alimento
- ausencia de residuo
- compatibilidad eco
- ni mismo marco regulatorio que otro producto alimentario

---

## Criterios de esta capa

### 1. Relación con género alimentario
- **directa probable**
- **indirecta probable**
- **solo entorno / superficie / equipo**
- **auxiliar técnico sin contacto directo principal**

### 2. Lógica de residuo o enjuague
- **sin residuo / no residuo**
- **requiere o presupone aclarado / enjuague**
- **residuo o contacto controlado de proceso**
- **no consta con limpieza suficiente**

### 3. Lógica funcional dominante
- **limpieza**
- **desengrase**
- **higienización / desinfección / sanitización**
- **tratamiento de agua o proceso**
- **acabado / abrillantado / secado**
- **lubricación / contacto técnico**

### 4. Señales documentales clave
- uso profesional
- industria alimentaria
- contacto alimentario / procesado / envasado
- eco / CAAE

---

## Aplicación al bloque principal

### OXISAN
- **Relación con género alimentario**: **indirecta probable**, a través de agua/circuito de proceso; no conviene afirmar aquí contacto directo simple como si fuera un producto de aplicación plana sobre género
- **Lógica de residuo o enjuague**: **no consta con cierre fino**, pero precisamente parece producto donde el control de residuo/proceso importa mucho
- **Lógica funcional dominante**:
  - tratamiento de proceso
  - higienización oxidante
  - posible tratamiento de aguas de lavado
- **Señales documentales clave**:
  - uso industrial
  - conexión fuerte previa del proyecto con eje **CAAE / ecológico**
  - relevancia alta en entorno alimentario/postcosecha
- **Lectura pedagógica**:
  - OXISAN es una referencia clave para aprender que un producto puede ser central en proceso alimentario sin encajar como simple detergente ni como biocida clásico

### CHEMGRAS DS
- **Relación con género alimentario**: **solo entorno / superficie / equipo**
- **Lógica de residuo o enjuague**: **probable necesidad de aclarado o control de uso**, aunque no consta aquí formulado así con detalle operativo
- **Lógica funcional dominante**:
  - limpieza
  - desengrase
- **Señales documentales clave**:
  - uso industrial
  - FDS fuerte
  - no consta señal eco
- **Lectura pedagógica**:
  - buen ejemplo de química técnica de limpieza que no debe mezclarse con proceso alimentario directo

### HIDROBRILL
- **Relación con género alimentario**: **directa probable o muy próxima al género tratado**, por su posición de secado/abrillantado final de verduras y hortalizas
- **Lógica de residuo o enjuague**: **muy sensible**, porque justo su función hace pensar en contacto o fase final; no debe cerrarse sin mejor soporte, pero es un punto crítico
- **Lógica funcional dominante**:
  - acabado
  - secado
  - abrillantado
- **Señales documentales clave**:
  - contexto hortofrutícola
  - uso en enjuague final
  - soporte documental parcial
- **Lectura pedagógica**:
  - producto muy importante para entender que “alimentario” no es solo limpiar o desinfectar; también hay auxiliares de acabado de proceso

### V-80
- **Relación con género alimentario**: **auxiliar técnico sin contacto directo principal**, aunque pensado para contextos donde puede haber contacto alimentario técnico compatible
- **Lógica de residuo o enjuague**: **no aplica igual que en limpiadores**; la clave aquí es compatibilidad técnica/contacto alimentario, no aclarado
- **Lógica funcional dominante**:
  - lubricación
  - auxiliar técnico
  - protección/proceso
- **Señales documentales clave**:
  - procesamiento y envasado de alimentos
  - FDA
  - NSF H-1
  - CE 1935/2004
- **Lectura pedagógica**:
  - obliga a distinguir muy bien entre “producto alimentario”, “producto para industria alimentaria” y “auxiliar técnico apto para contacto alimentario”

### ACTIV CLOR
- **Relación con género alimentario**: **solo entorno / superficie / equipo**, salvo prueba más fina en sentido distinto
- **Lógica de residuo o enjuague**: **probable necesidad de aclarado o manejo controlado**, pero no consta aquí el detalle operativo exacto
- **Lógica funcional dominante**:
  - limpieza
  - blanqueo
  - cloración
- **Señales documentales clave**:
  - uso profesional
  - formulación clorada clara
- **Lectura pedagógica**:
  - sirve para distinguir productos clorados de limpieza/blanqueo frente a clorados más claramente orientados a limpieza-desinfección compleja

### ALICLOR COMPLET
- **Relación con género alimentario**: **solo entorno / superficie / equipo / utensilio**, aunque dentro de industria alimentaria
- **Lógica de residuo o enjuague**: **muy probablemente requiere manejo controlado y lógica de limpieza-desinfección con posterior gestión adecuada**, pero el detalle fino no se fuerza aquí
- **Lógica funcional dominante**:
  - limpieza
  - desinfección
  - desengrase
- **Señales documentales clave**:
  - uso en industria alimentaria
  - uso ambiental
  - registro/documentación fuerte
  - perfil bactericida/fungicida clorado
- **Lectura pedagógica**:
  - pieza muy buena para aprender la diferencia entre limpiar una instalación alimentaria y tratar directamente el género

### TUNELIMP
- **Relación con género alimentario**: **solo entorno / equipo / línea de lavado**, no como tratamiento directo simple del género
- **Lógica de residuo o enjuague**: **presupone proceso técnico controlado y probablemente aclarado**, aunque no consta aquí el modo exacto
- **Lógica funcional dominante**:
  - limpieza
  - lavado técnico cáustico
- **Señales documentales clave**:
  - detergente lavavajillas
  - entorno técnico industrial
- **Lectura pedagógica**:
  - buen ejemplo de limpieza fuerte de línea o sistema, no de química de acabado o de contacto manual

### DERGEL SO
- **Relación con género alimentario**: **sin contacto principal con género; sí con persona que opera en entorno alimentario**
- **Lógica de residuo o enjuague**: **sin residuo / no residuo**, según la lógica declarada del producto
- **Lógica funcional dominante**:
  - higiene de manos
  - lavado
- **Señales documentales clave**:
  - industria alimentaria
  - sin perfume
  - sin colorantes
  - sin residuo
- **Lectura pedagógica**:
  - muy útil para separar higiene personal funcional de sanitización rápida y de limpieza de superficies

### BRINET BQ
- **Relación con género alimentario**: **solo entorno / superficie / suelo**
- **Lógica de residuo o enjuague**: **no consta con limpieza suficiente; parece mantenimiento general más que producto de zona crítica de género**
- **Lógica funcional dominante**:
  - limpieza
  - mantenimiento
- **Señales documentales clave**:
  - hostelería, hospitales, oficinas, fábricas
  - referencia de posible uso en industria alimentaria
- **Lectura pedagógica**:
  - útil para aprender qué parte del catálogo es limpieza comercial general y no química técnica sensible

### BRINET AML
- **Relación con género alimentario**: **solo entorno / superficie / suelo**
- **Lógica de residuo o enjuague**: **no consta con limpieza suficiente**
- **Lógica funcional dominante**:
  - limpieza
  - desodorización
  - mantenimiento
- **Señales documentales clave**:
  - ámbitos de servicios, hostelería y aseos
  - perfil amoniacal
- **Lectura pedagógica**:
  - refuerza la separación entre catálogo de mantenimiento y bloque alimentario técnico sensible

### NETIND
- **Relación con género alimentario**: **solo entorno / pieza / superficie técnica**
- **Lógica de residuo o enjuague**: **no consta aquí; la lógica principal va más por evaporación/disolución/uso técnico profesional que por enjuague alimentario**
- **Lógica funcional dominante**:
  - limpieza técnica
  - disolución
- **Señales documentales clave**:
  - uso exclusivo profesional
  - inflamabilidad / aspiración como riesgos dominantes
- **Lectura pedagógica**:
  - demuestra que parte del catálogo Chemie entra por carriles de solvente, no de detergencia o desinfección

### TR-20
- **Relación con género alimentario**: **indirecta probable con posible efecto funcional sobre género tratado dentro del proceso**
- **Lógica de residuo o enjuague**: **punto crítico**, porque se presenta para agua de lavado y eliminación de residuos/fitosanitarios; aquí el tema residuo y proceso es central
- **Lógica funcional dominante**:
  - tratamiento de agua/proceso
  - mejora de lavado
  - mejora de acabado
- **Señales documentales clave**:
  - industria alimentaria hortofrutícola
  - túneles DINOX
  - especial orientación a tomate
  - referencias de calidad alimentaria en anexo
- **Lectura pedagógica**:
  - junto con OXISAN e HIDROBRILL, es de las piezas más valiosas para entender química de proceso hortofrutícola

### CHEMGRAS BAC
- **Relación con género alimentario**: **solo entorno / superficie / equipo**, salvo soporte posterior más específico
- **Lógica de residuo o enjuague**: **probable manejo con aclarado/control**, pero no consta aquí el detalle operativo fino
- **Lógica funcional dominante**:
  - limpieza
  - desengrase
  - higienización no clorada
- **Señales documentales clave**:
  - FDS fuerte
  - presencia de amonios cuaternarios
  - higienizante no clorado
- **Lectura pedagógica**:
  - pieza buenísima para separar desinfección/higienización no clorada de las líneas cloradas del catálogo

### IBERFARM L
- **Relación con género alimentario**: **auxiliar técnico sin contacto directo principal**, aunque muy vinculado a procesado y envasado de alimentos
- **Lógica de residuo o enjuague**: **la clave es compatibilidad técnica y pureza, no la lógica clásica de enjuague**
- **Lógica funcional dominante**:
  - lubricación
  - antiadherencia
  - desmoldeo
  - abrillantado técnico
- **Señales documentales clave**:
  - FDA
  - Farmacopeas
  - CE 1935/2004
  - USDA H-1 / NSF
- **Lectura pedagógica**:
  - junto con V-80, enseña muy bien la familia de auxiliares técnicos atóxicos de uso alimentario

### LICOGEL
- **Relación con género alimentario**: **solo indirecta respecto al género; directa sobre mano/superficie/utensilio**
- **Lógica de residuo o enjuague**: **consta lógica de uso directo sin aclarado sobre superficies**, lo cual lo hace distinto de otros productos del mapa
- **Lógica funcional dominante**:
  - sanitización
  - higiene rápida
- **Señales documentales clave**:
  - base hidroalcohólica
  - uso directo
  - industria alimentaria / hostelería / colectividades
- **Lectura pedagógica**:
  - muy útil para separar jabón de manos, sanitización rápida y desinfección fuerte de superficies

### TUNELIMP CL
- **Relación con género alimentario**: **solo entorno / línea / cajas / material**, no género directo según lo que hoy consta
- **Lógica de residuo o enjuague**: **probable proceso con aclarado y control técnico**, pero no consta aquí el detalle completo
- **Lógica funcional dominante**:
  - limpieza
  - higienización
  - cloración técnica de túnel
- **Señales documentales clave**:
  - industria alimentaria
  - cajas de fruta
  - material de vidrio y material usado en alimentación
- **Lectura pedagógica**:
  - permite diferenciar mejor entre detergencia técnica general de línea y variante clorada e higienizante más específica

---

## Lecturas maestras que deja ya esta capa

### 1. El eje más valioso para tu aprendizaje probablemente es este
#### Química de proceso hortofrutícola / alimentario sensible
- OXISAN
- HIDROBRILL
- TR-20

Porque aquí se cruzan:
- agua de lavado
- tratamiento del proceso
- acabado del producto
- residuo
- encaje alimentario
- posible conexión eco

### 2. Hay tres grandes mundos que conviene no mezclar
#### A. Limpieza y desinfección de entorno
- CHEMGRAS DS
- ACTIV CLOR
- ALICLOR
- TUNELIMP
- CHEMGRAS BAC
- TUNELIMP CL

#### B. Higiene personal / sanitización rápida
- DERGEL SO
- LICOGEL

#### C. Auxiliares técnicos alimentarios
- V-80
- IBERFARM L

### 3. “Industria alimentaria” no quiere decir siempre lo mismo
Puede significar cosas muy distintas:
- producto para manos en entorno alimentario
- producto para superficie/equipo en industria alimentaria
- producto que entra en agua o proceso de lavado
- producto técnico de lubricación o contacto indirecto compatible con alimentos

Ese matiz es probablemente de las cosas más importantes que necesitas interiorizar.

### 4. “Eco” sigue siendo una excepción muy controlada
No conviene contaminar este mapa con la idea de que todo lo hortofrutícola o alimentario tiene lectura eco.
A día de hoy, la referencia fuerte sigue siendo **OXISAN**.

---

## Conclusión ejecutiva
Esta capa 3 ya permite leer el catálogo con una lógica bastante más madura.

La idea clave sería esta:

> **La pregunta buena ya no es solo “qué producto es”, sino “sobre qué actúa, qué deja o evita dejar, y si su papel real es limpiar, higienizar, tratar, acabar o ayudar técnicamente al proceso”.**

Eso sí puede convertirse en una base sólida de aprendizaje y futura base de datos útil.

---

## Siguiente paso recomendado
A partir de aquí, el siguiente salto fuerte sería una **capa 4 estructurada casi como base de datos**, con campos normalizados tipo:
- `producto`
- `familia_funcional`
- `intervencion_principal`
- `contacto_genero`
- `tipo_contacto`
- `logica_residuo`
- `logica_funcional`
- `industria_alimentaria_si_no`
- `eco_si_consta`
- `soporte_documental`
- `dosificacion_consta_si_no`
- `dudas`

### Mi recomendación real
Yo iría ya a esa capa 4.
Porque sería el paso natural para transformar todo esto en la **base de datos mental y luego documental** que quieres construir.
