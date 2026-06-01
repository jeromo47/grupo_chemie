# Mini auditoría - Saldos viejos de Chemie v2

## Objetivo
Separar dentro de la bolsa de saldos antiguos de clientes de **Chemie** qué parte parece:
- pendiente real vivo
- arrastre histórico
- devuelto / renovado
- anulado
- o simple residuo contable que ensucia la foto comercial

---

## Fuente principal
- `/home/jero/cloud/02_proyectos/grupo_familiar/00_inbox/2026-05-22_paquete_informe_consultoria_grupo_chemie_2024_2025/descomprimido/03_cobros_bancos_deuda_grupo.txt`

---

## 1. Conclusión principal
La bolsa de saldos viejos de Chemie **sí existe**, pero la lectura ahora es más matizada que “gran morosidad abierta”.

Lo que sale con bastante claridad es esto:
- hay una parte de **pendiente real vivo**
- pero una parte importante del bloque problemático parece ser **residuo histórico o estados no equivalentes a deuda comercial normal**
- especialmente por la presencia de:
  - `Dev-Ren`
  - `Devuelto`
  - `Anulado`

### Traducción clara
La calidad del balance comercial **no es perfecta**, pero tampoco parece que todo ese volumen raro sea dinero realmente pendiente de cobrar en sentido fuerte.

---

## 2. Foto global por estados
En `ESTADOS_CLIENTES_PTE_2025` aparece:
- **Cobrado** -> `42` movimientos -> **122.504,70 €** | pendiente ajustado **89.552,92 €**
- **Pendiente** -> `23` movimientos -> **23.025,33 €** | pendiente ajustado **23.025,33 €**
- **Dev-Ren** -> `1` movimiento -> **7.592,59 €** | pendiente ajustado **7.592,59 €**
- **Devuelto** -> `1` movimiento -> **974,05 €** | pendiente ajustado **974,05 €**
- **Anulado** -> `12` movimientos -> **24.085,85 €** | pendiente ajustado **867,57 €**

---

## 3. Qué significa esto de verdad
### La clave está en `Anulado`
Este bloque es muy importante porque evita sobredramatizar.

Aunque `Anulado` suma **24.085,85 €** de nominal, el pendiente ajustado asociado baja a solo **867,57 €**.

### Lectura
Eso sugiere con mucha fuerza que una parte relevante de los importes llamativos:
- no representan deuda comercial viva en sentido normal
- sino documentos o posiciones ya neutralizadas, corregidas o sin verdadera exigibilidad económica

### Implicación
El nominal bruto asusta más que la realidad económica ajustada.

---

## 4. Qué sigue siendo realmente delicado
### 4.1 Pendiente vivo
Aquí sí hay materia real:
- **23** movimientos
- **23.025,33 €** ajustados

Este es el bloque que más debería importarnos si queremos medir riesgo comercial real.

### 4.2 Dev-Ren
Aparece:
- **Canalex, S.A.T.**
- estado `Dev-Ren`
- **7.592,59 €**
- origen muy antiguo: **2010-10-30**

### Lectura
Esto ya no suena a pendiente reciente normal.
Suena a:
- efecto devuelto/renovado
- saldo histórico enquistado
- o posición antigua no terminada de limpiar

### 4.3 Devuelto
Aparece:
- **Hortofrutícola Méndez, S.A.**
- **974,05 €**
- fecha muy antigua: **2010-01-10**

### Lectura
Esto refuerza que Chemie arrastra algo de memoria contable vieja.
No parece una gran alarma por importe, pero sí síntoma de **depuración imperfecta**.

---

## 5. Casos principales detectados
### Mercedes Martínez Jiménez
- **8.840,00 €**

Sigue siendo uno de los importes más llamativos del bloque.
Con lo visible aquí no queda reclasificado en anulado/devuelto, así que merece respeto analítico.

### Canalex, S.A.T.
- **7.592,59 €** en `Dev-Ren`
- además aparece otra línea vieja de 2012 con estado `Devuelto` y pendiente ajustado **2.203,82 €**

Este caso parece más un **nudo histórico contable/comercial** que un pendiente nuevo normal.

### Jerónimo Molina Caparrós
- **5.000,00 €**
- estado `Pendiente`
- fecha **2025-05-12`

Este caso no debe leerse como saldo viejo genérico, porque ya quedó contextualizado: está ligado probablemente a la **Ducati** dentro de una operación patrimonial interna.

### Agrupa Adra, S.A.
- **3.633,57 €**
- fecha **2022-09-15**

Sí parece uno de los saldos vivos a vigilar dentro del bloque pendiente.

---

## 6. Mi lectura global de calidad del balance comercial
### Lo malo
- Chemie sí arrastra residuos históricos
- hay saldos muy viejos todavía visibles
- la limpieza de ciertos clientes no parece completamente afinada

### Lo no tan malo
- una parte relevante del bloque ruidoso no es pendiente comercial puro, sino:
  - anulado
  - devuelto
  - dev-ren
  - o residuo histórico reclasificado

### Traducción honesta
El balance comercial de Chemie **no está sucio de una forma catastrófica**, pero sí presenta un nivel de arrastre histórico que pide:
- limpieza
- explicación
- o separación interna más fina

---

## 7. Qué cambia respecto a una lectura alarmista
### Lectura superficial
“Chemie tiene una gran bolsa de clientes impagados.”

### Lectura más correcta
“Chemie tiene una combinación de:
- pendiente vivo real
- operaciones vinculadas concretas
- y bastante residuo histórico/documental que no debe confundirse automáticamente con mora comercial exigible.”

Esto cambia bastante el tono.

---

## 8. Qué me preocuparía de verdad
### Prioridad 1
Los **23.025,33 €** en estado `Pendiente`.
Ese sí es el bloque a depurar si queremos medir riesgo actual.

### Prioridad 2
Los grandes casos individuales todavía no claramente neutralizados, sobre todo:
- Mercedes Martínez Jiménez
- Agrupa Adra
- y cualquier otro saldo alto realmente vivo

### Prioridad 3
Canalex como caso histórico enredado.
No tanto por ser el mayor riesgo vivo inmediato, sino por ser un buen ejemplo de saldo viejo mal digerido.

---

## 9. Qué se puede afirmar ya con bastante seguridad
- Chemie sí tiene **bolsa de saldos históricos**
- no todo el bloque problemático equivale a **mora viva real**
- el estado `Anulado` reduce muchísimo el peso económico real del nominal bruto
- hay una zona de **pendiente real** en torno a **23.025,33 €** que sí merece atención
- la calidad del balance comercial es **aceptable con arrastre**, no limpia del todo pero tampoco desbordada

---

## 10. Conclusión ejecutiva
Si tuviera que resumir esta mini auditoría en una frase:

> **Chemie arrastra saldos antiguos y algo de suciedad histórica en clientes, pero una parte importante del ruido no es deuda comercial viva, sino residuo contable o estados ya degradados como anulado, devuelto o dev-ren.**

Eso me parece importante, porque mejora bastante la lectura de calidad del balance: hay trabajo de depuración pendiente, sí, pero no parece un agujero comercial tan grande como sugería una lectura bruta.

---

## 11. Siguiente paso recomendado
Veo dos caminos útiles:

1. bajar al detalle del bloque `Pendiente` para identificar cuáles son los **saldos vivos realmente preocupantes**
2. o pasar a una lectura ya más alta de **calidad global del núcleo** con todo lo consolidado

### Mi recomendación real
Yo haría primero el **detalle fino del bloque Pendiente**.
Porque ya hemos limpiado el ruido, y ahora toca ver qué mora o exposición real queda de verdad.
