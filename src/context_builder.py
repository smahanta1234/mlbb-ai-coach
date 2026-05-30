from src.hero_system import build_hero_context
from src.rag_pipeline import retrieve_context
from src.draft_analyzer import analyze_draft
from src.build_context import get_relevant_items, get_relevant_emblems


def build_full_context(hero, lane, playstyle, ally_team, enemy_team):
    hero_context = build_hero_context(hero)

    draft_analysis = analyze_draft(hero, ally_team, enemy_team)

    rag_context = retrieve_context(
        f"{hero} {lane} {' '.join(playstyle)}"
    )

    items_context = get_relevant_items(hero, lane, playstyle)
    emblems_context = get_relevant_emblems(hero, playstyle)

    return {
        "hero_context": hero_context,
        "draft_analysis": draft_analysis,
        "rag_context": rag_context,
        "items": items_context,
        "emblems": emblems_context
    }