# Análisis de concentración de clientes y dependencia comercial v1

## Objetivo
Abrir la nueva fase de preparación remota para septiembre con un primer análisis 100 % explotable desde DuckDB:
- concentración real de clientes
- dependencia por comercial

Fuentes usadas:
- `t_07a_ventas_lineas_grupo_2024_2025`
- `t_07h_clientes_maestro_grupo`
- y salidas de control generadas en `13_CONSULTAS_CONTROL`

Archivos soporte creados:
- `13J14_top10_clientes_concentracion_por_empresa_anio.csv`
- `13J15_resumen_concentracion_clientes.csv`
- `13J16_resumen_clientes_por_comercial_maestro.csv`
- `13J17_ventas_por_comercial_empresa_anio.csv`

---

## 1. Dato confirmado - concentración de clientes
### ALMERIENSE
#### 2024
- clientes con ventas: **34**
- top 1: **33,05 %**
- top 3: **71,60 %**
- top 5: **85,47 %**
- top 10: **92,20 %**

#### 2025
- clientes con ventas: **24**
- top 1: **44,53 %**
- top 3: **81,90 %**
- top 5: **89,91 %**
- top 10: **96,05 %**

### Lectura prudente
ALMERIENSE muestra una **concentración comercial muy alta**. El negocio parece depender de muy pocos clientes, y además la concentración empeora en 2025.

---

### CHEMIE
#### 2024
- clientes con ventas: **71**
- top 1: **16,05 %**
- top 3: **40,57 %**
- top 5: **57,29 %**
- top 10: **74,06 %**

#### 2025
- clientes con ventas: **57**
- top 1: **16,91 %**
- top 3: **45,56 %**
- top 5: **57,27 %**
- top 10: **72,94 %**

### Lectura prudente
CHEMIE también tiene concentración relevante, pero bastante menos extrema que ALMERIENSE. Parece una cartera con más base real, aunque el top 10 sigue pesando mucho.

---

### ECOCLEAN
#### 2024
- clientes con ventas: **90**
- top 1: **7,18 %**
- top 3: **16,49 %**
- top 5: **23,14 %**
- top 10: **36,46 %**

#### 2025
- clientes con ventas: **87**
- top 1: **6,89 %**
- top 3: **17,20 %**
- top 5: **25,58 %**
- top 10: **40,08 %**

### Lectura prudente
ECOCLEAN parece la cartera más atomizada de las tres. Eso reduce dependencia de pocos clientes, aunque no implica por sí solo mejor calidad de negocio.

---

## 2. Dato confirmado - dependencia por comercial
## Maestro de clientes
El maestro comercial muestra códigos de comercial, no nombres.

### ALMERIENSE
- comercial `0`: **191** clientes asignados
- comercial `32`: **30**
- resto: volúmenes mucho menores

### Ventas 2025
- comercial `0`: **79.413,45 €** con **19** clientes
- comercial `3`: **65.138,48 €** con **1** cliente
- comercial `32`: **1.714,70 €** con **4** clientes

### Lectura prudente
Aquí hay dos alertas claras:
1. el código `0` parece un gran cajón de asignación comercial
2. el comercial `3` sostiene en 2025 un cliente único muy pesado

Esto obliga a aclarar:
- qué significa exactamente el comercial `0`
- quién es el comercial `3`
- si ese cliente único es una dependencia personal, una cuenta histórica o un caso excepcional

---

### CHEMIE
#### Ventas 2024
- comercial `38`: **194.943,20 €** con **17** clientes
- comercial `36`: **193.568,25 €** con **32** clientes
- comercial `0`: **137.496,77 €** con **19** clientes
- comercial `3`: **56.655,15 €** con **1** cliente

### Lectura prudente
CHEMIE ya muestra una estructura comercial más rica que ALMERIENSE, pero vuelve a aparecer:
- un bloque grande bajo comercial `0`
- un cliente único muy pesado bajo comercial `3`

Eso sugiere que el maestro comercial necesita interpretación humana antes de sacar conclusiones sobre personas concretas.

---

## 3. Qué parece decir este primer corte
### Confirmado
- ALMERIENSE tiene una dependencia de clientes mucho más concentrada que CHEMIE y ECOCLEAN.
- ECOCLEAN tiene una base de clientes bastante más atomizada.
- El maestro comercial contiene códigos que concentran mucha cartera y que deben descifrarse antes de leerlos como comerciales reales individuales.
- Hay indicios de cuentas/clientes muy grandes asociados a un solo código comercial.

### Interpretación prudente
Este análisis ya permite llegar a septiembre con mejor criterio sobre:
- riesgo de concentración comercial
- necesidad de mapear quién es quién en el maestro comercial
- importancia de no leer la red comercial solo por intuición familiar

---

## 4. Preguntas que genera para tío y padre
### Para tío
- ¿Qué significa exactamente el comercial `0` en el maestro? ¿es sin asignar, cartera histórica, administración o mezcla?
- ¿Quiénes son los códigos comerciales `3`, `36`, `38` y `32` en la práctica real?
- ¿Qué clientes muy grandes dependen de una sola relación personal o de una sola cuenta comercial?
- ¿Qué parte del maestro comercial está limpia y qué parte es histórica o poco fiable?

### Para padre
- ¿Qué clientes del top 10 de ALMERIENSE y CHEMIE consideras verdaderamente estratégicos?
- ¿Hay clientes de gran peso que realmente dependan de una sola persona?
- ¿Qué cliente parece muy importante por volumen pero en realidad deja poco margen o da muchos problemas?

---

## 5. Pendiente de validar
- identificar nombre/persona real detrás de cada código comercial relevante
- cruzar ventas por comercial con margen por cliente o por familia
- determinar si el comercial veterano coincide con alguno de los códigos de mayor peso
- aislar top clientes concretos para preparar preguntas más finas

---

## 6. Juicio de valor
Este es un muy buen primer frente remoto porque ya cambia la foto del riesgo:
- **ALMERIENSE** aparece como la pieza más concentrada comercialmente
- **CHEMIE** parece más equilibrada, pero con códigos comerciales que exigen descifrado
- **ECOCLEAN** parece menos dependiente de pocos clientes

La siguiente mejora natural es cruzar este análisis con:
1. **top clientes concretos**
2. **margen por familia**
3. **ACI / ALMERIENSE en detalle**, porque la concentración ahí es especialmente alta
