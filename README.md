# 🎮 MLBB AI Coach

An AI-powered gameplay coaching platform for Mobile Legends: Bang Bang (MLBB) that analyzes gameplay context, hero selection, draft composition, and player preferences to generate intelligent coaching reports.

The project currently includes:

- ✅ Fully functional Streamlit application
- 🚧 React + FastAPI migration in progress
- ✅ Retrieval-Augmented Generation (RAG)
- ✅ AI-powered gameplay analysis
- ✅ Draft intelligence system
- ✅ Hero, item, and emblem recommendation systems

Built using Python, Streamlit, FastAPI, React, and LLM-based AI workflows.

---

## Current Project Status

| Component | Status |
|------------|---------|
| Streamlit App | ✅ Complete |
| AI Guide Generation | ✅ Complete |
| Draft Analysis | ✅ Complete |
| Hero Intelligence System | ✅ Complete |
| RAG Pipeline | ✅ Complete |
| Item Recommendations | ✅ Complete |
| Emblem Recommendations | ✅ Complete |
| FastAPI Backend | 🚧 In Progress |
| React Frontend | 🚧 In Progress |
| Voice Features | 🚧 Planned |

---

## Features

### 🤖 AI Gameplay Coaching
- Generates structured gameplay reports
- Macro and micro gameplay analysis
- Improvement recommendations
- Matchup advice
- Educational coaching

### ⚔️ Draft Intelligence
- Ally and enemy team analysis
- Counter-pick evaluation
- Synergy analysis
- Matchup insights

### 🧠 Hero Intelligence System
- Hero validation
- Meta tier evaluation
- Role and lane compatibility
- Playstyle analysis

### 🛡️ Recommendation Systems
- Item recommendations
- Emblem recommendations
- Situational build suggestions

### 📚 Retrieval-Augmented Generation (RAG)
- Retrieves MLBB knowledge from local knowledge base
- Injects contextual information into prompts
- Improves guide quality and relevance

### 🎙️ Planned Features
- Voice analysis
- Speech-to-text gameplay input
- Audio coaching output
- Live draft assistant

---

## Tech Stack

### AI / ML
- LLM-powered guide generation
- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- Recommendation Systems
- NLP workflows

### Backend
- Python
- FastAPI
- Requests
- dotenv
- OpenRouter API

### Frontend
- React
- Vite
- TailwindCSS

### Streamlit
- Streamlit UI
- Interactive dashboard components

---

## Project Structure

```text
mlbb-ai-coach/
│
├── app.py                    # Streamlit app
├── api.py                    # FastAPI backend
│
├── src/
│   ├── guide_generator.py
│   ├── rag_pipeline.py
│   ├── hero_system.py
│   ├── draft_analyzer.py
│   ├── item_system.py
│   ├── emblem_system.py
│   └── context_builder.py
│
├── data/
├── knowledge_base/
│
├── mlbb-coach-ui/            # React frontend
│
├── .env.example
├── README.md
└── .gitignore
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/smahanta1234/mlbb-ai-coach.git

cd mlbb-ai-coach
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

Mac/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

Install backend dependencies:

```bash
pip install -r requirements.txt
```

Install React dependencies:

```bash
cd mlbb-coach-ui
npm install
```

---

## Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openrouter_api_key
OPENAI_BASE_URL=https://openrouter.ai/api/v1/chat/completions
```

---

## Run Streamlit App

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## Run FastAPI Backend

```bash
uvicorn api:app --reload
```

Open:

```text
http://localhost:8000
```

---

## Run React Frontend

```bash
cd mlbb-coach-ui

npm run dev
```

Open:

```text
http://localhost:5173
```

---

## Sample Workflow

1. Select hero and lane
2. Select playstyle
3. Add ally and enemy draft
4. Add gameplay transcript
5. Generate AI coaching report

---

## Future Improvements

- Complete React migration
- Voice coaching
- Live draft assistant
- Streaming responses
- Match history integration
- User authentication
- Analytics dashboard
- Deployment

---

## Author

**Sankalpa Mahanta**

GitHub:
https://github.com/smahanta1234

---

## Disclaimer

Mobile Legends: Bang Bang and related assets are trademarks of their respective owners. This project is an independent educational and portfolio project and is not affiliated with or endorsed by Moonton.
