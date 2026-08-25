# Castellano simplificado

Una aplicación sencilla que transforma texto en español a una versión simplificada, reduciendo el número de letras del abecedario.

## ¿Qué hace?

La aplicación recibe un texto escrito en español y aplica una serie de reglas para intentar que el texto pueda ser leído igual, pero reduciendo las letras utilizadas a las siguientes:
A, B, D, E, F, G, I, J, K, L, M, N, O, P, K, R, S, T, U, Z

Además, se busca que cada letra corresponda únicamente con un fonema, por lo que:
- la letra 'g' tendrá siempre el fonema /g/ y nunca el /j/
- el fonema /ll/ es reemplazado por /i/, al venir, salvo en extranjerismos y nombres propios, siempre precedido por vocal, y ser este el sonido más parecido que he encontrado
- El fonema /ñ/ es reemplazado por /ni/, al venir, salvo en nombres propios, siempre precedido por vocal, y ser este el sonido más parecido que he encontrado

Por ejemplo:

```text
Texto original:
En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor.

Texto simplificado:
en un lugar de la manksa, de kuio nombre no kiero akordarme, no a mukso tiempo ke bibía un idalgo de los de lanza en astiiero, adarga antigua, rocín flako i galgo korredor.
```

> El objetivo del proyecto es experimentar con la simplificación del español y la eliminación de ciertas letras manteniendo fonemas iguales o similares. La idea del proyecto es más bien humorística y se centra en la premisa de que "sobran letras" y que cada letra debe corresponder a un único sonido, obviando la filología y la evolución cultural por la cuál se ha llegado al vocabulario castellano actual.

## Uso

### Windows

Puedes utilizar directamente el ejecutable:

```text
trad_inutil.exe
```

No es necesario tener Python instalado.

También puedes ejecutar el programa desde una terminal:

```bash
trad_inutil.exe
```

## Ejecutar desde Python

Si quieres ejecutar el código fuente, necesitas tener Python instalado.

Clona el repositorio y ejecuta:

```bash
trad_inutil.py
```

## Compilar el ejecutable

El ejecutable se ha generado utilizando [PyInstaller](https://pyinstaller.org/).

Para generar un único ejecutable:

```bash
pyinstaller --onefile trad_inutil.py
```

El ejecutable resultante se encontrará en:

```text
dist/trad_inutil.exe
```

## Estructura del proyecto

```text
.
├── trad_inutil.py       # Código fuente
├── trad_inutil.exe      # Ejecutable para Windows
└── README.md         # Documentación
```

## Limitaciones

La simplificación se basa en reglas definidas por el programa, por lo que el resultado no siempre será perfecto. El texto devuelto por el programa estará completamente en minúsculas. No he estudiado filología ni me considero experto en lengua castellana, por lo que las reglas utilizadas para este castellano simplificado pueden no ser las más adecuadas.

## Licencia

Este proyecto está disponible bajo la licencia MIT.
