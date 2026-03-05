# CLAUDE.md — AI Assistant Guide for TechnovationGirlsPython

This file provides context for AI assistants working on this repository.

---

## Project Overview

**TechnovationGirlsPython** is a Spanish-language educational resource repository for the [Technovation Girls](https://technovationchallenge.org/) program. It teaches Python programming fundamentals to beginners (ages 12–17) with no prior experience. All written content is in **Spanish**, with English used only for technical keywords (e.g., `print`, `input`, `if`, `for`).

**Repository type:** Documentation-only (Markdown guides). No runnable source code, no tests, no build system.

---

## Repository Structure

```
TechnovationGirlsPython/
├── README.md                          # Project overview and learning path
├── CLAUDE.md                          # This file
└── guias/                             # 8 sequential learning guides
    ├── 01_introduccion_a_python.md    # What is Python, first program
    ├── 02_variables_y_tipos_de_datos.md  # Variables, types, input/output
    ├── 03_condicionales.md            # if/elif/else, comparison operators
    ├── 04_ciclos.md                   # for/while loops, break/continue
    ├── 05_funciones.md                # Functions, parameters, return values
    ├── 06_listas_y_diccionarios.md    # Lists, dicts, data structures
    ├── 07_entrada_y_salida.md         # File I/O, CSV, error handling
    └── 08_modulos_y_librerias.md      # Modules, pip, standard library
```

### Planned Future Structure (not yet created)
- `tutoriales/` — Guided projects for real-world applications
- `ejercicios/` — Practice problems by difficulty level
- `recursos/` — Installation guides and tool references

---

## Content and Curriculum

### Learning Progression
The 8 guides follow a strict, sequential learning path:

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
- **Accumulator pattern** — variable initialized before loop, updated inside
- **Input validation loop** — `while True` with `break` on valid input
- **List of dicts** — standard way to model records/objects
- **Functional decomposition** — one function = one responsibility
- **Context manager** — `with open(...) as f:` for all file operations

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
3. Add a link to the new guide in `README.md` under the "Contenido" section
4. Update navigation links in the previous guide to point to the new one

### When Editing an Existing Guide
- Preserve the existing structure and section headers
- Keep all code examples valid Python 3
- Do not remove exercise difficulty tiers

---

## Key Dependencies (Standard Library — Used in Code Examples)

| Module | Used In | Purpose |
|--------|---------|---------|
| `random` | Guide 04, 08 | Random numbers, selections |
| `math` | Guide 08 | Math functions and constants |
| `datetime` | Guide 08 | Date and time manipulation |
| `os` / `os.path` | Guide 07 | File path operations |
| `csv` | Guide 07, 08 | CSV file reading/writing |
| `string` | Guide 08 | String constants |

**External libraries mentioned** (not required to install for the guides themselves):
`requests`, `flask`, `pandas`, `matplotlib`, `pillow`, `pygame`

---

## Recommended Tools for Students

Students are directed to use one of:
- **Replit** (replit.com) — Browser-based, no installation
- **Google Colab** — Notebook environment, good for quick experiments
- **VS Code** with Python extension — Local development
- **Python 3** official installer from python.org

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
- Do not use advanced Python (decorators, async, type hints, dataclasses) — content targets absolute beginners.
- Do not add CI/CD or testing infrastructure unless explicitly requested.

---

## Repository Metadata

- **License:** MIT
- **Language:** Spanish (content), Python 3 (code examples)
- **Target audience:** Girls ages 12–17, complete beginners
- **Affiliation:** Technovation Girls program
- **Status:** Active — Phase 1 (8 foundational guides) complete; future phases planned
