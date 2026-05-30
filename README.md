# 🎮 MLBB AI Coach

An AI-powered gameplay coaching platform for Mobile Legends: Bang Bang (MLBB) that analyzes gameplay context, draft composition, hero selection, and player preferences to generate intelligent coaching reports.

Built using FastAPI, React, Retrieval-Augmented Generation (RAG), and LLM-powered analysis.

---

## Features

### 🤖 AI Gameplay Coaching
- Generates structured gameplay reports
- Provides macro and micro strategy recommendations
- Explains strengths and weaknesses
- Suggests improvement plans

### ⚔️ Draft Intelligence
- Analyzes ally and enemy team compositions
- Evaluates hero synergies and counters
- Provides matchup insights

### 🧠 Hero Intelligence System
- Hero validation
- Role and lane compatibility
- Meta tier information
- Playstyle analysis

### 🛡️ Build Recommendations
- Item recommendations
- Emblem recommendations
- Situational build guidance

### 📚 Retrieval-Augmented Generation (RAG)
- Retrieves relevant MLBB knowledge
- Injects contextual information into prompts
- Produces more informed responses

### 🎙️ Planned Features
- Voice analysis
- Speech-to-text gameplay input
- Audio coaching output
- Enhanced live draft assistant

---

## Tech Stack

### Backend
- Python
- FastAPI
- OpenRouter API
- Requests
- dotenv

### Frontend
- React
- Vite
- TailwindCSS

### AI / ML
- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- Context Builders
- Recommendation Systems

---

## Project Structure

```text
mlbb-ai-coach/
│
├── api.py
├── src/
│   ├── guide_generator.py
│   ├── rag_pipeline.py
│   ├── hero_system.py
│   ├── draft_analyzer.py
│   ├── item_system.py
│   ├── emblem_system.py
│   └── context_builder.py
│
├── knowledge_base/
├── data/
│
├── mlbb-coach-ui/
│   ├── src/
│   └── components/
│
├── .env.example
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/smahanta1234/mlbb-ai-coach.git
cd mlbb-ai-coach
```

Create a virtual environment:

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

Install frontend dependencies:

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

## Run Backend

```bash
uvicorn api:app --reload
```

Backend:

```text
http://localhost:8000
```

---

## Run Frontend

```bash
cd mlbb-coach-ui
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

## Sample Workflow

1. Select hero and lane
2. Choose playstyle
3. Add ally and enemy draft information
4. Provide gameplay transcript
5. Generate AI coaching report

---

## Future Improvements

- Live draft assistant
- Match history integration
- Voice coaching
- Streaming responses
- User accounts
- Analytics dashboard
- Deployment

---

## Author

**Sankalpa Mahanta**

GitHub:
https://github.com/smahanta1234
