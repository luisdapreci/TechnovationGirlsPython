# Proyecto Final — Nivel Basico: Sistema de Recetas Favoritas

Felicitaciones por llegar al final del Nivel Basico. Has aprendido muchisimo:
variables, condicionales, ciclos, funciones, listas, diccionarios, archivos y modulos.

Este proyecto integra **todos esos conceptos** en un solo programa: un sistema
para guardar y gestionar tus recetas favoritas.

---

## Que vas a construir

Un programa de consola que permite:

1. **Agregar** una receta con nombre, ingredientes, tiempo de preparacion y dificultad
2. **Ver** todas las recetas guardadas
3. **Buscar** recetas por nivel de dificultad
4. **Recibir** una sugerencia aleatoria de que cocinar
5. **Ver estadisticas** del recetario (total, promedio de tiempo, etc.)
6. **Guardar** el recetario en un archivo CSV
7. **Cargar** el recetario desde ese archivo al iniciar el programa

---

## Conceptos que practica este ejercicio

| Concepto | Guia | Donde aparece |
|----------|------|---------------|
| `print()` e `input()` | 01, 02 | Menu, agregar receta, mostrar resultados |
| Variables y tipos de datos | 02 | Nombre (str), tiempo (int), dificultad (str) |
| f-strings | 02 | Mostrar informacion de cada receta |
| Condicionales `if/elif/else` | 03 | Validar dificultad, opciones del menu |
| Ciclo `while` | 04 | Menu principal, validacion de entrada |
| Ciclo `for` con `enumerate()` | 04, 06 | Mostrar lista de recetas numeradas |
| Funciones con `def` y `return` | 05 | Una funcion por cada operacion |
| Listas | 06 | Almacenar el conjunto de recetas |
| Diccionarios | 06 | Representar cada receta individual |
| Lista de diccionarios | 06 | La estructura principal del recetario |
| `open()`, `with`, modos de archivo | 07 | Guardar y cargar desde CSV |
| Modulo `csv` | 07, 08 | Leer y escribir el archivo CSV |
| `try/except` | 07 | Manejar que el archivo no exista |
| Modulo `random` | 08 | Sugerencia aleatoria de receta |
| Modulo `datetime` | 08 | Mostrar la fecha al iniciar el programa |
| `import` | 08 | Importar los modulos necesarios |

---

## Instrucciones

### Paso 0 — Preparacion

Abre el archivo `nivel_basico_proyecto_final.py`. Esta el codigo de arranque con
todas las secciones marcadas con `# TODO:`. Tu tarea es completar cada seccion.

Lee los comentarios con cuidado: te dicen exactamente que debe hacer cada funcion.

### Paso 1 — Importaciones y variables globales

Al principio del archivo importa los modulos necesarios:

```python
import csv
import random
from datetime import datetime
```

Luego crea:
- Una lista vacia llamada `recetas` donde se guardaran todas las recetas
- Una constante `ARCHIVO_CSV` con el nombre del archivo: `'mis_recetas.csv'`

### Paso 2 — Funcion `mostrar_bienvenida()`

Debe imprimir un encabezado con:
- El titulo del programa
- La fecha de hoy usando `datetime.now()`

Ejemplo de salida esperada:
```
===================================
   Sistema de Recetas Favoritas
   Hoy es: viernes, 07 marzo 2026
===================================
```

> **Tip:** Usa `datetime.now().strftime('%A, %d %B %Y')` para formatear la fecha.

### Paso 3 — Funcion `agregar_receta()`

Debe pedir al usuario:
1. Nombre de la receta (`str`)
2. Ingredientes separados por coma (`str`)
3. Tiempo de preparacion en minutos (`int`) — valida que sea un numero positivo
4. Dificultad: solo acepta `'facil'`, `'media'` o `'dificil'` — repite la pregunta si ingresa otro valor

Luego crea un diccionario con esos datos y agregalo a la lista `recetas`.

Estructura del diccionario:
```python
{
    'nombre': ...,
    'ingredientes': ...,
    'tiempo': ...,    # int
    'dificultad': ...
}
```

### Paso 4 — Funcion `mostrar_todas()`

- Si `recetas` esta vacia, muestra: `"No tienes recetas guardadas todavia."`
- Si hay recetas, recorrelas con `enumerate()` mostrando el numero y los datos de cada una

Ejemplo de salida:
```
--- Tu recetario ---
1. Tortilla de papas  |  Dificultad: media  |  Tiempo: 30 min
2. Ensalada cesar     |  Dificultad: facil  |  Tiempo: 15 min
```

### Paso 5 — Funcion `buscar_por_dificultad()`

- Pide una dificultad al usuario
- Filtra la lista `recetas` y muestra solo las que coincidan
- Informa cuantas recetas encontro

### Paso 6 — Funcion `receta_aleatoria()`

- Si no hay recetas, avisa al usuario
- Si las hay, elige una al azar con `random.choice(recetas)` y la muestra completa

### Paso 7 — Funcion `estadisticas()`

Calcula y muestra:
- Total de recetas
- Tiempo promedio de preparacion (suma de tiempos / cantidad)
- Cuantas recetas hay de cada dificultad (`facil`, `media`, `dificil`)

> **Tip:** Usa un diccionario con las tres dificultades como claves y un contador como valor. Recorre la lista y suma.

### Paso 8 — Funcion `guardar_en_csv()`

Guarda todas las recetas en `ARCHIVO_CSV` usando `csv.DictWriter`.

```python
with open(ARCHIVO_CSV, 'w', newline='', encoding='utf-8') as f:
    campos = ['nombre', 'ingredientes', 'tiempo', 'dificultad']
    escritor = csv.DictWriter(f, fieldnames=campos)
    escritor.writeheader()
    # TODO: escribe cada receta
```

### Paso 9 — Funcion `cargar_desde_csv()`

Intenta cargar el archivo `ARCHIVO_CSV`. Si no existe, no pasa nada (usa `try/except`).

Recuerda convertir el tiempo de `str` a `int` al cargar (el CSV guarda todo como texto).

### Paso 10 — Funcion `main()` y el menu

Completa la funcion `main()`:
1. Llama a `mostrar_bienvenida()`
2. Llama a `cargar_desde_csv()` para cargar datos del archivo si existe
3. Entra en un ciclo `while True` que muestra el menu y procesa la opcion del usuario
4. Sal del ciclo cuando el usuario elija la opcion 8 (Salir)

---

## Ejemplo de ejecucion

```
===================================
   Sistema de Recetas Favoritas
   Hoy es: viernes, 07 marzo 2026
===================================
Recetario cargado desde mis_recetas.csv (2 recetas encontradas).

=== MENU ===
1. Agregar receta
2. Ver todas las recetas
3. Buscar por dificultad
4. Receta aleatoria
5. Ver estadisticas
6. Guardar en archivo
7. Cargar desde archivo
8. Salir
Elige una opcion: 2

--- Tu recetario ---
1. Tortilla de papas  |  Dificultad: media  |  Tiempo: 30 min
2. Ensalada cesar     |  Dificultad: facil  |  Tiempo: 15 min
```

---

## Niveles de dificultad

### Basico
Completa las funciones `mostrar_bienvenida()`, `agregar_receta()` y `mostrar_todas()`.
El programa debe poder agregar y mostrar recetas en pantalla, aunque no las guarde.

### Intermedio
Agrega las funciones `buscar_por_dificultad()`, `receta_aleatoria()` y `estadisticas()`.
Integra todo en el menu principal con el ciclo `while`.

### Avanzado
Implementa `guardar_en_csv()` y `cargar_desde_csv()` para que el recetario persista
entre sesiones. Cuando cierres y vuelvas a abrir el programa, tus recetas deben seguir ahi.

---

## Pistas si te trabas

- Para validar que la dificultad sea correcta, usa un ciclo `while True` con `break`
  cuando el valor sea valido:
  ```python
  while True:
      dificultad = input('Dificultad (facil/media/dificil): ').lower()
      if dificultad in ['facil', 'media', 'dificil']:
          break
      print('Opcion no valida. Intenta de nuevo.')
  ```

- Para convertir el tiempo a entero de forma segura:
  ```python
  try:
      tiempo = int(input('Tiempo en minutos: '))
  except ValueError:
      print('Ingresa un numero valido.')
  ```

- `random.choice(lista)` devuelve un elemento aleatorio de la lista

- `csv.DictWriter` necesita que le pases la lista de campos con `fieldnames`

---

## Extension opcional

Si terminas todo lo anterior y quieres ir mas lejos:

- Agrega la opcion de **eliminar** una receta por numero
- Permite **editar** el tiempo o la dificultad de una receta existente
- Agrega un campo `fecha_agregada` usando `datetime.now()` al crear la receta
- Ordena las recetas por tiempo antes de mostrarlas (investiga `sorted()` con `key=`)

---

## Recursos

- [Guia 01 — Introduccion a Python](../guias/01_introduccion_a_python.md)
- [Guia 02 — Variables y Tipos de Datos](../guias/02_variables_y_tipos_de_datos.md)
- [Guia 03 — Condicionales](../guias/03_condicionales.md)
- [Guia 04 — Ciclos](../guias/04_ciclos.md)
- [Guia 05 — Funciones](../guias/05_funciones.md)
- [Guia 06 — Listas y Diccionarios](../guias/06_listas_y_diccionarios.md)
- [Guia 07 — Entrada y Salida](../guias/07_entrada_y_salida.md)
- [Guia 08 — Modulos y Librerias](../guias/08_modulos_y_librerias.md)
