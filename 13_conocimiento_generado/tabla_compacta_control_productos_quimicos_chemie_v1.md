# Tabla compacta de control - productos químicos Chemie v1

## Objetivo
Tener una vista corta, comparativa y manejable del núcleo de productos ya trabajados, útil para:
- consultar rápido
- comparar productos entre sí
- detectar huecos documentales
- y seguir alimentando una futura base de datos sin perder criterio

Esta tabla no sustituye a las capas largas.
Las resume.

---

## Leyenda corta
- **Intervención**:
  - `MANO`
  - `SUP/EQ` = superficie/equipo/utensilio/línea
  - `AGUA` = agua de proceso/lavado
  - `GEN` = género/producto tratado
  - `AUX` = auxiliar técnico/proceso/maquinaria
- **Contacto género**:
  - `DIR` = directa probable
  - `IND` = indirecta probable
  - `NO` = no principal / solo entorno
- **Residuo**:
  - `SIN` = lógica de no residuo
  - `ACL` = probable aclarado/enjuague o control posterior
  - `PROC` = residuo/proceso sensible o dependiente del circuito
  - `NC` = no consta con limpieza suficiente
- **Soporte**:
  - `ALTO`
  - `MED-ALTO`
  - `MEDIO`
  - `MED-BAJO`
- **Eco**:
  - `SI`
  - `NO`
  - `NC`

---

## Tabla compacta

| Producto | Familia corta | Intervención | Contacto género | Residuo | Lógica principal | Alimentario | Eco | Soporte | Dosificación | Duda clave corta |
|---|---|---|---|---|---|---|---|---|---|---|
| **OXISAN** | oxidante proceso | AGUA | IND | PROC | tratamiento + higienización | Sí | **SI** | **ALTO** | No | encaje exacto proceso/coadyuvante |
| **CHEMGRAS DS** | desengrasante industrial | SUP/EQ | NO | ACL | limpieza + desengrase | No clara | NO | **ALTO** | No | usos concretos y vigencia |
| **HIDROBRILL** | secante-abrillantador | GEN | DIR | PROC | acabado + secado + brillo | Sí | NO | **MED-BAJO** | No | FDS y encaje técnico fino |
| **V-80** | aceite blanco alimentario | AUX | NO | NC | lubricación + auxiliar técnico | Sí | NO | **MED-ALTO** | No | FDS y diferencia real con IBERFARM L |
| **ACTIV CLOR** | clorado limpieza/blanqueo | SUP/EQ | NO | ACL | limpieza + blanqueo | No clara | NO | **ALTO** | No | usos actuales frente a otras líneas cloradas |
| **ALICLOR COMPLET** | clorado limpieza-desinfección | SUP/EQ | NO | ACL | limpieza + desinfección + desengrase | Sí | NO | **ALTO** | No | vigencia exacta de registro/formulación |
| **TUNELIMP** | detergente cáustico de línea | SUP/EQ | NO | ACL | limpieza técnica de lavado | Sí probable | NO | **ALTO** | No | relación exacta con TUNELIMP CL |
| **DERGEL SO** | lavado manos sin residuo | MANO | NO | **SIN** | higiene manos | Sí | NO | **MEDIO** | No | FDS y peso comercial real |
| **BRINET BQ** | limpieza general bioalcohol | SUP/EQ | NO | NC | limpieza + mantenimiento | Sí secundaria | NO | **MED-BAJO** | No | qué significa “apto” en alimentaria |
| **BRINET AML** | limpiador amoniacal | SUP/EQ | NO | NC | limpieza + desodorización | No clara | NO | **MED-BAJO** | No | FDS y vigencia real |
| **NETIND** | disolvente técnico | SUP/EQ | NO | NC | limpieza técnica + disolución | No clara | NO | **ALTO** | No | peso real de la familia solvente |
| **TR-20** | aditivo aguas lavado | AGUA | IND | PROC | tratamiento proceso + acabado | Sí | NC | **MEDIO** | No | FDS y encaje exacto de proceso |
| **CHEMGRAS BAC** | higienizante no clorado | SUP/EQ | NO | ACL | limpieza + desengrase + higienización | Sí probable | NO | **ALTO** | No | peso real frente a CHEMGRAS DS |
| **IBERFARM L** | lubricante alimentario atóxico | AUX | NO | NC | lubricación + antiadherencia + desmoldeo | Sí | NO | **MED-ALTO** | No | relación exacta con V-80 |
| **LICOGEL** | sanitizante hidroalcohólico | MANO / SUP | NO | **SIN** | sanitización rápida | Sí | NO | **MEDIO** | Parcial sí | FDS y soporte completo de usos |
| **TUNELIMP CL** | túnel clorado higienizante | SUP/EQ | NO | ACL | limpieza + higienización + cloración | Sí | NO | **MEDIO** | No | FDS específica y relación con TUNELIMP |

---

## Cómo leer rápido la tabla

### 1. Los más sensibles para aprender proceso alimentario/hortofrutícola
- **OXISAN**
- **HIDROBRILL**
- **TR-20**

### 2. Los más útiles para distinguir limpieza de entorno vs proceso
- **CHEMGRAS DS**
- **ALICLOR COMPLET**
- **TUNELIMP**
- **CHEMGRAS BAC**
- **TUNELIMP CL**

### 3. Los que te enseñan la familia de auxiliares técnicos alimentarios
- **V-80**
- **IBERFARM L**

### 4. Los que separan higiene de manos / sanitización rápida
- **DERGEL SO**
- **LICOGEL**

### 5. Los más flojos documentalmente por ahora
- **HIDROBRILL**
- **BRINET BQ**
- **BRINET AML**
- **TR-20**
- **LICOGEL**
- **TUNELIMP CL**

---

## Lecturas maestras que deja esta tabla

### A. Qué toca género o proceso sensible
- **HIDROBRILL** = más cerca del género tratado
- **OXISAN** y **TR-20** = más cerca del agua/proceso con posible efecto sobre género

### B. Qué es solo entorno/superficie
- CHEMGRAS DS
- ACTIV CLOR
- ALICLOR COMPLET
- TUNELIMP
- BRINET BQ
- BRINET AML
- NETIND
- CHEMGRAS BAC
- TUNELIMP CL

### C. Qué es auxiliar técnico, no limpiador
- **V-80**
- **IBERFARM L**

### D. Qué tiene eco real en lo trabajado
- **OXISAN**

---

## Juicio final
Esta tabla ya sirve bastante bien como **panel corto de control**.

No sustituye a las fichas largas, pero sí permite ver de un vistazo:
- dónde actúa cada producto
- qué lógica tiene
- cuál es su nivel documental
- y qué dudas merece la pena cerrar primero

---

## Siguiente paso recomendable
Si quieres seguir construyendo base de datos buena de verdad, yo haría después una de estas dos:

1. **pasar esta tabla a CSV** con columnas fijas
2. **abrir una capa 5 de preguntas inteligentes por producto**, por ejemplo:
   - con qué otro se confunde
   - cuándo elegir uno u otro
   - qué pregunta exacta falta por resolver

### Mi recomendación
Primero **CSV**.
Porque ya te deja una base exportable, filtrable y mucho más útil para crecer bien.
