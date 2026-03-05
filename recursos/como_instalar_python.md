# Como instalar Python (o programar sin instalarlo)

No necesitas instalar nada para empezar a programar en Python. Esta guia te explica todas las opciones disponibles, desde las mas rapidas hasta las mas completas, para que elijas la que mejor se adapte a tu situacion.

---

## Resumen de opciones

| Opcion | Instalacion | Requiere internet | Nivel recomendado |
|--------|-------------|-------------------|-------------------|
| Replit | No | Si | Principiante |
| Google Colab | No | Si | Principiante |
| VS Code + Python | Si | Solo para instalar | Intermedio |
| Python solo (terminal) | Si | Solo para instalar | Cualquier nivel |

---

## Opcion 1 — Replit (sin instalar nada)

**Replit** es un editor de codigo que funciona directamente desde tu navegador web. No necesitas instalar nada en tu computadora.

### Como empezar

1. Abre tu navegador y ve a [replit.com](https://replit.com)
2. Haz clic en **Sign up** (registrarse)
3. Crea una cuenta gratuita con tu correo electronico o con tu cuenta de Google
4. Una vez dentro, haz clic en **+ Create Repl**
5. Selecciona **Python** como lenguaje
6. Escribe un nombre para tu proyecto y haz clic en **Create Repl**

### Como usar Replit

Veras tres secciones en la pantalla:

- **Izquierda:** el explorador de archivos
- **Centro:** el editor donde escribes tu codigo
- **Derecha:** la consola donde ves los resultados

Escribe tu codigo en el editor central y presiona el boton verde **Run** (o usa el atajo `Ctrl + Enter`) para ejecutarlo.

### Ventajas de Replit

- No necesitas instalar nada
- Puedes acceder a tu codigo desde cualquier dispositivo con internet
- Puedes compartir tu proyecto con un enlace
- Tiene una version gratuita con todo lo que necesitas para aprender

> **Tip:** Si cierras la pagina, tu codigo se guarda automaticamente. Puedes volver a el desde tu perfil en Replit.

---

## Opcion 2 — Google Colab (sin instalar nada)

**Google Colab** es una herramienta de Google que te permite escribir y ejecutar codigo Python en "cuadernos" (notebooks). Cada cuaderno tiene celdas de texto y celdas de codigo que puedes ejecutar por separado.

### Como empezar

1. Necesitas una cuenta de Google (Gmail)
2. Ve a [colab.research.google.com](https://colab.research.google.com)
3. Haz clic en **Nuevo cuaderno** (New notebook)
4. Se abrira un cuaderno en blanco con una celda de codigo lista para usar

### Como usar Google Colab

- Haz clic dentro de una celda de codigo y escribe tu programa
- Presiona `Shift + Enter` para ejecutar la celda y ver el resultado justo abajo
- Puedes agregar nuevas celdas con el boton **+ Codigo** o **+ Texto**
- Tu cuaderno se guarda automaticamente en Google Drive

```python
# Ejemplo: escribe esto en una celda y presiona Shift + Enter
print("Hola desde Google Colab")
```

### Ventajas de Google Colab

- No requiere instalacion
- Los cuadernos se guardan en tu Google Drive automaticamente
- Puedes combinar codigo, texto explicativo e imagenes en el mismo documento
- Ideal para tomar notas mientras aprendes

> **Tip:** Puedes abrir cualquier archivo `.ipynb` directamente desde Google Drive haciendo doble clic.

---

## Opcion 3 — Python instalado + VS Code (recomendado para trabajo serio)

Si quieres trabajar sin depender de internet, o quieres una experiencia mas completa como programadora, te recomendamos instalar **Python** y **VS Code** en tu computadora.

### Paso 1 — Instalar Python

#### En Windows

1. Ve a [python.org/downloads](https://www.python.org/downloads/)
2. Haz clic en el boton grande que dice **Download Python 3.x.x** (el numero puede variar; elige la version mas reciente)
3. Abre el archivo descargado (`.exe`)
4. **Muy importante:** antes de hacer clic en *Install Now*, marca la casilla que dice **"Add Python to PATH"** en la parte inferior del instalador

   > **Atencion:** Si no marcas esa casilla, Python no funcionara correctamente desde la terminal.

5. Haz clic en **Install Now**
6. Espera a que termine la instalacion y haz clic en **Close**

**Verificar la instalacion:**

Abre la aplicacion **Simbolo del sistema** (busca "cmd" en el menu Inicio) y escribe:

```
python --version
```

Deberia mostrarte algo como:

```
Python 3.12.4
```

Si ves eso, Python esta instalado correctamente.

> **Nota:** La documentacion oficial de Python para Windows esta disponible en [docs.python.org/dev/using/windows.html](https://docs.python.org/dev/using/windows.html). Ahi encontraras instrucciones detalladas sobre el lanzador de Python (`py`), variables de entorno, y configuraciones avanzadas.

#### En macOS

1. Ve a [python.org/downloads](https://www.python.org/downloads/)
2. Descarga el instalador para macOS (`.pkg`)
3. Abre el archivo y sigue los pasos del instalador
4. Al terminar, abre la aplicacion **Terminal** y escribe:

```
python3 --version
```

En macOS, el comando es `python3` (no `python`). Deberia mostrarte la version instalada.

#### En Linux

La mayoria de distribuciones de Linux ya incluyen Python 3. Verificalo abriendo una terminal y escribiendo:

```
python3 --version
```

Si no esta instalado, usa el gestor de paquetes de tu distribucion:

```
# Ubuntu / Debian
sudo apt install python3

# Fedora
sudo dnf install python3
```

---

### Paso 2 — Instalar VS Code

**Visual Studio Code** (VS Code) es un editor de codigo gratuito, liviano y muy popular. Esta disponible para Windows, macOS y Linux.

1. Ve a [code.visualstudio.com](https://code.visualstudio.com)
2. Haz clic en el boton de descarga para tu sistema operativo
3. Abre el instalador y sigue los pasos (puedes dejar todas las opciones por defecto)
4. Al terminar, abre VS Code

---

### Paso 3 — Instalar la extension de Python en VS Code

VS Code necesita una extension para trabajar con Python. Es facil de instalar:

1. Abre VS Code
2. Haz clic en el icono de extensiones en la barra lateral izquierda (parece cuatro cuadraditos)
3. En el buscador, escribe: `Python`
4. El primer resultado deberia ser la extension **Python** de **Microsoft**
5. Haz clic en **Install** (Instalar)

Una vez instalada, VS Code detectara automaticamente la version de Python que instalaste.

---

### Paso 4 — Crear y ejecutar tu primer archivo

1. En VS Code, ve a **File > New File** (Archivo > Nuevo archivo)
2. Guarda el archivo con el nombre `hola.py` (el `.py` le dice a VS Code que es codigo Python)
3. Escribe tu programa:

```python
print("Hola, mundo")
```

4. Presiona `Ctrl + F5` (o haz clic derecho en el editor y selecciona **Run Python File in Terminal**)
5. En la parte inferior de la pantalla aparecera una terminal con el resultado:

```
Hola, mundo
```

> **Tip:** Puedes tambien abrir una terminal en VS Code con el menu **Terminal > New Terminal** y ejecutar tu archivo escribiendo `python hola.py` (Windows) o `python3 hola.py` (macOS/Linux).

---

## Opcion 4 — Python solo desde la terminal (sin editor)

Si ya tienes Python instalado, puedes usarlo directamente desde la terminal sin necesidad de un editor como VS Code. Esta opcion es util para probar cosas rapidamente.

### Modo interactivo (REPL)

Abre la terminal y escribe `python` (Windows) o `python3` (macOS/Linux). Veras algo como:

```
Python 3.12.4 (main, ...)
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

El simbolo `>>>` significa que Python esta listo para recibir instrucciones. Puedes escribir codigo directamente:

```python
>>> print("Hola")
Hola
>>> 2 + 2
4
```

Para salir del modo interactivo, escribe `exit()` o presiona `Ctrl + Z` (Windows) / `Ctrl + D` (macOS/Linux).

### Ejecutar un archivo desde la terminal

Si tienes un archivo `programa.py`, ejecutalo con:

```
python programa.py       # Windows
python3 programa.py      # macOS / Linux
```

---

## Que opcion elegir

| Situacion | Opcion recomendada |
|-----------|-------------------|
| Quiero empezar ahora mismo, sin instalar nada | Replit |
| Tengo cuenta de Google y quiero tomar notas junto al codigo | Google Colab |
| Quiero trabajar sin internet y tener un entorno profesional | VS Code + Python |
| Solo quiero probar cosas rapido desde la terminal | Python solo (REPL) |

---

## Preguntas frecuentes

**¿Que version de Python debo instalar?**
Siempre la mas reciente. Al momento de escribir esta guia, Python 3.12 es una buena opcion. Evita Python 2, que ya no tiene soporte oficial.

**¿Puedo tener Python 2 y Python 3 al mismo tiempo?**
Si, pero no es necesario para aprender. Instala solo Python 3.

**Instale Python pero el comando no funciona en la terminal.**
En Windows, probablemente no marcaste la casilla "Add Python to PATH" durante la instalacion. La solucion mas facil es desinstalar Python y volver a instalarlo marcando esa opcion.

**¿VS Code es gratis?**
Si, completamente. Es un editor de codigo abierto mantenido por Microsoft.

**¿Puedo usar otro editor en lugar de VS Code?**
Si. Otras opciones populares son PyCharm (mas completo, pero mas pesado), Thonny (muy simple, ideal para principiantes) y IDLE (viene incluido con Python). VS Code es nuestra recomendacion por su equilibrio entre simplicidad y funcionalidad.

---

## Siguiente paso

Una vez que tengas tu entorno listo, regresa a la guia de introduccion y escribe tu primer programa.

[Empezar con la Guia 01 — Introduccion a Python](../guias/01_introduccion_a_python.md)
