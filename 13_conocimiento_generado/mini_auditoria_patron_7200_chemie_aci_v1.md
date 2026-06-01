# Mini auditoría - Patrón 7.200 € Chemie / ACI v1

## Objetivo
Aclarar la naturaleza del patrón recurrente detectado entre **Chemie** y **ACI / Almeriense** por importe de **7.200 € anuales** en 2024 y 2025.

---

## Fuente principal
- `/home/jero/cloud/02_proyectos/grupo_familiar/00_inbox/2026-05-22_paquete_informe_consultoria_grupo_chemie_2024_2025/descomprimido/02_margen_clientes_proveedores_grupo.txt`
- `/home/jero/cloud/02_proyectos/grupo_familiar/00_inbox/2026-05-22_paquete_informe_consultoria_grupo_chemie_2024_2025/descomprimido/04_pyg_patrimonio_grupo.txt`

---

## 1. Hallazgo principal
El patrón de **7.200 €** entre Chemie y ACI ya no parece una cifra genérica sin contexto.

La evidencia visible apunta con bastante fuerza a que se trata de un **flujo periódico, trimestral y estable**, compuesto por:
- **4 facturas al año**
- de **1.800 €** cada una
- registradas en la cuenta **6210000000**
- tanto en **2024** como en **2025**

---

## 2. Evidencia directa encontrada
### En `02_margen_clientes_proveedores_grupo.txt`
Aparece:
- `ALMERIENSE COMPTOS. INDUSTRIALES, S.L.`
- **4 movimientos**
- **7.200,00 €** en **2024**
- **4 movimientos**
- **7.200,00 €** en **2025**

Y simétricamente, en el bloque de ventas de ACI, aparece **GRUPO CHEMIE LA JUAIDA, S.L.** con:
- **4 movimientos**
- **7.200,00 €** en **2024**
- **4 movimientos**
- **7.200,00 €** en **2025**

### Esto confirma
Que no es una suma inferida de forma indirecta, sino un flujo explícito y bilateralmente visible:
- para Chemie = compra/gasto
- para ACI = venta/ingreso

---

## 3. Despiece del patrón
### En `04_pyg_patrimonio_grupo.txt`
Aparecen movimientos repetidos en **Chemie**:

#### 2024
- **2024-03-31** -> `Fra. nº 1-240042, ALMERIENSE COMPTOS. IND` -> **1.800,00 €**
- **2024-06-30** -> `Fra. nº 1-240082, ALMERIENSE COMPTOS. IND` -> **1.800,00 €**
- **2024-09-30** -> `Fra. nº 1-240123, ALMERIENSE COMPTOS. IND` -> **1.800,00 €**
- **2024-12-30** -> `Fra. nº 1-240168, ALMERIENSE COMPTOS. IND` -> **1.800,00 €**

#### 2025
- **2025-03-31** -> `Fra. nº 1-250031, ALMERIENSE COMPTOS. IND` -> **1.800,00 €**
- **2025-06-30** -> `Fra. nº 1-250067, ALMERIENSE COMPTOS. IND` -> **1.800,00 €**
- y el patrón del paquete indica otras dos trimestrales hasta completar **4 movimientos / 7.200 €** en 2025

### Además
Tras varias de esas facturas aparecen apuntes de **pago** en cuenta `4000004235`, lo que refuerza que el circuito es limpio:
- factura
- registro del gasto
- pago posterior

---

## 4. Qué significa la cuenta 6210000000
Este punto es clave.

Las cuatro facturas trimestrales de 1.800 € están registradas en **6210000000**.

En el PGC español, el grupo **621** suele asociarse a:
- **arrendamientos y cánones**

### Lectura prudente pero fuerte
Aunque el extracto muestra `<null>` en el título concreto de esa subcuenta, la codificación **621** hace muy verosímil que el patrón 7.200 € responda a:
- alquiler
- canon
- cesión de uso
- o algún coste periódico equiparable

### Lo que ya no parece
Con esta evidencia, **ya no parece una compra ordinaria de mercancía**.
No está pasando por 600/601 como compra troncal, sino por una cuenta con mucha pinta de gasto periódico de uso/estructura.

---

## 5. Interpretación más probable
### Mi mejor lectura ahora mismo
ACI parece facturar a Chemie un **coste estructural recurrente** de:
- **1.800 € por trimestre**
- **7.200 € al año**

### Naturaleza más probable
Lo más probable es que este flujo corresponda a una de estas figuras:
1. **arrendamiento**
2. **cesión de nave, espacio o instalaciones**
3. **canon interno de uso**
4. otro servicio estructural muy estable de naturaleza asimilable

### Hipótesis más fuerte
La hipótesis que mejor encaja es **uso de inmueble, espacio o infraestructura** de ACI por parte de Chemie.

Y eso encaja muy bien con todo el resto del dossier, donde ACI ya venía saliendo como pieza:
- patrimonial
- logística
- soporte
- con activos inmobiliarios reales

---

## 6. Lo que aporta esto a la lectura del núcleo
Este hallazgo mejora mucho la comprensión de ACI.

### Antes
ACI ya parecía:
- sociedad mixta
- con patrimonio
- con soporte al núcleo

### Ahora
Además aparece con una función económica mucho más concreta:
- **vehículo que cobra a Chemie un flujo periódico estable vinculado probablemente al uso de estructura o espacio**

### Traducción clara
ACI no solo acompaña al núcleo por contexto familiar o por coexistencia documental.
Parece participar en la **infraestructura material/económica real** que utiliza Chemie.

---

## 7. Qué NO sugiere este patrón
No sugiere, con lo visible:
- un gran desorden intersocietario
- un saldo oculto enorme
- una financiación cruzada opaca
- ni una relación contable caótica

Al contrario, lo que transmite es:
- periodicidad
n- regularidad
- importe estable
- trazabilidad
- y pago normalizado

---

## 8. Riesgo o alerta
### Tipo de alerta
No roja.
Ni siquiera me parece especialmente naranja.

La llamaría una **alerta amarilla de interpretación estructural**.

### Por qué importa
Porque ayuda a responder algo muy valioso:
> **qué hace exactamente ACI para Chemie dentro del sistema**

### Qué revisión fina quedaría abierta
Solo si más adelante compensa, quedaría por confirmar documentalmente si esos 1.800 €/trimestre responden a:
- una nave concreta
- una cesión parcial de uso
- un alquiler interno formalizado
- o un servicio estructural distinto

---

## 9. Qué se puede afirmar ya con bastante seguridad
- el patrón de **7.200 €** existe en **2024** y **2025**
- se compone de **4 facturas trimestrales de 1.800 €**
- el gasto se registra en **6210000000**
- ACI lo refleja como ingreso/venta a Chemie
- el circuito parece **regular y pagado**
- la naturaleza más probable es **arrendaticia o de cesión estructural**, no compra ordinaria de mercancía

---

## 10. Conclusión ejecutiva
Si tuviera que resumir esta mini auditoría en una frase:

> **El patrón Chemie-ACI de 7.200 € anuales parece responder a un flujo trimestral estable de naturaleza muy probablemente arrendaticia o de cesión estructural, lo que refuerza el papel de ACI como sociedad soporte-patrimonial real del núcleo.**

Esto me parece una pieza muy buena porque convierte una intuición general sobre ACI en una función económica bastante concreta.

---

## 11. Siguiente paso recomendado
Dos caminos útiles:

1. intentar vincular este flujo con una **nave/espacio concreto** del mapa patrimonial
2. o seguir con la **explicación fina de la mejora financiera 2025 de Chemie**

### Mi recomendación real
Yo haría primero el cruce con patrimonio/sedes.
Porque puede cerrar muy elegantemente la función exacta de ACI dentro del núcleo.
