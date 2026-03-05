# Guia 07 — Entrada y salida de archivos

Hasta ahora toda la informacion de tus programas desaparece cuando los cierras. Si agregas contactos a tu agenda o calificaciones a tu lista, la proxima vez que ejecutes el programa tendras que volver a ingresarlos.

Para que un programa **recuerde informacion entre ejecuciones**, necesita guardarla en un archivo. En esta guia aprenderas a leer y escribir archivos de texto desde Python.

---

## Abrir un archivo con `open()`

La funcion `open()` abre un archivo y devuelve un objeto con el que puedes leerlo o escribirlo:

```python
archivo = open("nombre_del_archivo.txt", "modo")
```

Los modos mas comunes son:

| Modo | Significado | Que pasa si el archivo no existe |
|---|---|---|
| `"r"` | Leer *(read)* | Error `FileNotFoundError` |
| `"w"` | Escribir *(write)*, borra el contenido anterior | Lo crea |
| `"a"` | Agregar al final *(append)* | Lo crea |
| `"r+"` | Leer y escribir | Error si no existe |

Siempre que abres un archivo debes **cerrarlo** cuando termines:

```python
archivo = open("notas.txt", "r")
contenido = archivo.read()
archivo.close()
```

---

## La forma recomendada: `with`

Usar `with` es mejor practica porque **cierra el archivo automaticamente** aunque ocurra un error:

```python
with open("notas.txt", "r") as archivo:
    contenido = archivo.read()

# Aqui el archivo ya esta cerrado
print(contenido)
```

A partir de ahora usaremos siempre esta forma.

---

## Leer archivos

### Leer todo el contenido de una vez

```python
with open("notas.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
```

### Leer linea por linea

```python
with open("notas.txt", "r") as archivo:
    for linea in archivo:
        print(linea)
```

Cada linea incluye el caracter de salto de linea `\n` al final. Para eliminarlo usa `.strip()`:

```python
with open("notas.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())
```

### Leer todas las lineas en una lista

```python
with open("notas.txt", "r") as archivo:
    lineas = archivo.readlines()

print(lineas)       # lista de strings, cada uno es una linea
print(lineas[0])    # primera linea
```

---

## Escribir archivos

### Crear o sobreescribir un archivo

```python
with open("notas.txt", "w") as archivo:
    archivo.write("Primera linea\n")
    archivo.write("Segunda linea\n")
    archivo.write("Tercera linea\n")
```

El modo `"w"` **borra todo el contenido anterior** si el archivo ya existe. Ten cuidado con esto.

### Agregar contenido sin borrar lo anterior

```python
with open("notas.txt", "a") as archivo:
    archivo.write("Esta linea se agrega al final\n")
```

### Escribir varias lineas con `writelines()`

```python
lineas = ["Ana\n", "Lucia\n", "Valeria\n"]

with open("participantes.txt", "w") as archivo:
    archivo.writelines(lineas)
```

---

## Trabajar con rutas de archivos

Por defecto Python busca el archivo en la misma carpeta donde esta tu programa. Puedes especificar rutas relativas o absolutas:

```python
# Misma carpeta
open("datos.txt", "r")

# Subcarpeta
open("datos/participantes.txt", "r")

# Carpeta superior
open("../config.txt", "r")
```

Para evitar problemas con rutas en diferentes sistemas operativos, puedes usar el modulo `os.path`:

```python
import os

ruta = os.path.join("datos", "participantes.txt")
with open(ruta, "r") as archivo:
    contenido = archivo.read()
```

---

## Manejar el error cuando el archivo no existe

Si intentas leer un archivo que no existe, Python lanza un `FileNotFoundError`. Puedes manejarlo con `try` y `except`:

```python
try:
    with open("notas.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no existe todavia.")
```

`try / except` es la forma de Python para manejar errores sin que el programa se detenga. Encierra en `try` el codigo que podria fallar y en `except` lo que debe pasar si falla.

---

## Trabajar con archivos CSV

Los archivos **CSV** *(Comma-Separated Values)* son archivos de texto donde cada linea es un registro y los valores estan separados por comas. Son muy usados para guardar datos tabulares (como una hoja de calculo).

```
nombre,edad,ciudad
Ana,15,Monterrey
Lucia,14,Guadalajara
Valeria,16,CDMX
```

Python tiene el modulo `csv` para leerlos y escribirlos facilmente:

### Leer un CSV

```python
import csv

with open("participantes.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(f"{fila['nombre']} — {fila['ciudad']}")
```

`DictReader` lee cada linea como un diccionario usando la primera fila como claves.

### Escribir un CSV

```python
import csv

participantes = [
    {"nombre": "Ana",     "edad": 15, "ciudad": "Monterrey"},
    {"nombre": "Lucia",   "edad": 14, "ciudad": "Guadalajara"},
    {"nombre": "Valeria", "edad": 16, "ciudad": "CDMX"},
]

with open("participantes.csv", "w", newline="") as archivo:
    campos = ["nombre", "edad", "ciudad"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)

    escritor.writeheader()   # escribe la fila de encabezados
    escritor.writerows(participantes)

print("Archivo guardado.")
```

---

## Verificar si un archivo existe antes de abrirlo

```python
import os

if os.path.exists("notas.txt"):
    with open("notas.txt", "r") as archivo:
        print(archivo.read())
else:
    print("El archivo no existe.")
```

---

## Ejemplo completo: diario personal

Este programa guarda entradas en un archivo de texto y permite releerlas:

```python
import os
from datetime import date

ARCHIVO = "diario.txt"

def nueva_entrada():
    hoy = date.today().strftime("%d/%m/%Y")
    texto = input("Escribe tu entrada de hoy:\n> ")

    with open(ARCHIVO, "a") as archivo:
        archivo.write(f"\n[{hoy}]\n{texto}\n")

    print("Entrada guardada.")

def leer_diario():
    if not os.path.exists(ARCHIVO):
        print("Tu diario esta vacio. Escribe tu primera entrada.")
        return

    with open(ARCHIVO, "r") as archivo:
        print("\n--- Mi diario ---")
        print(archivo.read())

def menu():
    while True:
        print("\n1. Nueva entrada")
        print("2. Leer diario")
        print("3. Salir")

        opcion = input("Elige una opcion: ")

        if opcion == "1":
            nueva_entrada()
        elif opcion == "2":
            leer_diario()
        elif opcion == "3":
            print("Hasta luego!")
            break
        else:
            print("Opcion no valida.")

menu()
```

---

## Ejercicio de esta guia

Crea un programa de **lista de tareas** que guarde las tareas en un archivo `tareas.txt`:

1. `agregar_tarea(tarea)` — agrega una tarea al archivo
2. `ver_tareas()` — muestra todas las tareas numeradas
3. `limpiar_tareas()` — borra todas las tareas (pide confirmacion antes)
4. Un menu que permita usar las tres opciones

Ejemplo del archivo `tareas.txt`:
```
Estudiar para el examen de matematicas
Terminar el prototipo de la app
Preparar presentacion de Technovation
```

**Reto extra:** Agrega la posibilidad de marcar una tarea como completada agregando `[x]` al inicio de la linea.

**Reto avanzado:** Guarda las tareas en un archivo CSV con columnas `tarea` y `completada`, y muestra las pendientes y completadas por separado.

---

## Resumen

| Concepto | Que aprendiste |
|---|---|
| `open(archivo, modo)` | Abre un archivo para leerlo o escribirlo |
| `with open(...) as f` | Forma segura de abrir archivos; los cierra automaticamente |
| `"r"`, `"w"`, `"a"` | Modos de lectura, escritura y agregar |
| `.read()` | Lee todo el contenido como un string |
| `.readlines()` | Lee todas las lineas en una lista |
| `.write()` | Escribe un string en el archivo |
| `.strip()` | Elimina espacios y saltos de linea al inicio y final |
| `try / except` | Maneja errores sin detener el programa |
| Modulo `csv` | Lee y escribe archivos de valores separados por comas |
| `os.path.exists()` | Verifica si un archivo existe |

---

## Que sigue

En la ultima guia aprenderas sobre **modulos y librerias**: como usar el codigo que otras personas ya escribieron para agregar funcionalidades poderosas a tus programas sin empezar desde cero.

[Anterior: 06 — Listas y diccionarios](06_listas_y_diccionarios.md) | [Siguiente: 08 — Modulos y librerias](08_modulos_y_librerias.md)
