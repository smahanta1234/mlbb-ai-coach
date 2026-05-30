import os
import requests

from dotenv import load_dotenv

from src.rag_pipeline import retrieve_context
from src.hero_system import validate_hero
from src.context_builder import build_full_context

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENAI_API_KEY")

OPENROUTER_BASE_URL = os.getenv(
    "OPENAI_BASE_URL",
    "https://openrouter.ai/api/v1/chat/completions"
)

MODELS = [
    "deepseek/deepseek-v4-flash:free",
    "google/gemma-4-31b-it:free",
    "nvidia/nemotron-3-super-120b-a12b:free"
]


def generate_guide(
    transcript: str,
    hero: str,
    lane: str,
    playstyle: list,
    guide_type: str,
    difficulty: str,
    ally_team,
    enemy_team
):

    # -------------------------
    # Validate hero selection
    # -------------------------

    is_valid, validation_message = validate_hero(
        hero,
        lane,
        playstyle
    )

    if not is_valid:
        return f"Invalid Setup:\n\n{validation_message}"

    # -------------------------
    # Retrieve RAG knowledge
    # -------------------------

    rag_context = retrieve_context(
        f"{hero} {lane} {' '.join(playstyle)}"
    )

    # -------------------------
    # Build all contexts
    # -------------------------

    context = build_full_context(
        hero=hero,
        lane=lane,
        playstyle=playstyle,
        ally_team=ally_team,
        enemy_team=enemy_team
    )

    hero_context = context.get(
        "hero_context",
        ""
    )

    draft_context = context.get(
        "draft_analysis",
        ""
    )

    items_context = context.get(
        "items",
        []
    )

    emblems_context = context.get(
        "emblems",
        []
    )

    # -------------------------
    # Prompt
    # -------------------------

    prompt = f"""
You are an elite Mobile Legends analyst and coach.

PLAYER SETTINGS

Hero: {hero}
Lane: {lane}
Playstyle: {", ".join(playstyle)}
Guide Type: {guide_type}
Difficulty: {difficulty}

MLBB Knowledge:
{rag_context}

Hero Context:
{hero_context}

Draft Analysis:
{draft_context}

Recommended Items:
{", ".join(items_context)}

Recommended Emblems:
{", ".join(emblems_context)}

GAMEPLAY TRANSCRIPT

{transcript}

Return markdown using:

# Hero Analysis
# Recommended Emblem Setup
# Recommended Build
# Strengths
# Weaknesses
# Macro Strategy
# Micro Strategy
# Common Mistakes
# Improvement Plan
# Matchup Advice
# Beginner FAQ
"""

    headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost:5173",
    "X-Title": "MLBB AI Coach"
}

    last_error = None

    for model_name in MODELS:

        try:

            response = requests.post(
                OPENROUTER_BASE_URL,
                headers=headers,
                json={
                    "model": model_name,
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    "temperature": 0.7,
                    "max_tokens": 700
                },
                timeout=60
            )

            print("MODEL:", model_name)
            print("STATUS:", response.status_code)
            print("RAW RESPONSE:")
            print(response.text)

            if response.status_code != 200:
                last_error = (
                    f"{response.status_code}: "
                    f"{response.text}"
                )
                continue

            try:

                data = response.json()

                if "choices" in data:
                    return data["choices"][0]["message"]["content"]

                last_error = data

            except Exception as e:

                last_error = (
                    f"JSON parse error: {e}\n\n"
                    f"Raw:\n{response.text}"
                )

        except Exception as e:

            last_error = str(e)
            continue

    return f"Error generating guide:\n\n{last_error}"