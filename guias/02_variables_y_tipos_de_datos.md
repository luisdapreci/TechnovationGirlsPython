# Guia 02 — Variables y tipos de datos

En la guia anterior aprendiste a mostrar texto en pantalla con `print`. Pero un programa util necesita recordar informacion: el nombre de un usuario, su edad, un puntaje, una respuesta. Para eso existen las **variables**.

---

## Que es una variable

Una variable es un espacio con nombre donde guardas un dato. Piensalo como una caja con una etiqueta: la etiqueta es el nombre de la variable y lo que hay dentro es su valor.

```python
nombre = "Sofia"
edad = 14
```

Aqui creamos dos variables:
- `nombre` guarda el texto `"Sofia"`
- `edad` guarda el numero `14`

El simbolo `=` no significa "igual" como en matematicas. Significa **"guarda este valor en esta variable"**. Se llama **operador de asignacion**.

Ahora podemos usar esas variables en cualquier parte del programa:

```python
nombre = "Sofia"
edad = 14

print(nombre)
print(edad)
```

Resultado:
```
Sofia
14
```

---

## Reglas para nombrar variables

Los nombres de variables pueden ser casi cualquier cosa, pero hay reglas:

| Regla | Ejemplo correcto | Ejemplo incorrecto |
|---|---|---|
| Solo letras, numeros y guion bajo `_` | `mi_nombre` | `mi-nombre` |
| No pueden empezar con un numero | `resultado2` | `2resultado` |
| No pueden tener espacios | `nombre_completo` | `nombre completo` |
| No pueden ser palabras reservadas de Python | `puntos` | `print`, `if`, `for` |

Ademas, por convencion (no es obligatorio pero si recomendado):
- Usa nombres en **minusculas**
- Separa palabras con guion bajo: `nombre_usuario`, `puntaje_total`
- Usa nombres **descriptivos**: `edad` es mejor que `x`, `nombre_jugadora` es mejor que `n`

Un buen nombre hace que el codigo sea facil de leer y entender.

---

## Tipos de datos

No todos los datos son iguales. Python distingue entre diferentes **tipos de datos**. Los mas importantes para empezar son cuatro:

### 1. Cadena de texto — `str`

Texto entre comillas simples o dobles. Se llama *string* en ingles.

```python
saludo = "Hola, mundo"
ciudad = 'Ciudad de Mexico'
mensaje = "Bienvenida a Technovation Girls"
```

Puedes usar comillas simples `'...'` o dobles `"..."`. Lo importante es que abras y cierres con el mismo tipo.

### 2. Numero entero — `int`

Numeros sin decimales, positivos o negativos.

```python
edad = 15
puntaje = 200
temperatura = -3
nivel = 0
```

### 3. Numero decimal — `float`

Numeros con parte decimal. Se usa punto `.`, no coma.

```python
precio = 19.99
promedio = 8.5
altura = 1.62
```

### 4. Valor verdadero o falso — `bool`

Solo puede tener dos valores: `True` (verdadero) o `False` (falso). La primera letra va en mayuscula.

```python
esta_lloviendo = False
tiene_cuenta = True
es_mayor_de_edad = False
```

Los booleanos se vuelven muy utiles cuando aprendas condicionales en la siguiente guia.

---

## Como saber el tipo de un dato

Python tiene una funcion llamada `type()` que te dice de que tipo es un valor o variable:

```python
nombre = "Valeria"
edad = 13
altura = 1.55
es_estudiante = True

print(type(nombre))
print(type(edad))
print(type(altura))
print(type(es_estudiante))
```

Resultado:
```
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

---

## Cambiar el valor de una variable

Una variable puede cambiar de valor durante el programa. Por eso se llama "variable".

```python
puntos = 0
print(puntos)  # muestra: 0

puntos = 10
print(puntos)  # muestra: 10

puntos = 25
print(puntos)  # muestra: 25
```

Cada vez que usas `=`, el valor anterior se reemplaza con el nuevo.

---

## Operaciones con variables

### Con numeros

Puedes hacer operaciones matematicas directamente:

```python
precio = 50
descuento = 10
precio_final = precio - descuento

print(precio_final)  # muestra: 40
```

Los operadores matematicos en Python son:

| Operador | Operacion | Ejemplo | Resultado |
|---|---|---|---|
| `+` | Suma | `5 + 3` | `8` |
| `-` | Resta | `10 - 4` | `6` |
| `*` | Multiplicacion | `3 * 7` | `21` |
| `/` | Division | `15 / 2` | `7.5` |
| `//` | Division entera | `15 // 2` | `7` |
| `%` | Residuo | `15 % 2` | `1` |
| `**` | Potencia | `2 ** 8` | `256` |

### Con texto

Puedes unir cadenas de texto con el operador `+`. Esto se llama **concatenacion**:

```python
nombre = "Ana"
apellido = "Garcia"
nombre_completo = nombre + " " + apellido

print(nombre_completo)  # muestra: Ana Garcia
```

Tambien puedes repetir texto con `*`:

```python
linea = "-" * 20
print(linea)  # muestra: --------------------
```

---

## Combinar texto y variables con f-strings

Una forma muy practica de mezclar texto fijo con variables es usando **f-strings**. Solo pones una `f` antes de las comillas y encierras las variables entre llaves `{}`:

```python
nombre = "Camila"
edad = 16

print(f"Me llamo {nombre} y tengo {edad} anos.")
```

Resultado:
```
Me llamo Camila y tengo 16 anos.
```

Esto es mucho mas claro que concatenar con `+`. Usaras f-strings constantemente, asi que vale la pena practicarlos desde ahora.

---

## Pedir datos al usuario

Hasta ahora los valores de las variables los escribimos directamente en el codigo. Pero los programas utiles le **preguntan** cosas al usuario. Para eso usamos la funcion `input()`:

```python
nombre = input("Como te llamas? ")
print(f"Hola, {nombre}!")
```

Cuando ejecutas este programa, Python espera a que escribas algo y presiones Enter. Lo que escribas queda guardado en la variable `nombre`.

**Importante:** `input()` siempre devuelve un *string*, aunque el usuario escriba un numero. Si necesitas usar ese dato como numero, debes convertirlo:

```python
edad_texto = input("Cuantos anos tienes? ")
edad = int(edad_texto)  # convierte el string a numero entero

print(f"En 5 anos tendras {edad + 5} anos.")
```

O de forma mas corta:

```python
edad = int(input("Cuantos anos tienes? "))
print(f"En 5 anos tendras {edad + 5} anos.")
```

---

## Conversion entre tipos de datos

Python tiene funciones para convertir datos de un tipo a otro:

| Funcion | Convierte a | Ejemplo |
|---|---|---|
| `int()` | Numero entero | `int("25")` → `25` |
| `float()` | Numero decimal | `float("3.14")` → `3.14` |
| `str()` | Texto | `str(100)` → `"100"` |
| `bool()` | Verdadero/Falso | `bool(0)` → `False` |

---

## Ejercicio de esta guia

Escribe un programa que:

1. Le pregunte al usuario su nombre
2. Le pregunte su edad
3. Le pregunte el nombre de su ciudad
4. Muestre un resumen con esa informacion usando f-strings

Ejemplo de como deberia verse al ejecutarlo:

```
Como te llamas? Lucia
Cuantos anos tienes? 15
En que ciudad vives? Monterrey

--- Tu perfil ---
Nombre: Lucia
Edad: 15 anos
Ciudad: Monterrey
En 3 anos tendras 18 anos.
```

**Reto extra:** agrega una linea que calcule en que ano naciste (pista: el ano actual es 2025, restale la edad).

---

## Resumen

| Concepto | Que aprendiste |
|---|---|
| Variable | Espacio con nombre para guardar un dato |
| `=` | Operador de asignacion (no es "igual") |
| `str` | Tipo de dato para texto |
| `int` | Tipo de dato para numeros enteros |
| `float` | Tipo de dato para numeros decimales |
| `bool` | Tipo de dato para verdadero/falso |
| `type()` | Funcion que dice de que tipo es un dato |
| `input()` | Funcion para pedirle datos al usuario |
| f-string | Forma de mezclar texto y variables con `f"...{variable}..."` |

---

## Que sigue

En la siguiente guia aprenderas sobre **condicionales**: como hacer que tu programa tome decisiones y ejecute diferentes instrucciones segun la situacion.

[Anterior: 01 — Introduccion a Python](01_introduccion_a_python.md) | [Siguiente: 03 — Condicionales](03_condicionales.md)
