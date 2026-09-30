# Pathfinder AI — Agent Instructions

Read this file first. Keep work small, verified and honest.

## 1. Source of truth (highest wins)

1. Actual repository code, data and test results
2. `docs/DECISIONS.md` (frozen decisions)
3. `docs/CURRENT_STATE.md` (live status; verify against code)
4. `docs/ARCHITECTURE.md`
5. `docs/PROJECT_CONTEXT.md`, `README.md`
6. `docs/archive/` (history only)

Documentation is not proof that code exists. Verify in the repo.

## 2. What Pathfinder is

An evidence-driven career decision-intelligence platform. Natural-language input → user-type detection → extraction → minimal clarification → Career Identity → Market Reality → rule-based Verdict → personalized dashboard → LLM explanation.

It is NOT a chatbot, quiz, roadmap generator, or skill-gap calculator. Not a long form.

**Frozen rules** (full list in `docs/DECISIONS.md`):
- Natural-language-first. Discover before recommend. Evidence before recommendation.
- Negative preferences are hard constraints: a fundamental conflict excludes the role. Never turn this into a score penalty.
- Reality over motivation. Unrealistic paths are labelled unrealistic, with the closest realistic alternative.
- Primary recommendations are separate from "Explore More Options".
- Multi-domain V2: engines and schema stay domain-neutral (no IT-only assumptions in logic).
- LLM explains and discusses verified results; it never decides or overrides a verdict.
- ML is supportive, justified and evaluated. V2 is local-first, ₹0. V3/production is out of scope.

## 3. Working protocol

1. Understand the exact task. Inspect only the relevant files.
2. Non-trivial task → give a 3–6 line plan first.
3. Smallest change that solves the task. No drive-by refactors, no new abstractions or files "for cleanliness".
4. Write or update a test, run it, run the full suite.
5. Report: what changed, what was verified (commands + results), what is still unverified.
6. Update `docs/CURRENT_STATE.md` only when project state materially changed.

If a real architectural problem blocks the task, explain it briefly and ask. Never silently change a frozen decision.

## 4. Anti-fragility: fix causes, not symptoms

- **Root cause first.** Reproduce the bug, find why it happens, fix that. Do not add special-case `if` patches for one input.
- **Every bug fix ships with a regression test** using the real failing input. Known golden cases live in `tests/golden/` (for example: a CSE-Data-Science student writing "CSE(data science)" must NOT get "Data Science" as a career interest; "don't want client-facing work" must exclude roles with high client interaction).
- **Single source of truth.** One place for constants, weights, thresholds, vocabularies and score formulas (`config/`). No duplicated magic numbers in engines.
- **One canonical data format.** Lists in the dataset use one representation (pipe-delimited). Parsers do not guess between formats. Never use `eval`/`ast.literal_eval` on data.
- **Structured, not stringly-typed.** Negative/positive preferences map to a fixed vocabulary of role fields (`client_interaction`, `networking_required`, `shift_type`, `travel_required`, `coding_intensity`, `leadership_required`, …), never matched as free-text sentences.
- **No silent failure.** No bare `except`, no swallowed errors, no returning default values that hide a problem. Fail loudly with `src/exceptions/` types and log context.
- **Layering.** UI → services → engines/context → models/database. Engines are pure functions of their inputs: no network, no file I/O, no LLM, no Streamlit imports. Add a test that fails if an engine imports `streamlit`, the LLM client, or the scraper.
- **Explainable outputs.** Every score/verdict stores the evidence and data source used. Generic strengths that apply to every role ("High market demand") are a bug, not a feature.
- Before editing, run `pytest`. After editing, run it again. A red suite is never left behind.

## 5. Dependencies (no hallucinated packages)

- **Never add a package you have not verified.** Before adding: confirm it exists on PyPI, the exact import name, the current maintained version, and that the API you plan to use exists in the *installed* version (check the docs or run it).
- `requirements.txt` lists **direct dependencies only**, pinned. Keep the full `pip freeze` in `requirements.lock`. Remove packages that are not imported.
- Justify every new dependency in the PR/report: what it does, why the stdlib/existing stack is not enough, its size and maintenance status.
- Approved stack: Python, Pandas, NumPy, SQLite (sqlite3), scikit-learn, Streamlit, Plotly, pytest, BeautifulSoup/requests, Scrapy or Playwright only when a source needs it, Ollama client for the LLM. Anything else (LangChain, FAISS, SQLAlchemy, PyTorch, spaCy, sentence-transformers) needs an entry in `docs/DECISIONS.md` first, and a demonstrated need. A direct prompt with structured evidence often replaces a RAG framework.
- Do not invent function names, flags, file paths or config keys. Grep the repo or read the docs first. If you cannot verify, say so.
- Run `pip check` and `python -c "import <module>"` for new imports.

## 6. Security

- **No secrets in code or git.** Use `.env` (git-ignored); keep `.env.example` with placeholders only. V2 needs no API keys.
- **SQL:** parameterized queries only. Never build SQL with f-strings or string concatenation.
- **Untrusted input:** treat user text, scraped pages and LLM output as untrusted. Validate against a schema, cap lengths, strip/escape before display. Never `eval`/`exec`/`subprocess` anything derived from them. In Streamlit, do not use `unsafe_allow_html` with user or scraped content.
- **LLM safety:** user text is data, not instructions. The LLM receives only verified evidence plus the user's question; system instructions stay fixed; its output is displayed, never executed, and never changes a verdict. LLM-based extraction must be schema-validated and must fall back to deterministic extraction.
- **Scraping:** check each source's robots.txt and terms before writing a scraper; prefer open datasets and official APIs; set timeouts, rate limits and a clear User-Agent; no login bypass, no CAPTCHA evasion, no credentials. Do not scrape sources that prohibit it.
- **Privacy:** user profiles stay local. Do not log raw user text or personal details. Do not commit real user data, databases, logs or scraped dumps.
- **Files:** validate paths and sizes; never write outside `data/`/`logs/`. Downloaded models are pinned by name and fetched only from official sources.
- Run `pip-audit` (or equivalent) when dependencies change and report findings.

## 7. Data pipeline rules

- Collection (scraping) is separate from decision logic. Engines read normalized data from the database only.
- Flow: Source → Raw → Validate → Clean → Normalize → Load. Bad data is rejected with a reason, not silently repaired.
- **Fallback:** a new dataset is built in a staging location, validated, then atomically promoted. If any step fails, keep serving the last valid dataset and surface a clear status message. Never load partial data into the live database.
- Every dataset carries `source`, `collected_at` and `version`. The UI shows them next to evidence numbers. Seed/hand-curated values are labelled as seed, never as market data.

## 8. Production-readiness (local-first, honestly)

- One-command setup and run on a clean clone (`pip install -r requirements.txt`, `python pipeline.py`, `streamlit run app.py`). If it fails on a clean clone it is a bug.
- Optional layers degrade gracefully: no Ollama running → deterministic template explanation; no internet → last valid dataset; empty result → clear message, never a stack trace in the UI.
- Config via `config/` and environment variables; no hardcoded absolute paths (use `pathlib` relative to the project root).
- Structured logging with levels; no `print` in library code.
- Free temporary hosting is optional for demos. Do not add Docker/cloud/auth/scale work in V2 (that is V3) unless explicitly requested.

## 9. Honesty (no perception gap)

- Never claim a feature works unless you ran it. Say "implemented and tested (command X)", "implemented, untested", or "not implemented".
- Do not present seed data, mock outputs or placeholder screens as real results. Label them.
- ML/LLM claims require evidence: what task, what data, what metric, compared to the rule-based baseline. If it does not beat the baseline, say so.
- UI is a thin layer. It calls `services/` and renders results; it contains no decision logic.
- Keep `README.md` status table and `docs/CURRENT_STATE.md` truthful when status changes.

## 10. Token efficiency

Read this file first; read only docs relevant to the task; targeted searches over full-repo exploration; do not reread unchanged files; no unnecessary summaries or large docs; concise plans and reports.

## 11. Definition of done

- [ ] Requirement met and behavior demonstrated (command/output shown)
- [ ] Regression test added for any bug fixed; full `pytest` green
- [ ] No new unverified dependency; `requirements.txt` accurate
- [ ] No secrets, unsafe input handling or raw-user-data logging added
- [ ] No frozen decision changed; layering respected
- [ ] `CURRENT_STATE.md` / README status updated if state changed
- [ ] Report states what was verified and what was not