from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.guide_generator import generate_guide

app = FastAPI(
    title="MLBB AI Coach API"
)

# allow React frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/generate-guide")
def generate(data: dict):

    result = generate_guide(
        transcript=data.get("transcript", ""),
        hero=data.get("hero", ""),
        lane=data.get("lane", ""),
        playstyle=data.get("playstyle", []),
        guide_type=data.get("guide_type", ""),
        difficulty=data.get("difficulty", ""),
        ally_team=data.get("ally_team", []),
        enemy_team=data.get("enemy_team", [])
    )

    return {
        "guide": result
    }


@app.get("/")
def home():
    return {
        "message": "MLBB AI Coach API running"
    }