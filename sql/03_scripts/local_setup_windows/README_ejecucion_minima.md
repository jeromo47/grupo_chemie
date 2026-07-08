# EJECUCION MINIMA EN EL PC WINDOWS

## Archivos de esta carpeta
- `test_conexion.py`
- `descubre.py`
- `config.template.json`

## Qué haces tú

### 1. Lleva esta carpeta al PC Windows
Cópiala por AnyDesk, red, Drive o USB a:

`C:\grupo_chemie\scripts\`

Si prefieres, también puede vivir toda junta en otra carpeta temporal, pero así queda más ordenado.

### 2. Crea tu `config.json`
- duplica `config.template.json`
- renómbralo a `config.json`
- rellena solo:
  - `password`
  - `fbclient_dll` si tu ruta real cambia
  - `charset_conexion` déjalo de momento como `PENDIENTE`

## 3. Ejecuta primero el test
En CMD o PowerShell:

```bat
C:\grupo_chemie\venv\Scripts\python.exe C:\grupo_chemie\scripts\test_conexion.py
```

### Si sale bien
Debes ver 3 líneas `OK` y al final:

`CONEXION VERIFICADA EN LAS 3 BASES`

### Si falla
Pásame el error literal.

## 4. Si el test va bien, ejecuta descubre

```bat
C:\grupo_chemie\venv\Scripts\python.exe C:\grupo_chemie\scripts\descubre.py
```

## 5. Qué te tiene que generar
Dentro de la carpeta `esquema` junto a los scripts:

- `esquema_CHEMIE.csv`
- `esquema_ACI.csv`
- `esquema_ECOCLEAN.csv`
- `charset_CHEMIE.txt`
- `charset_ACI.txt`
- `charset_ECOCLEAN.txt`

## 6. Qué me mandas luego
Me pasas esos 6 archivos y yo te digo:
- charset correcto definitivo
- si las 3 bases tienen la misma estructura o no
- qué tablas/columnas quedan validadas para la fase B
