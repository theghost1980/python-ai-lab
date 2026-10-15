# Plan: de dev TypeScript a Full-Stack AI Engineer (Python)

**Objetivo:** en 8 semanas, unas 10 h a la semana (1-1,5 h al día), tener **dos demos públicas** que cubran lo que piden las ofertas de "Senior GenAI Engineer": Python async, Pydantic, LangGraph, LiteLLM, Langfuse y RAG.

**Regla de oro:** escribe tú el código. Usa Claude Code solo para revisar ("¿qué sería más pythónico?"), no para generar.

Marca cada casilla al terminar (`- [x]`). Haz commit cada día: `git commit -m "día N"`.

---

## Día 0: preparación

- [x] Instalar las extensiones recomendadas de VS Code (aparece un aviso al abrir la carpeta)
- [x] `uv sync` y `uv run pytest` (2 tests en verde y 3 en skip)
- [x] Copiar `.env.example` a `.env` y poner la clave de OpenRouter
- [ ] `git init`, primer commit y repo **público** en GitHub (aprender en público también cuenta para el CV)

## Semana 1: el lenguaje

- [ ] **Día 1:** sintaxis con Learn X in Y minutes y 5 katas en CheckiO → `ejercicios/semana1/dia01_katas.md`
- [ ] **Día 2:** estructuras y comprehensions → `dia02_estadisticas.py`
- [ ] **Día 3:** tipado, dataclasses y `mypy --strict` → `dia03_tipado.py`
- [ ] **Día 4:** `asyncio`, `gather` y `Semaphore` contra OpenRouter → `dia04_async.py`
- [ ] **Día 5:** reintentos, timeouts y Exercism → `dia05_reintentos.md`

## Semana 2: Pydantic, FastAPI y tests

- [ ] **Día 6:** modelos Pydantic (tus esquemas Zod) → `src/demo_agent/models.py`
- [ ] **Día 7:** el LLM devuelve JSON y Pydantic lo valida → `src/demo_agent/llm.py`
- [ ] **Día 8:** `POST /analyze` con FastAPI → `src/demo_agent/api.py`
- [ ] **Día 9:** lotes con progreso en streaming → `src/demo_agent/api.py`
- [ ] **Día 10:** verificación de citas y pytest → `src/demo_agent/verify.py`

**Resultado de la semana 2:** una API que analiza transcripciones con salida tipada, en paralelo, con citas verificadas y con tests.

## Semanas 3-4: LangGraph

- [ ] Curso gratuito _Introduction to LangGraph_ de LangChain Academy (academy.langchain.com)
- [ ] Conceptos clave: estado, nodos, aristas condicionales, checkpoints e `interrupt` (human-in-the-loop)
- [ ] Repartir el código de la semana 2 en nodos: ingesta → extracción → verificación → aprobación humana → informe

## Semanas 5-6: demo 1, analizador de llamadas con agente

- [ ] Grafo de LangGraph completo con `interrupt` para la aprobación humana
- [ ] **LiteLLM:** fallback Claude → OpenAI → OpenRouter, más tokens y coste por ejecución
- [ ] **Langfuse:** trazas de cada nodo y coste visible
- [ ] Datos públicos (podcasts, presentaciones de resultados), **nunca** datos de clientes
- [ ] README con diagrama de arquitectura y vídeo de 2 minutos

## Semanas 7-8: demo 2, el agente de tu web con RAG

- [ ] Backend FastAPI + pgvector + LangGraph para el chat "Ask me about Saturno"
- [ ] Que cite la fuente de cada respuesta (CV, proyectos, repos)
- [ ] Set de evaluación de 20 preguntas con métricas de exactitud y alucinación en Langfuse
- [ ] Desplegado y enlazado desde saturnodev.netlify.app

## Al terminar

- [ ] Titular del CV: "Full-Stack AI Engineer · TypeScript & Python · LLM agents in production"
- [ ] Quitar "Python (nivel básico)" del CV y enlazar las dos demos
- [ ] Añadir las demos a la web, en la sección Work

---

## Recursos

| Tema             | Enlace                                                     |
| ---------------- | ---------------------------------------------------------- |
| uv               | https://docs.astral.sh/uv/                                 |
| Sintaxis rápida  | https://learnxinyminutes.com/python/                       |
| Tutorial oficial | https://docs.python.org/3/tutorial/                        |
| Tipos (mypy)     | https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html |
| Async            | https://realpython.com/async-io-python/                    |
| Pydantic         | https://docs.pydantic.dev/latest/                          |
| FastAPI          | https://fastapi.tiangolo.com/tutorial/                     |
| Práctica diaria  | https://checkio.org · https://exercism.org/tracks/python   |
| LangGraph        | https://academy.langchain.com                              |
