# CLAUDE.md — AI Assistant Guide for TechnovationGirlsPython

This file provides context for AI assistants working on this repository.

---

## Project Overview

**TechnovationGirlsPython** is a Spanish-language educational resource repository for the [Technovation Girls](https://technovationchallenge.org/) program. It teaches Python programming — from absolute fundamentals to building real web applications — to students ages 12–17 with no prior experience. All written content is in **Spanish**, with English used only for technical keywords (e.g., `print`, `input`, `if`, `for`).

The curriculum is organized in **three progressive levels**:
- **Nivel Basico** — Python fundamentals (Guides 01–08)
- **Nivel Intermedio** — OOP, HTML, CSS, HTTP, and APIs (Guides 09–14)
- **Nivel Avanzado** — Web development with FastAPI (Guides 15–19)

**Repository type:** Documentation-only (Markdown guides). No runnable source code, no tests, no build system.

---

## Repository Structure

```
TechnovationGirlsPython/
├── README.md                          # Project overview and learning path
├── CLAUDE.md                          # This file
├── guias/                             # 19 sequential learning guides (3 levels)
│   │
│   │  — Nivel Basico (Guides 01–08) —
│   ├── 01_introduccion_a_python.md        # What is Python, first program, environments
│   ├── 02_variables_y_tipos_de_datos.md   # Variables, types, input/output
│   ├── 03_condicionales.md                # if/elif/else, comparison operators
│   ├── 04_ciclos.md                       # for/while loops, break/continue
│   ├── 05_funciones.md                    # Functions, parameters, return values
│   ├── 06_listas_y_diccionarios.md        # Lists, dicts, data structures
│   ├── 07_entrada_y_salida.md             # File I/O, CSV, error handling
│   ├── 08_modulos_y_librerias.md          # Modules, pip, standard library
│   │
│   │  — Nivel Intermedio (Guides 09–14) —
│   ├── 09_clases_y_objetos.md             # OOP: classes, methods, instances
│   ├── 10_html_basico.md                  # HTML structure, tags, semantics
│   ├── 11_css_basico.md                   # Selectors, colors, typography, layout
│   ├── 12_formularios_html.md             # Inputs, validation, form submission
│   ├── 13_http_y_la_web.md                # How the internet works, requests/responses
│   ├── 14_consumir_apis.md                # requests, JSON, public APIs
│   │
│   │  — Nivel Avanzado (Guides 15–19) —
│   ├── 15_introduccion_a_fastapi.md       # First server, installation, Uvicorn
│   ├── 16_rutas_y_metodos_http.md         # GET, POST, parameters, Pydantic
│   ├── 17_plantillas_con_jinja2.md        # Dynamic HTML from Python, Jinja2
│   ├── 18_formularios_con_fastapi.md      # Processing HTML form data
│   └── 19_proyecto_web_completo.md        # Full app: FastAPI + HTML + CSS
│
└── recursos/                          # Reference and setup materials
    ├── como_instalar_python.md        # Replit, Google Colab, VS Code, local install
    ├── glosario.md                    # Key terms explained in Spanish
    └── herramientas_utiles.md         # Extensions, shortcuts, recommended settings
```

### Publication Status
- **Nivel Basico (01–08):** Complete and published
- **Nivel Intermedio (09–14):** Planned — guides being developed progressively
- **Nivel Avanzado (15–19):** Planned — guides being developed progressively
- **recursos/:** Planned — reference files to be added alongside level guides

---

## Content and Curriculum

### Learning Progression
The 19 guides follow a strict, sequential learning path across three levels:

#### Nivel Basico — Fundamentos de Python (Guides 01–08)

| Guide | Topic | Key Concepts |
|-------|-------|--------------|
| 01 | Introduction to Python | `print()`, comments, Replit/Colab/local setup |
| 02 | Variables & Data Types | `str`, `int`, `float`, `bool`, `input()`, f-strings, type conversion |
| 03 | Conditionals | `if`/`elif`/`else`, comparison + logical operators, `in` keyword |
| 04 | Loops | `for`/`while`, `range()`, `break`/`continue`, accumulator pattern |
| 05 | Functions | `def`, parameters, `return`, default args, scope |
| 06 | Lists & Dicts | List methods, dict methods, list-of-dicts pattern, `enumerate()` |
| 07 | File I/O | `open()`, `with`, read/write modes, `csv` module, `try/except` |
| 08 | Modules & Libraries | `import`, standard library, `pip`, `requests`, `flask`, etc. |

#### Nivel Intermedio — Hacia el Desarrollo Web (Guides 09–14)

| Guide | Topic | Key Concepts |
|-------|-------|--------------|
| 09 | Classes & Objects | `class`, `__init__`, methods, instances, OOP concepts |
| 10 | Basic HTML | Document structure, semantic tags, links, images |
| 11 | Basic CSS | Selectors, box model, colors, typography, flexbox basics |
| 12 | HTML Forms | `<form>`, input types, labels, form validation, data submission |
| 13 | HTTP & The Web | Client/server model, HTTP methods, status codes, URLs |
| 14 | Consuming APIs | `requests` library, JSON parsing, public APIs, error handling |

#### Nivel Avanzado — Aplicaciones Web con FastAPI (Guides 15–19)

| Guide | Topic | Key Concepts |
|-------|-------|--------------|
| 15 | Intro to FastAPI | `fastapi`, `uvicorn`, first server, route decorators |
| 16 | Routes & HTTP Methods | GET/POST routes, path/query params, Pydantic models |
| 17 | Templates with Jinja2 | `jinja2`, `Jinja2Templates`, dynamic HTML rendering |
| 18 | Forms with FastAPI | `Form(...)`, processing HTML form data, redirects |
| 19 | Complete Web Project | Full app integrating FastAPI + HTML + CSS + data |

### Each Guide's Structure
Every guide follows this internal layout:
1. **Learning objectives** — What the student will be able to do
2. **Concept explanations** — With tables, analogies, and inline code
3. **Code examples** — Annotated, runnable Python snippets
4. **Common mistakes** — Typical errors beginners make
5. **Exercises** — 3 difficulty tiers: Básico, Intermedio, Avanzado
6. **Navigation links** — "Guía anterior" / "Siguiente guía"

---

## Code Conventions (for examples in guides)

All Python code samples in the guides follow these conventions:

- **Variable names:** `snake_case` in Spanish (e.g., `nombre_usuario`, `puntaje_total`)
- **Indentation:** 4 spaces (never tabs)
- **Strings:** Single quotes preferred; f-strings for interpolation (`f"Hola {nombre}"`)
- **Comments:** `#` with a space and a short Spanish explanation
- **Functions:** Named with descriptive Spanish verbs (e.g., `calcular_promedio`, `mostrar_menu`)
- **Constants:** Not explicitly taught, but used from standard library (e.g., `math.pi`)

### Taught Programming Patterns

**Nivel Basico:**
- **Accumulator pattern** — variable initialized before loop, updated inside
- **Input validation loop** — `while True` with `break` on valid input
- **List of dicts** — standard way to model records/objects
- **Functional decomposition** — one function = one responsibility
- **Context manager** — `with open(...) as f:` for all file operations

**Nivel Intermedio:**
- **OOP encapsulation** — grouping data and behavior in a class
- **API request/response cycle** — fetch JSON, parse, display
- **Form data flow** — HTML form → HTTP POST → server handler

**Nivel Avanzado:**
- **Route handler pattern** — one function per URL route
- **Template rendering** — pass Python data into Jinja2 HTML templates
- **MVC-lite separation** — routes (logic) vs. templates (presentation) vs. data

---

## Writing Style Guidelines

When adding or editing guide content:

1. **Language:** Write in clear, simple Spanish. Avoid regional slang; use neutral Latin American Spanish.
2. **Tone:** Encouraging and supportive. Address the reader as "tú" (informal singular). Celebrate progress.
3. **Technical terms:** Use the English Python keyword/term first, then explain in Spanish (e.g., "`print()` — la función para mostrar texto en pantalla").
4. **Examples:** Use relatable scenarios for young women: social apps, quizzes, personal projects, games.
5. **Inclusivity:** Avoid gendered examples that assume only male readers. Use neutral names or female names.
6. **Code blocks:** Always use fenced markdown code blocks with `python` syntax highlighting.
7. **Callout boxes:** Use `>` blockquotes for tips (`> **Tip:**`), warnings (`> **⚠️ Cuidado:**`), and notes.

---

## No Build/Test Infrastructure

This repository has **no build system, no test runner, and no CI/CD pipeline**. There is nothing to install or run at the repository level. Validation is manual (read the Markdown files and verify code examples are correct Python 3).

If you are asked to verify code examples, test them mentally or note that they should be run in Python 3 directly.

---

## Development Workflow

### Branch Strategy
- **`master`** — Main/production branch with published content
- **`claude/...`** — AI-generated feature branches (e.g., `claude/claude-md-mme2xeprxugvhmoj-0rNMf`)

### Commit Style
Commits follow a short imperative format:
```
Add Guia 08: Modulos y librerias
Update README with new guide links
Fix typo in condicionales examples
```

### When Adding a New Guide
1. Create file in `guias/` with zero-padded number prefix: `09_tema.md`
2. Follow the internal guide structure (objectives → concepts → examples → exercises → navigation)
3. Add a link to the new guide in `README.md` under the correct level section ("Nivel Basico", "Nivel Intermedio", or "Nivel Avanzado")
4. Update navigation links in the previous guide to point to the new one
5. For Nivel Intermedio and Avanzado guides, note any new library requirements at the top of the guide

### When Adding to `recursos/`
1. Create the file in `recursos/` with a descriptive name: `como_instalar_python.md`
2. Keep content tool-agnostic where possible (cover Replit, Colab, and local options)
3. Add a link to the file in `README.md` under "Recursos y apoyo"

### When Editing an Existing Guide
- Preserve the existing structure and section headers
- Keep all code examples valid Python 3
- Do not remove exercise difficulty tiers
- For Nivel Intermedio/Avanzado guides, verify that prerequisite guides are clearly referenced

---

## Key Dependencies (Used in Code Examples)

### Standard Library

| Module | Used In | Purpose |
|--------|---------|---------|
| `random` | Guide 04, 08 | Random numbers, selections |
| `math` | Guide 08 | Math functions and constants |
| `datetime` | Guide 08 | Date and time manipulation |
| `os` / `os.path` | Guide 07 | File path operations |
| `csv` | Guide 07, 08 | CSV file reading/writing |
| `string` | Guide 08 | String constants |
| `json` | Guide 14 | JSON parsing |

### External Libraries (Nivel Intermedio & Avanzado)

| Library | Used In | Purpose |
|---------|---------|---------|
| `requests` | Guide 14 | HTTP requests to external APIs |
| `fastapi` | Guides 15–19 | Web framework for building APIs and web apps |
| `uvicorn` | Guides 15–19 | ASGI server to run FastAPI apps |
| `jinja2` | Guide 17–19 | HTML templating engine |
| `pydantic` | Guide 16 | Data validation for FastAPI models |
| `python-multipart` | Guide 18 | Form data parsing for FastAPI |

**Other libraries mentioned for context** (not taught in depth):
`flask`, `pandas`, `matplotlib`, `pillow`, `pygame`

> **Note for Nivel Avanzado:** FastAPI and related libraries require a local Python installation or Replit. Google Colab is not suitable for running a web server.

---

## Recommended Tools for Students

Students are directed to use one of the following, depending on their level:

| Tool | Best For | Level |
|------|----------|-------|
| **Replit** (replit.com) | Browser-based, no installation, supports FastAPI | All levels |
| **Google Colab** | Quick Python experiments, notebook style | Nivel Basico only |
| **VS Code** with Python extension | Full local development | All levels |
| **Python 3** (python.org) | Local installation base | Nivel Intermedio & Avanzado |

For Nivel Avanzado (FastAPI), students need either a local Python install or Replit — Google Colab cannot run a persistent web server.

---

## AI Assistant Guidance

### What to Do
- When creating new guides, follow the established structure and style precisely.
- When fixing code examples, ensure they are valid **Python 3** (not Python 2).
- When translating or adding content, maintain Spanish throughout with English for code/keywords only.
- When adding links between guides, use relative Markdown links: `[Guia 02](02_variables_y_tipos_de_datos.md)`.

### What NOT to Do
- Do not add source code files (`.py`) unless a `tutoriales/` or `ejercicios/` section is being created.
- Do not add `requirements.txt`, `setup.py`, or similar files — the repo has no runtime dependencies.
- Do not change the guide numbering scheme or rename existing files without updating all cross-references.
- Do not use advanced Python (decorators, async, type hints, dataclasses, metaclasses) — content targets beginners.
- Do not add CI/CD or testing infrastructure unless explicitly requested.
- Do not introduce Nivel Intermedio or Avanzado concepts (OOP, HTML, FastAPI) into Nivel Basico guides.
- Do not assume a local Python install for Nivel Basico — those guides must work on Replit or Colab.

---

## Repository Metadata

- **License:** MIT
- **Language:** Spanish (content), Python 3 (code examples)
- **Target audience:** Girls ages 12–17, ranging from complete beginners to intermediate learners
- **Affiliation:** Technovation Girls program
- **Status:** Active
  - Phase 1 (Nivel Basico, Guides 01–08): Complete
  - Phase 2 (Nivel Intermedio, Guides 09–14): In progress
  - Phase 3 (Nivel Avanzado, Guides 15–19): Planned
  - recursos/ section: Planned alongside Phase 2–3
