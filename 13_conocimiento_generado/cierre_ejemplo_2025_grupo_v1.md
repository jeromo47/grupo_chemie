# Cierre ejemplo 2025 del grupo v1

## Objetivo
Usar la plantilla de cierre mensual mínimo como inspiración para construir un **cierre ejemplo anual 2025** con la base ya consolidada del proyecto.

Este documento no pretende fingir un cierre contable perfecto mes a mes.
Pretende enseñar **cómo debería leerse el grupo** cuando empieces a usar un sistema de control real.

Por eso, aquí el objetivo no es el detalle cronológico mensual fino.
El objetivo es construir una **lectura ejecutiva 2025 útil, prudente y reutilizable**.

---

## Datos básicos del cierre
- **Periodo revisado:** ejercicio 2025
- **Tipo de pieza:** cierre ejemplo / cierre escuela / lectura marco
- **Preparado por:** Minion
- **Base usada:** lecturas ya consolidadas del paquete económico 2024-2025 y análisis DuckDB del grupo
- **Límite principal:** no sustituye un cierre contable formal ni una revisión mensual real extraída directamente del programa

---

# 1. Resumen ejecutivo
## 1.1 Qué ha pasado en 2025
- **Chemie** confirma su papel de motor económico del núcleo y mejora frente a 2024.
- **ACI / ALMERIENSE** mantiene entidad económica, pero su lectura comercial y de margen sigue muy contaminada por mezcla de capas y problemas fuertes de dato/stock.
- **Ecoclean** se mantiene como pieza real pero menor, más simple y coherente.
- La mejora de **Chemie** parece apoyarse en tres factores: más ventas, mejor margen y alivio financiero claro.
- El principal foco rojo del grupo en lectura de datos sigue estando en **ALMERIENSE**.

## 1.2 Tres ideas clave del ejercicio
1. **Chemie mejora de verdad en 2025 y sigue siendo la pieza tractora del grupo.**
2. **ALMERIENSE no puede leerse como comercial limpia: mezcla mercado, patrimonial, intragrupo y ruido severo de stock/coste.**
3. **El grupo necesita control mensual simple y disciplinado, porque una parte relevante del riesgo ya no está solo en resultados, sino en calidad de lectura y dependencia de personas clave.**

## 1.3 Tres focos a vigilar después de este cierre
1. separar mejor el negocio real de **ACI / ALMERIENSE**
2. consolidar seguimiento de **clientes/proveedores críticos de Chemie**
3. aterrizar un sistema real de cierre mensual y control al entrar en septiembre

---

# 2. Ventas y cartera
## 2.1 Ventas por empresa
- **Chemie:** **630.692,76 €**
- **ACI / ALMERIENSE:** **146.266,63 €**
- **Ecoclean:** **89.077,75 €**

## 2.2 Lectura rápida
- La empresa que tira claramente del grupo es **Chemie**.
- **ACI** mantiene actividad real y no residual, pero muy por debajo de Chemie.
- **Ecoclean** confirma escala menor.

### Comentario breve
La jerarquía del núcleo queda bastante clara en 2025:
- **Chemie** = corazón económico
- **ACI** = pieza intermedia
- **Ecoclean** = línea menor y complementaria

## 2.3 Top clientes / concentración
### Chemie
- top 1: **16,91 %**
- top 3: **45,56 %**
- top 5: **57,27 %**
- top 10: **72,94 %**

Clientes destacados:
- **S.A.T. HORTOFRUTICOLA MABE**
- **INDASOL, S.A.T. Nº9404**
- **EJIDOMAR, Sdad.Coop.And.**

### ACI / ALMERIENSE
- top 1: **44,53 %**
- top 3: **81,90 %**
- top 5: **89,91 %**
- top 10: **96,05 %**

Clientes destacados:
- **EJIDOMAR, Sdad.Coop.And.**
- **AGROPONIENTE NATURAL PRODUCE, S.L.**
- **BOOKING (ARRENDAMIENTO MACENAS)**
- **GRUPO CHEMIE LA JUAIDA, S.L.**

### Ecoclean
- top 1: **6,89 %**
- top 3: **17,20 %**
- top 5: **25,58 %**
- top 10: **40,08 %**

### Lectura de concentración
- **Chemie** tiene concentración relevante, pero dentro de una cartera más real y estructurada.
- **ALMERIENSE** tiene concentración extrema y además mezcla cliente mercado, patrimonial e intragrupo.
- **Ecoclean** tiene la cartera más atomizada.

---

# 3. Margen y calidad comercial
## 3.1 Margen por empresa
### Chemie
- margen total líneas 2025: **303.356,20 €**
- margen core limpio 2025: **286.569,37 €**

### ACI / ALMERIENSE
- lectura no limpia todavía
- la capa de mercado sale con un margen agregado extremadamente negativo, pero contaminado por stock/coste/maestro poco fiables

### Ecoclean
- estructura comercial simple y razonablemente coherente
- sin gran alerta visible comparable a ALMERIENSE

## 3.2 Lectura rápida
- **Chemie** no solo mueve ventas, también sostiene margen reconocible.
- **ALMERIENSE** sigue siendo el gran foco de prudencia: no conviene leer su margen bruto como verdad económica limpia.
- **Ecoclean** parece más sencilla y legible.

## 3.3 Familias / líneas relevantes
### Chemie - familias troncales 2025
1. **08 CELULOSA-LINEA BLANCA** -> **194.711,45 €** ventas | **81.217,35 €** margen
2. **09 PROD. Y ACCESORIOS PARA LIMPIEZA** -> **126.589,05 €** | **50.004,38 €**
3. **03 PROD. ESPECIALES INDUST. ALIMENTARIA** -> **101.262,90 €** | **63.474,43 €**
4. **01 DESENGRASANTES Y LIMPIADORES GENERALES** -> **74.493,40 €** | **50.115,10 €**
5. **06 PINTURAS Y DISOLVENTES** -> **73.488,30 €** | **28.281,08 €**

### Ecoclean - familias troncales 2025
- limpieza
- celulosa
- desengrasantes
- especiales industria alimentaria

### ACI / ALMERIENSE
- margen/familias contaminados por referencias genéricas, stock absurdo, líneas patrimoniales y mezcla de capas

## 3.4 Incidencias de calidad comercial
### ALMERIENSE
- referencias `999999`, `000000` y vacías con ruido fuerte
- stock absurdo y muy contaminado
- familias vacías o no comerciales mezcladas con actividad real
- margen 2025 de mercado no fiable sin depuración previa

### Comentario breve
El negocio más “sano para leer” en 2025 es claramente **Chemie**.
El más peligroso de leer mal es **ALMERIENSE**.

---

# 4. Compras y abastecimiento
## 4.1 Compras por empresa
- **Chemie:** **433.441,08 €**
- **ACI / ALMERIENSE:** **83.534,85 €**
- **Ecoclean:** **27.924,11 €**

## 4.2 Concentración de proveedores
### Chemie
- top 1: **18,52 %**
- top 3: **38,41 %**
- top 5: **50,52 %**
- top 10: **71,86 %**

Proveedores destacados:
- **DICOCEL, S.A.**
- **INDUSTRIA PAPELERA DE MURO, S.L.**
- **DETERVAL CHEMICAL, S.L.**
- **JABIPACK, S.L.**
- **MANGIR UTILITIES, S.L.**

### ACI / ALMERIENSE
- top 1: **18,48 %**
- top 3: **29,17 %**
- top 5: **37,18 %**
- top 10: **52,46 %**

### Ecoclean
- top 1: **30,40 %**
- top 3: **60,64 %**
- top 5: **81,75 %**
- top 10: **98,88 %**

## 4.3 Lectura de abastecimiento
- **Chemie** depende de un núcleo proveedor fuerte, pero coherente con su negocio.
- **Ecoclean** tiene una base pequeña y concentrada, normal por escala, pero frágil si falla un proveedor clave.
- **ALMERIENSE** no parece tan tensionada por proveedores como por calidad de lectura comercial y concentración de ingresos.

---

# 5. Cobros, pagos, bancos y deuda
## 5.1 Clientes pendientes
### Chemie
La mejor lectura actual es:
- el pendiente real está **muy concentrado** en pocos casos grandes
- una parte relevante corresponde a:
  - **Mercedes Martínez Jiménez**
  - **Agrupa Adra**
  - **Jerónimo Molina Caparrós** (pero este no debe leerse como mora comercial normal, sino como operación patrimonial interna ligada a la Ducati)
- existe además una cola larga de importes pequeños antiguos que parece más residuo histórico que riesgo comercial agudo

### Lectura
No parece un colapso general de cobros.
Parece un riesgo concentrado + suciedad histórica pendiente de depurar.

## 5.2 Bancos y deuda - Chemie
- **Bancos 2025:** **59.106,93 €**
- **Deuda detectada 2025:** **23.166,77 €**
- **Intereses 2025:** **2.609,34 €**

### Comparación con 2024
- más banco
- menos deuda
- mucha menos carga financiera

## 5.3 Lectura financiera rápida
La mejora financiera de **Chemie** en 2025 parece bastante real.
La mejor explicación hoy es una combinación de:
- más ventas
- más margen
- menos presión financiera

### Comentario breve
Este es uno de los mejores datos del cierre 2025 del grupo.

---

# 6. Alertas especiales
## 6.1 ACI / ALMERIENSE
### Alertas fuertes
- concentración extrema de ingresos
- mezcla de mercado, patrimonial e intragrupo
- stock muy contaminado
- referencias genéricas que distorsionan margen y lectura
- margen 2025 no interpretable limpiamente sin depuración previa

### Juicio
**ALMERIENSE** es hoy la pieza más peligrosa de leer mal.
No porque sepamos ya que sea un desastre real cerrado,
sino porque mezcla demasiadas capas y demasiado ruido de dato.

## 6.2 Chemie
### Alertas principales
- concentración relevante de clientes top
- dependencia de un núcleo proveedor importante
- pendiente comercial concentrado en pocos nombres
- necesidad de no confiarse con la mejora 2025 sin sostener control mensual después

### Juicio
**Chemie** es la pieza más fuerte del grupo, pero precisamente por eso merece control disciplinado.

## 6.3 Ecoclean
### Alertas principales
- escala pequeña
- base de proveedores concentrada
- menos peso estratégico, pero no conviene perderla de vista

---

# 7. Lectura final del ejercicio
## 7.1 Qué ha ido bien
1. **Chemie mejora de forma visible en 2025.**
2. El núcleo del grupo se entiende mucho mejor y con más base económica real.
3. Ya se distinguen con más claridad los negocios legibles de los contaminados.

## 7.2 Qué preocupa
1. **ALMERIENSE** sigue siendo una caja mezclada de negocio, patrimonialidad, intragrupo y dato sucio.
2. El grupo sigue teniendo alta dependencia de personas clave para entender y gobernar bien estos números.
3. Falta todavía un uso disciplinado y repetible del control mensual.

## 7.3 Qué habría que vigilar después de este cierre
1. clientes/proveedores críticos de **Chemie**
2. separación real de capas en **ACI / ALMERIENSE**
3. depuración del pendiente histórico y lectura práctica de cobros/pagos

---

# 8. Conclusión ejecutiva
Si tuviera que resumir este cierre ejemplo 2025 en una frase:

> **2025 deja a Chemie como motor del grupo con mejora real y deja a ALMERIENSE como la gran pieza que todavía exige separación, limpieza de dato y lectura mucho más fina.**

Y si tuviera que resumir la utilidad de esta pieza:

> **sirve para mostrar cómo debería empezar a pensarse un cierre del grupo: no solo como suma de cifras, sino como lectura de negocio, calidad de dato, concentración y alertas.**

---

# 9. Huecos concretos que sí podrían justificar extracción nueva de BBDD
No hace falta pedir nada todavía por defecto.
Pero, si quisiéramos mejorar esta pieza con ayuda del chat técnico de BBDD, las siguientes extracciones sí tendrían sentido:

1. cierre mensual real de un mes reciente de 2026 por empresa
2. ventas/margen/compras por mes 2026
3. clientes pendientes y proveedores pendientes por corte de último mes cerrado
4. bancos/deuda por corte reciente
5. primer detalle mensual de ALMERIENSE separado en:
   - mercado
   - patrimonial
   - intragrupo
   - ruido/genéricas si la base lo permite

### Regla buena
Pedir solo lo que ayude a aterrizar el próximo cierre real, no por acumular datos.
