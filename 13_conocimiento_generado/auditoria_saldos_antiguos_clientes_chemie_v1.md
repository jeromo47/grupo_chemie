# Auditoría de saldos antiguos de clientes Chemie v1

## Objetivo
Hacer una primera limpieza conceptual de los **saldos antiguos de clientes de Chemie** para distinguir entre:
- pendiente comercial razonablemente vivo
- arrastre histórico contable
- efectos devueltos o renovados
- importes anulados que no deben leerse como riesgo real pleno

---

## Fuente principal
- `/home/jero/cloud/02_proyectos/grupo_familiar/00_inbox/2026-05-22_paquete_informe_consultoria_grupo_chemie_2024_2025/descomprimido/03_cobros_bancos_deuda_grupo.txt`

---

## 1. Conclusión principal
La bolsa de pendientes de clientes de Chemie **no debe leerse como una morosidad simple y homogénea**.

Lo que aparece es una mezcla de tres capas:
1. **pendiente reciente o razonablemente vivo**
2. **saldos históricos arrastrados durante años**
3. **efectos anulados/devueltos/renovados** que exigen depuración antes de tratarlos como riesgo comercial real

La buena noticia es que el propio paquete ya ayuda bastante a separar esas capas.

---

## 2. Foto general de pendientes ajustados 2025
### Resumen por estados
- **Cobrado**: 42 vencimientos | 122.504,70 € | pendiente ajustado asociado 89.552,92 €
- **Pendiente**: 23 vencimientos | 23.025,33 € | pendiente ajustado 23.025,33 €
- **Dev-Ren**: 1 vencimiento | 7.592,59 € | pendiente ajustado 7.592,59 €
- **Devuelto**: 1 vencimiento | 974,05 € | pendiente ajustado 974,05 €
- **Anulado**: 12 vencimientos | 24.085,85 € | pendiente ajustado final 867,57 €

### Lectura rápida
Esto ya dice algo importante:
- no todo lo que aparece en bruto como vencimiento abierto equivale a riesgo vivo
- la capa `Anulado` distorsiona bastante la foto si se lee mal
- hay una **bolsa histórica previa a 2024** claramente identificable

---

## 3. Bolsa histórica arrastrada de 2024 a 2025
### Pendientes anteriores que sobreviven al cierre 2025
El bloque `PTE_CLIENTES_ANTERIOR_2024_A_2025` recoge estos principales saldos heredados:

- **Mercedes Martínez Jiménez** -> 8.840,00 €
- **Canalex, S.A.T.** -> 7.592,59 €
- **Agrupa Adra, S.A.** -> 3.633,57 €
- **Emilio Malpica Expósito, S.L.** -> 1.200,21 €
- **Hortofrutícola Méndez, S.A.** -> 974,05 €
- **Agroponiente Natural Produce, S.L.** -> 867,57 €
- **Agro Organics, Sdad. Coop. And.** -> 775,61 €
- **E.H. Femago, S.A.** -> 703,56 €
- **Caroexport, S.C.A.** -> 624,08 €
- **Darzoves Ispanija, S.L.** -> 467,06 €
- **Construcciones Alfonso Gómez, S.L.** -> 350,20 €
- **Albufera Marketing, S.L.** -> 318,60 €
- **Trans-Algaida, S.L.** -> 250,56 €

### Lectura
Aquí está el verdadero núcleo del arrastre viejo.
No parece una cartera grande de impagos recientes, sino una **mochila antigua de importes heterogéneos** que en varios casos vienen de:
- 2003
- 2006
- 2010
- 2016
- 2017
- 2018
- 2022

### Mi lectura prudente
Esto se parece más a una **bolsa histórica no limpiada del todo** que a un problema comercial actual puro.

---

## 4. Casos prioritarios
### 4.1 Mercedes Martínez Jiménez - 8.840,00 €
- vencimiento: **2016-09-26**
- estado: **Pendiente**

#### Lectura
Este es el saldo individual más llamativo.
Por importe y antigüedad, merece revisión específica.

### 4.2 Canalex, S.A.T. - 7.592,59 €
- vencimiento: **2010-10-30**
- estado: **Dev-Ren**

#### Lectura
Muy relevante.
No parece simple pendiente normal, sino un efecto devuelto o renovado que sigue vivo desde hace muchísimo tiempo.
Esto huele claramente a **arrastre histórico no resuelto**.

### 4.3 Agrupa Adra, S.A. - 3.633,57 €
- varios vencimientos de **2022**
- estado: **Pendiente**

#### Lectura
Este caso parece más reciente y más verosímil como saldo vivo de verdad que los de 2010/2016.

### 4.4 Jerónimo Molina Caparrós - 5.000,00 €
- vencimiento: **2025-05-12**
- estado: **Pendiente**

#### Lectura
No es un saldo antiguo, pero sí un caso especial por tratarse de una **persona del núcleo**.
No entra en “morosidad vieja”, pero sí en **operación vinculada o interna a revisar**.

---

## 5. Qué hacer con los anulados
### Casos visibles
Aparecen anulados, entre otros:
- **Vegacañada, S.A.**
- **Agropo­niente, S.A.**
- **ICA Produkt 2025, S.L.**
- **Indasol**
- **S.A.T. Hortofrutícola Mabe**
- **Agricultores del Sureste**
- **Natursur**
- **Agroponiente Natural Produce**

### Lectura
Aquí conviene no equivocarse:
- figuran como vencimientos en el sistema
- pero su **pendiente ajustado final es cero o casi cero** en la mayoría de casos

### Implicación
No deben meterse automáticamente en la misma bolsa que los impagos reales.
Son más bien:
- anulaciones
- regularizaciones
- o apuntes que el informe ya corrige en gran parte

---

## 6. Qué parece pendiente real y qué parece residuo
### Más cerca de pendiente real
- Agrupa Adra (2022)
- Toledano Hortícola (2025)
- parte del bloque pendiente reciente
- Jerónimo Molina Caparrós (como vinculada a revisar, no como mora vieja)

### Más cerca de residuo histórico / limpieza pendiente
- Canalex (2010, Dev-Ren)
- Mercedes Martínez (2016)
- Caroexport (2006)
- Construcciones Alfonso Gómez (2003)
- Albufera Marketing (2010)
- varios importes pequeños-medios 2017-2018-2022

### Casos especiales
- Hortofrutícola Méndez (Devuelto)
- Agroponiente Natural Produce (Anulado pero con 867,57 ajustados)

---

## 7. Riesgo real estimado de lectura
### Lo que NO haría
No diría ahora mismo que Chemie tenga una morosidad viva problemática por todo el importe bruto que aparece desperdigado.

### Lo que SÍ diría
Diría que Chemie tiene:
- una **bolsa de saldos viejos mal envejecidos o no depurados del todo**
- más algunos pendientes recientes que sí conviene vigilar

### Traducción práctica
El riesgo principal aquí no es solo comercial.
También es de:
- calidad contable
- limpieza de históricos
- y posible distorsión del análisis financiero si se toma la cartera tal cual

---

## 8. Qué me parece más probable
Mi hipótesis de trabajo ahora mismo es esta:

> Chemie tiene una contabilidad operativa suficientemente viva y funcional, pero arrastra una pequeña capa de históricos antiguos que probablemente no se ha saneado o cerrado con suficiente disciplina.

Eso encaja bastante con lo demás que hemos visto:
- empresa real
- operativa estable
- mejora financiera en 2025
- pero con residuos históricos contables todavía presentes

---

## 9. Recomendación de siguiente paso
La mejor continuación sería una mini auditoría dirigida de estos tres grupos:

### Grupo 1 - viejos grandes
- Mercedes Martínez Jiménez
- Canalex, S.A.T.
- Agrupa Adra, S.A.

### Grupo 2 - viejos pequeños/medios
- Emilio Malpica
- E.H. Femago
- Caroexport
- Darzoves
- Construcciones Alfonso Gómez
- Albufera Marketing
- Trans-Algaida

### Grupo 3 - especiales
- Jerónimo Molina Caparrós
- Agroponiente Natural Produce
- Toledano Hortícola

---

## 10. Conclusión ejecutiva
Si tuviera que resumir esta auditoría en una frase:

> **Más que una mora comercial masiva, Chemie parece arrastrar una mochila de saldos históricos y casos especiales que conviene depurar para que la lectura financiera sea limpia.**

Eso, honestamente, me preocupa bastante menos que un impago reciente generalizado, pero sí me parece una buena pista de auditoría interna.
