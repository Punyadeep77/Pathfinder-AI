🧭 Pathfinder AI
An evidence-driven career decision-intelligence platform.
Pathfinder takes a person's situation in plain language — skills, education or experience, interests, what they don't want, time available — and evaluates career directions against structured career and labor-market data. Every result comes with evidence. An LLM can then explain and discuss the result, but it never makes the decision.
Status: V1 backend works (terminal). V2 (UI, market-data pipeline, dashboard, LLM explanation) is in progress. See Current Status for exactly what is real today. Nothing in this README is claimed as done unless it appears in the "Working" column.
Why it exists
People choosing a career get conflicting advice ("learn DSA", "DSA doesn't matter", "AI is the future"). The problem is not missing information — it is missing personalized, evidence-based decision-making. Pathfinder asks:
Given this person's actual profile, constraints, preferences, timeline and market reality, which career directions make sense right now?
Core principles (frozen)
Discover before you learn — the user does not have to pick a target career first.
Evidence before recommendation — every verdict has traceable reasons and a data source.
What you don't want matters as much as what you want — a fundamental conflict excludes a role; it is not a small score penalty.
Reality over motivation — if the timeline or skills make a path unrealistic, Pathfinder says so and shows the closest realistic alternative.
The LLM explains; it does not decide.
Not a chatbot, not a career quiz, not a roadmap generator, not a skill-gap calculator.
How it works
text
Natural-language input
      ↓
Input understanding  →  user type (student / fresher / working professional / career switcher)
      ↓
Extraction (skills, education, timeline, interests, positive & negative preferences)
      ↓
Missing-information check  →  ask ONLY what is genuinely missing
      ↓
Career Identity
      ↓
Market Reality  (role data + market evidence, with source and date)
      ↓
Verdict Engine  (rule-based, explainable)
      ↓
Personalized dashboard
   ├─ Primary recommendations
   ├─ Excluded / low-priority paths (and why)
   └─ Explore More Options (clearly separate from the verdict)
      ↓
LLM discussion (explains verified results only)
Data pipeline (separate from decision logic):
text
Sources → Scraper → Raw data → Validate → Clean → Normalize (titles, skills)
       → Structured dataset → SQLite → Analytics / ML → Decision engines
Decision engines depend on normalized data, never on a specific source. Swapping seed data for scraped data must not change engine code.
Example situations
User	What Pathfinder should show
Graduate with Python/Pandas skills and two certifications	Current position, compatible roles across domains, required stacks, gaps, timeline, market evidence
2nd/3rd-year student who doesn't know the direction	Career directions discovered from interests, dislikes, skills, stage and time; why each fits
Working professional wanting a higher salary	Transferable skills, target roles, transition difficulty, gaps, realistic timeline
Each user type gets a different dashboard, because their situation is different.
Update Market Data (V2)
Update Market Data → scrapers run → data validated and cleaned → new dataset versioned → database updated. If scraping fails (no internet, source blocked, parsing error), Pathfinder shows a clear status message and keeps using the last successfully validated dataset. It never breaks and never silently uses partial data.
Multi-domain
The schema and engines are domain-neutral. Technology is first because data is available; healthcare, law and other domains are added by adding data, not by changing engines.
Current Status
Area	Working	Partial / Known issues	Planned
Natural-language input (terminal)	✅ basic regex extraction	Branch, "final year", multiple timelines and fallback offers are not extracted	spaCy / validated LLM extraction
Career Identity, Reality, Verdict engines	✅	Skill matching is exact-string, proficiency is ignored	Skill families, proficiency weighting
Negative preferences (hard exclusion)	⚠️ not reliable yet	Preference text is not mapped to structured role fields	Canonical preference → role-field mapping
Seed data (24 IT roles, 91 skills)	✅ hand-curated bootstrap	IT-only; market scores are seed values, not measured	Scraped, multi-domain data
ETL → SQLite	✅	One-command run via pipeline.py	Dataset versioning + fallback
Scraper	❌	—	V2
Analytics / ML	❌	—	V2, only where justified and evaluated
Streamlit UI / dashboard	⚠️ placeholder page only	—	First milestone
LLM discussion layer	❌	—	V2
Data provenance: all market numbers today are seed values, not live market data. The dashboard labels the source and date of every evidence figure.
Known limitations (kept honest)
Career-interest extraction can misfire on branch names (e.g. "CSE (Data Science)" read as an interest).
Recommendations for users with no skills, or from non-IT backgrounds, are weak because the dataset is IT-only.
Ranking weights are manually chosen and not yet validated against real data.
Tech stack (V2 is local-first and costs ₹0)
Area	Choice
Language / data	Python, Pandas, NumPy
Storage	SQLite (SQLAlchemy only if it earns its place)
Collection	requests/BeautifulSoup, Scrapy or Playwright where a source needs it
Analytics / ML	scikit-learn, only for an evaluated, justified task (e.g. skill-demand or role similarity)
LLM	Local open-weight model via Ollama; small enough for the dev machine
UI	Streamlit + Plotly
Quality	pytest, Git/GitHub
No paid APIs, no cloud services, no secrets required to run. Anything beyond this list needs a recorded decision in docs/DECISIONS.md.
Not in scope for V2 (this is V3): production infrastructure, continuous scraping, authentication, scale, commercial features.
Quick start
bash
git clone https://github.com/Punyadeep77/Pathfinder-AI.git
cd Pathfinder-AI
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env            # no secrets needed for local use

python pipeline.py              # generate seed data → ETL → SQLite
python main.py                  # terminal mode
streamlit run app.py            # UI (first milestone, in progress)
pytest                          # run the test suite
If any command fails on a fresh clone, that is a bug — please open an issue.
Repository layout
text
config/     constants, settings, logging
data/       seed/ raw/ processed/ database/   (generated data is git-ignored)
docs/       DECISIONS.md, ARCHITECTURE.md, CURRENT_STATE.md, PROJECT_CONTEXT.md
scripts/    dataset generators
src/
  context/    understanding: extraction, user type, constraints, clarification
  engines/    identity, reality, verdict   (pure rules, no I/O, no LLM)
  models/     dataclasses shared across layers
  services/   orchestration (the only layer the UI calls)
  database/   connection, schema, loader, queries
  utils/      ETL, validation, preprocessing
tests/
Layering rule: UI → services → engines/context → models/database. Engines never import the LLM, the UI or the scraper.
Engineering guarantees
Explainable decisions: verdicts come from deterministic rules with visible evidence.
Validated data only: data failing validation is rejected, not silently fixed.
Fail safe: scraper/LLM failure degrades gracefully; the core analysis still runs.
Reproducible: pinned direct dependencies, one-command setup, tests for every bug fixed.
Private by default: user input stays on the local machine; raw user text is not written to logs.
Roadmap
Milestone 1 — Demo UI: Streamlit page over the existing backend (input → analysis → results).
Fix input understanding and negative-preference constraints.
Market-data pipeline, Update Market Data, dataset versioning and fallback.
Personalized dashboard and Explore More Options.
Evaluated ML component.
LLM explanation/discussion layer.
License / Author
Author: Punyadeep Kaushik. License: to be decided before the repository is made public.