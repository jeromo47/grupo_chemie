# Mini auditoría - Desapalancamiento de Chemie en 2025 v1

## Objetivo
Bajar un nivel más en la explicación de la mejora financiera de Chemie en 2025, intentando responder mejor a esta pregunta:

> **qué deuda baja exactamente y por qué baja**

---

## Fuente principal
- `/home/jero/cloud/02_proyectos/grupo_familiar/00_inbox/2026-05-22_paquete_informe_consultoria_grupo_chemie_2024_2025/descomprimido/03_cobros_bancos_deuda_grupo.txt`
- apoyo complementario en:
  - `mini_auditoria_mejora_financiera_chemie_2025_v1.md`
  - `ficha_prestamos_renting_chemie_inicial.md`

---

## 1. Conclusión principal
La bajada de deuda de Chemie en 2025 **no parece una simple reclasificación cosmética**.

Con lo ya visible, la mejor lectura es que hubo un **desapalancamiento real** apoyado sobre todo en:
- amortización ordinaria continuada de varios préstamos
- al menos una **cuota final fuerte**
- y varias **cancelaciones explícitas** de deuda ligada a activos/vehículos

Esto encaja muy bien con la caída conjunta observada en:
- deuda total detectada
- intereses
- y mejora de posición bancaria

---

## 2. La señal global ya conocida
### Foto resumida
- deuda detectada **2024** -> **48.941,82 €**
- deuda detectada **2025** -> **23.166,77 €**
- variación -> **-25.775,05 €**

### Intereses
- **2024** -> **9.230,10 €**
- **2025** -> **2.609,34 €**
- variación -> **-6.620,76 €**

### Bancos
- **2024** -> **44.267,38 €**
- **2025** -> **59.106,93 €**
- variación -> **+14.839,55 €**

### Lectura
La mejora financiera no aparece solo en una línea, sino en varias a la vez.
Eso ya hacía pensar en desapalancamiento real, y el detalle lo refuerza.

---

## 3. Qué préstamos se ven claramente vivos en 2024
En el bloque `MOVIMIENTOS_DEUDA_INTERESES` aparecen varias subcuentas 170 con calendario de cuotas bastante normal:
- **1700000020** -> `PREST.225979`
- **1700000021** -> `PREST.000253`
- **1700000022** -> `PREST.82011`
- **1700000023** -> `PREST.55095`
- **1700000026** -> `PREST.29404`
- **1700000027** -> `PREST.1850196`
- **1700000028** -> `PREST.139901 / 254115 HONDA AFRICA`

### Lectura
Chemie en 2024 sí arrastraba una **cartera de préstamos/financiaciones fragmentada**, no una única deuda grande simple.

---

## 4. Qué baja de forma especialmente clara en 2025
Aquí sale lo más interesante.

### 4.1 Préstamo `1700000022` / `PREST.82011`
#### Secuencia visible en 2025
- apertura 2025 -> **12.341,09 H**
- cuotas normales enero-abril
- **2025-05-09** -> **`CUOTA FINAL PREST FURGONETA 82011` -> 11.416,57 D**

#### Lectura
Esto es una pista muy fuerte de **liquidación final importante** de una financiación ligada a una furgoneta.
No parece simple goteo, sino **cierre casi total del préstamo**.

---

### 4.2 Préstamo `1700000027` / `PREST.1850196`
#### Secuencia visible en 2025
- apertura 2025 -> **3.585,25 H**
- cuotas enero-marzo
- **2025-03-21** -> **`CANCELACION PREST.1850196` -> 2.263,75 D**
- **2025-05-12** -> `AJUSTE PRESTAMO` -> **0,01 D**

#### Lectura
Aquí la interpretación es bastante clara:
- hay una **cancelación expresa** del préstamo
- y un pequeño ajuste residual posterior

Esto sí parece **cancelación real**, no mera reclasificación.

---

### 4.3 Préstamo `1700000028` / Honda Africa
#### Secuencia visible en 2025
- apertura 2025 -> **11.297,10 H**
- cuotas enero-mayo
- **2025-06-09** -> **`CANCELACION PRESTAMO HONDA AFRICA` -> 10.595,01 D**

#### Lectura
Esto también es muy fuerte.
No estamos ante una interpretación difusa: el propio extracto habla de **cancelación**.

Además encaja con el patrón de activos/vehículos que ya veníamos viendo en Chemie.

---

## 5. Qué otras deudas siguen corriendo de forma más normal
No todo se cancela.
También se ve deuda que sigue amortizándose en régimen más ordinario durante 2025:
- `225979`
- `000253`
- `55095`
- `29404`

### Lectura
Esto apunta a una foto equilibrada:
- Chemie no se queda sin deuda de golpe
- pero sí **reduce varias piezas importantes**
- mientras otras siguen su curso normal

---

## 6. Qué me parece que explica de verdad la bajada 2025
### Mi mejor lectura causal
La reducción de deuda 2025 parece apoyarse en tres capas:

#### 1. amortización ordinaria mensual
varios préstamos siguen bajando cuota a cuota.

#### 2. cierres o cuotas finales relevantes
especialmente el caso de la **furgoneta 82011**.

#### 3. cancelaciones explícitas
al menos:
- `PREST.1850196`
- `PRESTAMO HONDA AFRICA`

### Traducción clara
La mejora financiera de Chemie **no parece un maquillaje**, sino una combinación de:
- disciplina de amortización
- cierres efectivos de financiación
- y simplificación parcial de la mochila de deuda

---

## 7. Encaje con la caída de intereses
Esto es importante.

Si en 2025 vemos:
- menos saldo vivo
- cancelaciones
- cuota final grande

entonces encaja muy bien que los **intereses** caigan de:
- **9.230,10 €**
- a **2.609,34 €**

### Lectura
La bajada de intereses ya no parece solo un efecto contable raro.
Parece bastante coherente con una **caída real del stock de deuda financiera**.

---

## 8. Qué sigue abierto
### Aún no queda perfecto
Todavía faltaría, para un cierre más fino:
- mapa uno a uno de cada préstamo con su activo o finalidad exacta
- saldo final exacto por subcuenta al cierre 2025 en todos los casos
- separar con precisión deuda puramente empresarial de deuda ligada a vehículos concretos
- entender qué es exactamente la cuenta `1700000029` y su entrada de **20.517,79 H** en 2025-07-29 (`Pago Fra. 8-1344, LUIS CONTRERAS S.L.`), porque podría ser nueva financiación, otra deuda distinta o una anomalía de clasificación a revisar

### Pero cuidado
Estos huecos ya no impiden una conclusión fuerte de nivel medio.

---

## 9. Qué se puede afirmar ya con bastante seguridad
- Chemie **reduce deuda real** en 2025
- no parece solo reclasificación
- la mejora viene de amortización ordinaria + cuota final fuerte + cancelaciones explícitas
- la caída de intereses encaja muy bien con esa reducción real del endeudamiento
- parte relevante del desapalancamiento parece ligada a **vehículos/activos financiados**, no solo a circulante abstracto

---

## 10. Conclusión ejecutiva
Si tuviera que resumir esta mini auditoría en una frase:

> **La mejora financiera de Chemie en 2025 se apoya en un desapalancamiento real y visible, especialmente por cierre/cancelación de varias financiaciones concretas, entre ellas una furgoneta y la Honda Africa, además de la amortización normal del resto de préstamos.**

Esto me parece un paso muy bueno, porque deja la mejora 2025 bastante menos abstracta y bastante más explicada.
