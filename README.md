# Python para Technovation Girls

Guias, tutoriales y ejercicios de Python para jovenes de 12 a 17 anos que participan en el programa **Technovation Girls**.

---

## Que encontraras aqui

Este repositorio es un complemento practico al curriculo de Technovation Girls. Aqui aprenderas a programar en Python desde cero hasta construir aplicaciones web reales, con ejemplos y proyectos pensados para que puedas aplicar lo que aprendes directamente en tu proyecto de Technovation.

El contenido esta organizado en tres niveles progresivos:

- **Nivel Basico** — fundamentos de Python: variables, condiciones, ciclos, funciones y archivos
- **Nivel Intermedio** — programacion orientada a objetos, HTML, CSS y consumo de APIs
- **Nivel Avanzado** — desarrollo web con FastAPI: servidor, rutas, plantillas y proyecto final

---

## Para quien es esto

- Jovenes de 12 a 17 anos participantes de Technovation Girls
- No necesitas experiencia previa en programacion
- Solo necesitas curiosidad y ganas de aprender

---

## Contenido

### Nivel Basico — Fundamentos de Python

Las primeras 8 guias te dan todo lo que necesitas saber de Python antes de pasar al desarrollo web. No se necesita experiencia previa.

```
guias/
+-- 01_introduccion_a_python.md        # Que es Python, primer programa, entornos
+-- 02_variables_y_tipos_de_datos.md   # Variables, strings, numeros, input()
+-- 03_condicionales.md                # if / elif / else, operadores
+-- 04_ciclos.md                       # for, while, range(), break, continue
+-- 05_funciones.md                    # def, parametros, return, scope
+-- 06_listas_y_diccionarios.md        # Listas, dicts, estructuras de datos
+-- 07_entrada_y_salida.md             # Archivos, CSV, try/except
+-- 08_modulos_y_librerias.md          # import, pip, libreria estandar
```

### Nivel Intermedio — Hacia el Desarrollo Web

Aqui amplias tu conocimiento de Python e introduces los conceptos fundamentales de la web: HTML, CSS y como Python se comunica con servicios externos.

```
guias/
+-- 09_clases_y_objetos.md             # Programacion orientada a objetos, clases, metodos
+-- 10_html_basico.md                  # Estructura HTML, etiquetas, semantica
+-- 11_css_basico.md                   # Selectores, colores, tipografia, layout
+-- 12_formularios_html.md             # Inputs, validacion, envio de datos
+-- 13_http_y_la_web.md                # Como funciona internet, peticiones, respuestas
+-- 14_consumir_apis.md                # requests, JSON, APIs publicas
```

### Nivel Avanzado — Aplicaciones Web con FastAPI

Con todo lo anterior puedes construir tu propia aplicacion web. Estas guias te llevan desde un servidor basico hasta una app completa con interfaz HTML/CSS y logica en Python.

```
guias/
+-- 15_introduccion_a_fastapi.md       # Primer servidor, instalacion, Uvicorn
+-- 16_rutas_y_metodos_http.md         # GET, POST, parametros, Pydantic
+-- 17_plantillas_con_jinja2.md        # HTML dinamico desde Python, Jinja2
+-- 18_formularios_con_fastapi.md      # Procesar datos de formularios HTML
+-- 19_proyecto_web_completo.md        # App funcional: FastAPI + HTML + CSS
```

### Ejercicios integradores

Proyectos que combinan todos los conceptos de un nivel. Cada ejercicio incluye
un archivo Markdown con instrucciones detalladas y un archivo `.py` con el codigo
de arranque listo para completar.

```
ejercicios/
+-- nivel_basico_proyecto_final.md     # Instrucciones del proyecto final del Nivel Basico
+-- nivel_basico_proyecto_final.py     # Codigo de arranque con TODOs para completar
```

### Recursos y apoyo

```
recursos/
+-- como_instalar_python.md            # Replit, Google Colab, VS Code, instalacion local
+-- glosario.md                        # Terminos clave explicados en espanol
+-- herramientas_utiles.md             # Extensiones, atajos y configuraciones recomendadas
```

> Las guias del Nivel Intermedio y Avanzado se iran publicando progresivamente. Las del Nivel Basico estan completas y disponibles ahora.

---

## Por donde empezar

**Si es tu primera vez programando:**

1. Elige tu entorno en [Como Instalar Python](recursos/como_instalar_python.md) (Replit es lo mas rapido)
2. Comienza con la [Guia 01 — Introduccion a Python](guias/01_introduccion_a_python.md)
3. Sigue las guias del Nivel Basico en orden, del 01 al 08
4. Cuando termines el Nivel Basico, continua con las guias del Nivel Intermedio

**Si ya sabes Python pero quieres aprender desarrollo web:**

- Salta directamente al [Nivel Intermedio](#nivel-intermedio--hacia-el-desarrollo-web) desde la guia 09

**Si ya conoces HTML/CSS y quieres construir una app con Python:**

- Ve directo al [Nivel Avanzado](#nivel-avanzado--aplicaciones-web-con-fastapi) desde la guia 15

---

## Conexion con Technovation Girls

Technovation Girls es un programa global que invita a jovenes a resolver problemas de su comunidad usando tecnologia. La programacion es una herramienta poderosa para ese objetivo.

En este repositorio encontraras ejercicios y proyectos que te ayudaran a:

- Entender como funciona el codigo detras de las apps
- Automatizar tareas y procesar informacion
- Dar forma a las ideas de tu equipo en codigo real
- Prepararte para el desarrollo de tu aplicacion movil o web

---

## Herramientas que usaremos

| Herramienta | Para que sirve | Donde conseguirla |
|---|---|---|
| Python 3 | Lenguaje de programacion principal | python.org |
| VS Code | Editor de codigo recomendado | code.visualstudio.com |
| Replit | Programar desde el navegador, sin instalar nada | replit.com |
| Google Colab | Cuadernos interactivos en la nube | colab.research.google.com |
| FastAPI | Framework para crear servidores web con Python | fastapi.tiangolo.com |
| Jinja2 | Motor de plantillas HTML para FastAPI | incluido con FastAPI |

Si no puedes instalar nada en tu computadora, puedes usar **Replit** o **Google Colab** directamente desde tu navegador. Para el Nivel Avanzado con FastAPI, recomendamos tener Python instalado localmente o usar Replit.

---

## Como contribuir

Si eres mentora, profesora o una participante que ya tiene experiencia, puedes contribuir a este repositorio:

1. Haz un *fork* del repositorio
2. Crea una rama nueva con un nombre descriptivo
3. Agrega o mejora el contenido
4. Abre un *pull request* explicando tus cambios

Todas las contribuciones son bienvenidas: correcciones, nuevos ejercicios, traducciones de ejemplos o mejoras a las explicaciones.

---

## Codigo de conducta

Este es un espacio seguro y de apoyo. Esperamos que todas las personas que participen:

- Se traten con respeto y amabilidad
- Hagan preguntas sin miedo a equivocarse
- Celebren los logros propios y ajenos
- Ayuden a otras cuando puedan

Las preguntas no tienen niveles de "dificultad correcta". Todas las dudas son validas.

---

## Licencia

El contenido de este repositorio esta disponible bajo la licencia [MIT](LICENSE). Puedes usarlo, compartirlo y adaptarlo libremente, siempre que des credito a la fuente.

---

Hecho con entusiasmo para futuras programadoras y creadoras de tecnologia.
