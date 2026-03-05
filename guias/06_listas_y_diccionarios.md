# Guia 06 — Listas y diccionarios

Hasta ahora has guardado un dato por variable. Pero los programas reales manejan colecciones de datos: una lista de participantes, las calificaciones de un grupo, la informacion de un usuario. Para eso Python tiene estructuras de datos especiales.

En esta guia aprenderemos las dos mas importantes: **listas** y **diccionarios**.

---

## Listas

Una lista es una coleccion ordenada de elementos. Se escribe entre corchetes `[]`, con los elementos separados por comas:

```python
participantes = ["Ana", "Lucia", "Valeria", "Sofia"]
calificaciones = [85, 92, 67, 78, 91]
mixta = ["texto", 42, True, 3.14]
vacia = []
```

Una lista puede contener cualquier tipo de dato, e incluso mezclarlos, aunque en la practica suele tener elementos del mismo tipo.

---

## Acceder a elementos por indice

Cada elemento de una lista tiene una posicion llamada **indice**. Los indices **empiezan en 0**:

```python
frutas = ["manzana", "pera", "uva", "mango"]
#           0          1       2      3

print(frutas[0])  # manzana
print(frutas[2])  # uva
```

Tambien puedes usar indices negativos para contar desde el final:

```python
print(frutas[-1])  # mango (ultimo)
print(frutas[-2])  # uva (penultimo)
```

Si intentas acceder a un indice que no existe, Python lanza un `IndexError`.

---

## Modificar elementos

Las listas son **mutables**: puedes cambiar sus elementos despues de crearlas.

```python
frutas = ["manzana", "pera", "uva"]
frutas[1] = "melon"
print(frutas)  # ['manzana', 'melon', 'uva']
```

---

## Metodos de listas

Python incluye metodos para manipular listas. Se usan con la notacion `lista.metodo()`:

### Agregar elementos

```python
frutas = ["manzana", "pera"]

frutas.append("uva")       # agrega al final
print(frutas)              # ['manzana', 'pera', 'uva']

frutas.insert(1, "mango")  # inserta en la posicion 1
print(frutas)              # ['manzana', 'mango', 'pera', 'uva']
```

### Eliminar elementos

```python
frutas = ["manzana", "pera", "uva", "mango"]

frutas.remove("pera")   # elimina por valor
print(frutas)           # ['manzana', 'uva', 'mango']

frutas.pop()            # elimina el ultimo elemento
print(frutas)           # ['manzana', 'uva']

frutas.pop(0)           # elimina por indice
print(frutas)           # ['uva']
```

### Buscar y ordenar

```python
numeros = [4, 1, 9, 2, 7, 1]

print(numeros.index(9))   # 2 (posicion del valor 9)
print(numeros.count(1))   # 2 (cuantas veces aparece el 1)

numeros.sort()
print(numeros)            # [1, 1, 2, 4, 7, 9]

numeros.sort(reverse=True)
print(numeros)            # [9, 7, 4, 2, 1, 1]

numeros.reverse()         # invierte el orden actual
```

### Otras operaciones utiles

```python
frutas = ["manzana", "pera", "uva"]

print(len(frutas))          # 3 — cantidad de elementos
print("pera" in frutas)     # True — verificar si existe
print("mango" in frutas)    # False

frutas2 = ["mango", "melon"]
todas = frutas + frutas2    # concatenar dos listas
print(todas)                # ['manzana', 'pera', 'uva', 'mango', 'melon']
```

---

## Recorrer una lista con `for`

Ya lo viste en la guia de ciclos, pero vale reforzarlo con mas ejemplos:

```python
puntajes = [70, 85, 60, 92, 55]

for puntaje in puntajes:
    if puntaje >= 60:
        print(f"{puntaje} — Aprobado")
    else:
        print(f"{puntaje} — Reprobado")
```

Si necesitas el indice ademas del valor, usa `enumerate()`:

```python
participantes = ["Ana", "Lucia", "Valeria"]

for i, nombre in enumerate(participantes):
    print(f"{i + 1}. {nombre}")
```

Resultado:
```
1. Ana
2. Lucia
3. Valeria
```

---

## Sublistas con slicing

Puedes obtener una parte de una lista usando `[inicio:fin]`:

```python
numeros = [10, 20, 30, 40, 50, 60]

print(numeros[1:4])   # [20, 30, 40] — del indice 1 al 3
print(numeros[:3])    # [10, 20, 30] — desde el inicio hasta el 2
print(numeros[3:])    # [40, 50, 60] — desde el 3 hasta el final
print(numeros[::2])   # [10, 30, 50] — de dos en dos
```

---

## Diccionarios

Un diccionario guarda pares de **clave: valor**. En lugar de acceder a los elementos por posicion, lo haces por nombre. Se escribe entre llaves `{}`:

```python
estudiante = {
    "nombre": "Sofia",
    "edad": 15,
    "ciudad": "Monterrey",
    "promedio": 8.7
}
```

Cada clave es unica dentro del diccionario y generalmente es un string. El valor puede ser cualquier tipo de dato.

---

## Acceder a valores

```python
print(estudiante["nombre"])   # Sofia
print(estudiante["edad"])     # 15
```

Si la clave no existe, Python lanza un `KeyError`. Para evitarlo, usa `.get()`:

```python
print(estudiante.get("telefono"))           # None (sin error)
print(estudiante.get("telefono", "N/A"))    # N/A (valor por defecto)
```

---

## Modificar y agregar entradas

```python
estudiante["edad"] = 16               # modificar valor existente
estudiante["escuela"] = "Tec de MTY"  # agregar nueva clave

print(estudiante)
```

---

## Eliminar entradas

```python
del estudiante["ciudad"]         # elimina la clave y su valor
telefono = estudiante.pop("edad") # elimina y devuelve el valor
```

---

## Recorrer un diccionario

```python
persona = {"nombre": "Ana", "edad": 14, "ciudad": "CDMX"}

# Solo claves
for clave in persona:
    print(clave)

# Solo valores
for valor in persona.values():
    print(valor)

# Claves y valores juntos
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
```

Resultado de la ultima version:
```
nombre: Ana
edad: 14
ciudad: CDMX
```

---

## Verificar si una clave existe

```python
if "nombre" in persona:
    print("Tiene nombre registrado")

if "telefono" not in persona:
    print("No tiene telefono registrado")
```

---

## Listas de diccionarios

Una combinacion muy comun es tener una **lista de diccionarios**, donde cada diccionario representa un elemento con varias propiedades:

```python
equipo = [
    {"nombre": "Ana",     "rol": "Desarrolladora", "edad": 15},
    {"nombre": "Lucia",   "rol": "Disenadora",     "edad": 14},
    {"nombre": "Valeria", "rol": "Investigadora",  "edad": 16},
]

for integrante in equipo:
    print(f"{integrante['nombre']} — {integrante['rol']}")
```

Resultado:
```
Ana — Desarrolladora
Lucia — Disenadora
Valeria — Investigadora
```

Esta estructura es muy parecida a como se organiza la informacion en bases de datos y APIs reales.

---

## Ejemplo completo: agenda de contactos

```python
agenda = []

def agregar_contacto(nombre, telefono):
    contacto = {"nombre": nombre, "telefono": telefono}
    agenda.append(contacto)
    print(f"Contacto '{nombre}' agregado.")

def buscar_contacto(nombre):
    for contacto in agenda:
        if contacto["nombre"].lower() == nombre.lower():
            return contacto
    return None

def mostrar_agenda():
    if len(agenda) == 0:
        print("La agenda esta vacia.")
        return
    print("\n--- Agenda ---")
    for i, contacto in enumerate(agenda, 1):
        print(f"{i}. {contacto['nombre']} — {contacto['telefono']}")

# Programa principal
agregar_contacto("Ana Garcia", "555-1234")
agregar_contacto("Lucia Lopez", "555-5678")
agregar_contacto("Valeria Ruiz", "555-9012")

mostrar_agenda()

nombre_buscar = input("\nBuscar contacto: ")
resultado = buscar_contacto(nombre_buscar)

if resultado:
    print(f"Encontrado: {resultado['nombre']} — {resultado['telefono']}")
else:
    print("Contacto no encontrado.")
```

---

## Ejercicio de esta guia

Crea un programa para gestionar las **calificaciones de un grupo**:

1. Define una lista de diccionarios donde cada uno tenga `"nombre"` y `"calificacion"`
2. Escribe una funcion `promedio_grupo(estudiantes)` que calcule el promedio de todas las calificaciones
3. Escribe una funcion `mejor_estudiante(estudiantes)` que devuelva el nombre de quien tiene la calificacion mas alta
4. Escribe una funcion `aprobados(estudiantes)` que devuelva una lista solo con los estudiantes que tienen calificacion >= 60
5. Muestra un reporte final con toda esa informacion

**Reto extra:** Agrega una funcion que ordene la lista de estudiantes por calificacion de mayor a menor y la muestre como ranking.

---

## Resumen

| Concepto | Que aprendiste |
|---|---|
| Lista `[]` | Coleccion ordenada y mutable de elementos |
| Indice | Posicion de un elemento; empieza en 0 |
| `.append()`, `.insert()` | Agregar elementos a una lista |
| `.remove()`, `.pop()` | Eliminar elementos de una lista |
| `.sort()`, `.reverse()` | Ordenar una lista |
| `enumerate()` | Recorrer una lista con indice y valor |
| Slicing `[a:b]` | Obtener una sublista |
| Diccionario `{}` | Coleccion de pares clave-valor |
| `.get()` | Acceder a un valor sin riesgo de error |
| `.items()` | Recorrer claves y valores de un diccionario |
| Lista de diccionarios | Estructura para representar colecciones de objetos |

---

## Que sigue

En la siguiente guia aprenderas sobre **entrada y salida**: como leer y escribir archivos para que tu programa pueda guardar informacion de forma permanente.

[Anterior: 05 — Funciones](05_funciones.md) | [Siguiente: 07 — Entrada y salida](07_entrada_y_salida.md)
