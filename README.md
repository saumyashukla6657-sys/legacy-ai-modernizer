# 🛡️ Agii AI Modernizer: Legacy Discovery & Audit Workbench (PoC)![Workbench Preview](./dashboard_preview.png)

An AI-powered pre-migration discovery engine designed to de-risk enterprise legacy modernizations. The platform ingests legacy COBOL code, indexes source lines for absolute auditability, and uses structured schema extraction to output verifiable business rules and migration risk registers.

---

## 🚀 Key Architectural Highlights

- **Deterministic Line Indexing:** Automatically prepends zero-padded line coordinates (`0001 | ...`) to enforce audit trails.
- **Pydantic Schema Enforcement:** Replaces unstructured chat text with machine-readable, typed JSON schemas for downstream migration tools.
- **Human-in-the-Loop Workbench:** Streamlit interface pairing raw source code side-by-side with interactive business rule validations and exportable evidence packages.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.11+, LangChain
- **LLM Engine:** Google Gemini API (`gemini-2.0-flash` / `gemini-2.5-flash`)
- **Frontend / Dashboard:** Streamlit
- **Validation:** Pydantic

---

## ⚙️ Quickstart

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)<your-username>/legacy-ai-modernizer.git
   cd legacy-ai-modernizer