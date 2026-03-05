# Guia 01 — Introduccion a Python

Bienvenida. Esta es la primera guia de tu camino como programadora.

Antes de escribir codigo, vale la pena entender que es Python, por que lo usamos y como funciona la idea de "programar". No te preocupes si al principio parece mucho: todo tiene sentido a medida que practicas.

---

## Que es un programa

Un programa es un conjunto de instrucciones que le damos a la computadora para que haga algo. La computadora hace exactamente lo que le decimos, ni mas ni menos. Por eso la programacion es un ejercicio de precision: tienes que ser clara y ordenada al expresar tus ideas.

Piensalo como una receta de cocina. Si la receta dice "agrega sal al gusto", una persona entiende que significa; una computadora no. Los programas tienen que ser exactos.

---

## Que es Python

Python es un lenguaje de programacion. Los lenguajes de programacion son la forma en que los humanos le "hablamos" a las computadoras de una manera que ambos podemos entender.

Python fue creado en 1991 por Guido van Rossum. Hoy es uno de los lenguajes mas populares del mundo y se usa para:

- Desarrollar aplicaciones web y moviles
- Analizar datos y hacer graficas
- Crear inteligencia artificial
- Automatizar tareas repetitivas
- Hacer juegos

Python es un excelente primer lenguaje porque su sintaxis (la forma en que se escribe) se parece mucho al ingles natural y es facil de leer.

---

## Tu primer programa

La tradicion al aprender cualquier lenguaje de programacion es escribir un programa que muestre el mensaje "Hola, mundo". Es simple, pero es un gran primer paso.

Abre tu editor o entorno (VS Code, Replit o Google Colab) y escribe esto:

```python
print("Hola, mundo")
```

Ejecutalo. Deberia aparecer en la pantalla:

```
Hola, mundo
```

Eso es todo. Acabas de escribir y ejecutar tu primer programa en Python.

### Que hace `print`?

`print` es una funcion que le dice a Python: "muestra esto en la pantalla". Lo que va dentro de los parentesis y entre comillas es el texto que quieres mostrar. En programacion, ese tipo de texto se llama **cadena de caracteres** o **string**.

Puedes cambiar el mensaje:

```python
print("Hola, soy programadora")
print("Me llamo Sofia")
print("Bienvenida a Python")
```

Cada `print` muestra una linea nueva. Prueba escribir varias seguidas y ve que pasa.

---

## Comentarios en el codigo

Los comentarios son notas que escribes en el codigo para explicar lo que hace. Python los ignora completamente; son solo para ti (o para quien lea tu codigo despues).

Un comentario empieza con el simbolo `#`:

```python
# Este programa saluda al usuario
print("Hola, mundo")

# Puedo poner comentarios en cualquier parte
print("Python es genial")  # Incluso al final de una linea de codigo
```

Acostumbrate a comentar tu codigo. Cuando vuelvas a leerlo despues de varios dias, te lo agradeceraas.

---

## Como funciona Python por dentro

Cuando ejecutas un programa de Python, pasan dos cosas:

1. Python lee tu codigo de arriba hacia abajo, linea por linea
2. Ejecuta cada instruccion en el orden en que aparece

Esto se llama **ejecucion secuencial**. Por ahora, todo lo que escribas se ejecutara en ese orden. Mas adelante aprenderas a cambiar ese orden usando condiciones y ciclos.

---

## Errores: parte normal del proceso

Cuando programas, vas a cometer errores. Todos lo hacen, incluso las programadoras con anos de experiencia. Lo importante es aprender a leer los mensajes de error para entender que salio mal.

Prueba escribir esto (con un error intencional):

```python
print("Hola, mundo"
```

Python te mostrara algo como:

```
  File "mi_programa.py", line 1
    print("Hola, mundo"
                       ^
SyntaxError: '(' was never closed
```

El error dice `SyntaxError`, que significa que algo en la escritura del codigo no esta bien formado. En este caso, falta el parentesis de cierre `)`.

Los errores mas comunes al principio son:

| Error | Causa tipica |
|---|---|
| `SyntaxError` | Parentesis, comillas o dos puntos faltantes |
| `NameError` | Usaste una palabra que Python no reconoce |
| `IndentationError` | El codigo no tiene el espaciado correcto |

No entres en panico cuando veas un error. Leelo con calma, busca la linea que menciona, y compara con el ejemplo correcto.

---

## Diferencia entre mayusculas y minusculas

Python distingue entre mayusculas y minusculas. Esto se llama ser **sensible a mayusculas** (o *case-sensitive* en ingles).

```python
print("correcto")   # Esto funciona
Print("incorrecto") # Esto genera un error: 'Print' no existe
PRINT("incorrecto") # Esto tambien genera un error
```

Cuando uses palabras que Python conoce (como `print`), asegurate de escribirlas exactamente como se muestran en los ejemplos.

---

## Donde escribir y ejecutar codigo Python

Tienes varias opciones segun lo que tengas disponible:

| Opcion | Requiere instalacion | Requiere internet |
|--------|---------------------|-------------------|
| Replit | No | Si |
| Google Colab | No | Si |
| VS Code + Python | Si | Solo para instalar |

### Opcion 1 — Replit (desde el navegador, sin instalar nada)
Entra a [replit.com](https://replit.com), crea una cuenta gratuita y abre un nuevo proyecto de Python. Es la forma mas rapida de empezar. Veras el editor a la izquierda y la consola con los resultados a la derecha; el boton **Run** ejecuta tu codigo.

### Opcion 2 — Google Colab (cuadernos interactivos)
Entra a [colab.research.google.com](https://colab.research.google.com). Necesitas una cuenta de Google. Escribe codigo en celdas y ejecuitalas con `Shift + Enter`. Los resultados aparecen justo debajo de cada celda, lo que es muy util para aprender paso a paso.

### Opcion 3 — VS Code + Python instalado en tu computadora
Si quieres trabajar sin depender de internet y tener un entorno mas completo, instala Python y el editor VS Code. Para las instrucciones detalladas de instalacion en Windows, macOS y Linux, consulta:

[Guia de instalacion completa](../recursos/como_instalar_python.md)

> **Tip:** Si es tu primera vez, te recomendamos empezar con Replit o Google Colab. Cuando te sientas comoda con Python, puedes dar el salto a la instalacion local.

---

## Ejercicio de esta guia

Escribe un programa que haga lo siguiente:

1. Muestre tu nombre
2. Muestre tu edad
3. Muestre una cosa que te guste hacer
4. Muestre por que te interesa aprender a programar

Ejemplo de como podria verse el resultado:

```
Me llamo Valeria
Tengo 14 anos
Me gusta dibujar y escuchar musica
Quiero aprender a programar para crear una app que ayude a mi comunidad
```

No hay una sola respuesta correcta. Lo importante es que el programa funcione y muestre exactamente lo que quieres mostrar.

---

## Resumen

| Concepto | Que aprendiste |
|---|---|
| Programa | Conjunto de instrucciones para la computadora |
| Python | Lenguaje de programacion popular y facil de leer |
| `print()` | Funcion para mostrar texto en pantalla |
| String | Texto entre comillas |
| Comentario | Nota en el codigo que empieza con `#` |
| Error | Mensaje que te dice que algo no esta bien escrito |

---

## Que sigue

En la siguiente guia aprenderas sobre **variables y tipos de datos**: como guardar informacion en tu programa y que tipos de informacion puede manejar Python.

[Siguiente: 02 — Variables y tipos de datos](02_variables_y_tipos_de_datos.md)
