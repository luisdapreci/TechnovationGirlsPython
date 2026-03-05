# Guia 08 — Modulos y librerias

Una de las razones por las que Python es tan popular es su ecosistema: miles de programadoras y programadores han escrito codigo que puedes usar libremente en tus proyectos. No tienes que reinventar la rueda.

En esta guia aprenderas a usar **modulos** (archivos de Python con funciones listas para usar) y **librerias externas** (paquetes que se instalan por separado).

---

## Que es un modulo

Un modulo es simplemente un archivo `.py` con funciones, variables y clases que puedes importar en tu programa. Python viene con muchos modulos incluidos — se llaman la **biblioteca estandar**.

---

## Importar un modulo con `import`

```python
import math

resultado = math.sqrt(16)
print(resultado)  # 4.0
```

Al escribir `import math`, le dices a Python que cargue el modulo `math`. Despues accedes a sus funciones con `math.nombre_funcion()`.

### Importar solo lo que necesitas con `from`

Si solo necesitas una funcion especifica, puedes importarla directamente:

```python
from math import sqrt, pi

print(sqrt(25))   # 5.0
print(pi)         # 3.141592653589793
```

Asi no necesitas escribir `math.` cada vez.

### Importar con alias

Si el nombre del modulo es largo, puedes darle un alias con `as`:

```python
import random as r

numero = r.randint(1, 10)
print(numero)
```

---

## Modulos de la biblioteca estandar

### `math` — operaciones matematicas

```python
import math

print(math.sqrt(144))      # 12.0 — raiz cuadrada
print(math.pow(2, 10))     # 1024.0 — potencia
print(math.floor(3.9))     # 3 — redondeo hacia abajo
print(math.ceil(3.1))      # 4 — redondeo hacia arriba
print(math.pi)             # 3.141592653589793
print(math.abs(-7))        # Error: usa abs() directamente
print(abs(-7))             # 7 — abs() es una funcion incorporada
```

### `random` — numeros y selecciones aleatorias

```python
import random

print(random.randint(1, 6))          # numero entero entre 1 y 6
print(random.random())               # decimal entre 0.0 y 1.0
print(random.uniform(1.0, 5.0))     # decimal entre 1.0 y 5.0

frutas = ["manzana", "pera", "uva", "mango"]
print(random.choice(frutas))         # elige un elemento al azar
random.shuffle(frutas)               # mezcla la lista en su lugar
print(frutas)
print(random.sample(frutas, 2))      # elige 2 elementos sin repetir
```

### `datetime` — fechas y horas

```python
from datetime import date, datetime

hoy = date.today()
print(hoy)                           # 2025-03-05
print(hoy.year)                      # 2025
print(hoy.month)                     # 3
print(hoy.day)                       # 5

ahora = datetime.now()
print(ahora)                         # 2025-03-05 14:32:10.123456

# Formatear fechas
print(hoy.strftime("%d/%m/%Y"))      # 05/03/2025
print(ahora.strftime("%H:%M"))       # 14:32
```

### `os` — interactuar con el sistema operativo

```python
import os

print(os.getcwd())                   # carpeta actual
print(os.listdir("."))               # archivos en la carpeta actual
os.makedirs("nueva_carpeta", exist_ok=True)  # crear carpeta
print(os.path.exists("datos.txt"))   # verificar si existe un archivo
print(os.path.join("carpeta", "archivo.txt"))  # construir rutas
```

### `string` y metodos de texto

Python tiene metodos de string integrados que no requieren importar nada:

```python
texto = "  Hola, Technovation Girls!  "

print(texto.strip())          # elimina espacios al inicio y final
print(texto.lower())          # todo en minusculas
print(texto.upper())          # todo en mayusculas
print(texto.replace("Hola", "Bienvenida"))
print(texto.split(","))       # divide en lista por separador
print("Girls" in texto)       # True — verifica si contiene el texto
print(texto.startswith("  Hola"))  # True
print(texto.count("l"))       # 3 — cuantas veces aparece "l"
```

---

## Instalar librerias externas con `pip`

La biblioteca estandar es muy completa, pero hay librerias externas que agregan funcionalidades especializadas. Se instalan con `pip`, el gestor de paquetes de Python.

Desde la terminal:

```bash
pip install nombre-de-la-libreria
```

### Librerias utiles para proyectos Technovation

| Libreria | Para que sirve | Instalacion |
|---|---|---|
| `requests` | Consumir APIs y hacer peticiones web | `pip install requests` |
| `flask` | Crear aplicaciones web | `pip install flask` |
| `pandas` | Analizar y manipular datos tabulares | `pip install pandas` |
| `matplotlib` | Crear graficas y visualizaciones | `pip install matplotlib` |
| `pillow` | Manipular imagenes | `pip install pillow` |
| `pygame` | Crear juegos 2D | `pip install pygame` |

---

## Ejemplo: consumir una API con `requests`

Una **API** es una forma de pedirle datos a otro servicio a traves de internet. Por ejemplo, puedes pedirle a una API el clima de una ciudad, datos de paises, o informacion de cualquier tema.

```python
import requests

respuesta = requests.get("https://restcountries.com/v3.1/name/mexico")

if respuesta.status_code == 200:
    datos = respuesta.json()
    pais = datos[0]
    print(f"Pais: {pais['name']['common']}")
    print(f"Capital: {pais['capital'][0]}")
    print(f"Poblacion: {pais['population']:,}")
else:
    print(f"Error: {respuesta.status_code}")
```

`.json()` convierte la respuesta en un diccionario de Python que puedes recorrer normalmente.

---

## Crear tu propio modulo

Puedes organizar tu codigo en modulos propios. Simplemente crea un archivo `.py` con las funciones que quieras reutilizar:

**`utilidades.py`**
```python
def saludar(nombre):
    return f"Hola, {nombre}!"

def es_par(numero):
    return numero % 2 == 0

PI_APROX = 3.14159
```

**`mi_programa.py`** (en la misma carpeta)
```python
import utilidades

print(utilidades.saludar("Sofia"))
print(utilidades.es_par(8))
print(utilidades.PI_APROX)
```

O usando `from`:

```python
from utilidades import saludar, es_par

print(saludar("Ana"))
print(es_par(7))
```

Dividir tu codigo en modulos hace que cada archivo sea mas corto y facil de mantener. En proyectos grandes esto es esencial.

---

## Ejemplo completo: generador de contrasenas

Este programa usa `random` y `string` para crear contrasenas seguras:

```python
import random
import string

def generar_contrasena(longitud=12, incluir_simbolos=True):
    letras = string.ascii_letters    # a-z A-Z
    numeros = string.digits          # 0-9
    simbolos = string.punctuation    # !@#$%...

    if incluir_simbolos:
        caracteres = letras + numeros + simbolos
    else:
        caracteres = letras + numeros

    contrasena = "".join(random.choices(caracteres, k=longitud))
    return contrasena

def evaluar_fortaleza(contrasena):
    tiene_mayuscula = any(c.isupper() for c in contrasena)
    tiene_minuscula = any(c.islower() for c in contrasena)
    tiene_numero = any(c.isdigit() for c in contrasena)
    tiene_simbolo = any(c in string.punctuation for c in contrasena)

    puntaje = sum([tiene_mayuscula, tiene_minuscula, tiene_numero, tiene_simbolo])

    if puntaje == 4:
        return "Muy fuerte"
    elif puntaje == 3:
        return "Fuerte"
    elif puntaje == 2:
        return "Media"
    else:
        return "Debil"

# Programa principal
print("--- Generador de contrasenas ---\n")

for i in range(5):
    contrasena = generar_contrasena(longitud=16)
    fortaleza = evaluar_fortaleza(contrasena)
    print(f"{contrasena}  ({fortaleza})")

print("\nPuedes copiar cualquiera de estas contrasenas.")
```

---

## Ejercicio de esta guia

Crea un programa que use al menos **tres modulos diferentes** para construir una pequeña herramienta util. Algunas ideas:

- **Generador de quiz aleatorio**: carga preguntas de un archivo CSV (`csv`), las mezcla (`random`) y registra el resultado con fecha (`datetime`)
- **Resumen del dia**: muestra la fecha actual (`datetime`), lista los archivos de una carpeta (`os`) y lee notas guardadas (`open`)
- **Conversor de unidades**: usa `math` para calcular conversiones y guarda el historial en un archivo

**Reto extra:** Publica tu herramienta como un modulo propio dividiendola en al menos dos archivos `.py`.

---

## Resumen

| Concepto | Que aprendiste |
|---|---|
| `import modulo` | Importa un modulo completo |
| `from modulo import func` | Importa solo lo que necesitas |
| `import modulo as alias` | Importa con un nombre mas corto |
| Biblioteca estandar | Modulos incluidos con Python: `math`, `random`, `datetime`, `os`, `csv` |
| `pip install` | Instala librerias externas desde la terminal |
| `requests` | Libreria para consumir APIs web |
| Modulo propio | Archivo `.py` con funciones reutilizables que puedes importar |

---

## Felicidades

Completaste las ocho guias basicas de Python. Ahora tienes las herramientas fundamentales para:

- Escribir programas que toman decisiones y se repiten
- Organizar tu codigo en funciones y modulos
- Guardar y leer informacion de archivos
- Usar librerias para no empezar desde cero

El siguiente paso es poner todo esto en practica. Revisa la carpeta `tutoriales/` para construir proyectos completos, o la carpeta `ejercicios/` para seguir practicando conceptos especificos.

Sigue escribiendo codigo. Cada programa que construyes, aunque sea pequeno, te hace mejor programadora.

---

[Anterior: 07 — Entrada y salida](07_entrada_y_salida.md) | [Siguiente: 09 — Clases y Objetos](09_clases_y_objetos.md)
