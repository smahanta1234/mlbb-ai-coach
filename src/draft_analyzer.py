from src.data_loader import heroes_data


def _extract_team_features(team):
    """
    Converts a team into aggregated draft features
    """

    roles = []
    playstyles = []

    heroes = heroes_data["heroes"]

    for hero in team:
        if hero not in heroes:
            continue

        roles.extend(heroes[hero].get("roles", []))
        playstyles.extend(heroes[hero].get("playstyles", []))

    return {
        "roles": roles,
        "playstyles": playstyles
    }


def analyze_draft(hero, ally_team, enemy_team):
    """
    Returns structured draft intelligence (NOT text)
    """

    heroes = heroes_data["heroes"]

    enemy_features = _extract_team_features(enemy_team)
    ally_features = _extract_team_features(ally_team)

    enemy_roles = enemy_features["roles"]
    enemy_playstyles = enemy_features["playstyles"]

    ally_roles = ally_features["roles"]
    ally_playstyles = ally_features["playstyles"]

    enemy_strengths = []
    enemy_weaknesses = []
    ally_strengths = []
    recommendations = []

    # -------------------------
    # ENEMY ANALYSIS
    # -------------------------
    if "Tank" in enemy_roles and "Mage" in enemy_roles:
        enemy_strengths.append("Balanced frontline + magic damage")

    if "Assassin" in enemy_roles:
        enemy_strengths.append("High pickoff threat")

    if "Sustain" in enemy_playstyles:
        enemy_strengths.append("Sustained fights")

    if "No Tank" in enemy_roles:
        enemy_weaknesses.append("Lack of frontline")

    if "Low Crowd Control" in enemy_playstyles:
        enemy_weaknesses.append("Weak engage/disengage")

    # -------------------------
    # ALLY ANALYSIS
    # -------------------------
    if "Tank" in ally_roles:
        ally_strengths.append("Frontline presence")

    if "Teamfight" in ally_playstyles:
        ally_strengths.append("Strong grouped fights")

    if "Burst" in ally_playstyles:
        ally_strengths.append("High pick potential")

    # -------------------------
    # HERO RECOMMENDATION (your existing logic)
    # -------------------------

    enemy_roles_set = set(enemy_roles)
    enemy_playstyles_set = set(enemy_playstyles)

    for hero_name, data in heroes.items():

        hero_roles = data.get("roles", [])
        hero_playstyles = data.get("playstyles", [])

        score = 0

        if "Tank" in enemy_roles_set and "Marksman" in hero_roles:
            score += 2

        if "Assassin" in enemy_roles_set and "Tank" in hero_roles:
            score += 2

        if "Mage" in enemy_roles_set and "Assassin" in hero_roles:
            score += 2

        if "Burst" in enemy_playstyles_set and "Tank" in hero_roles:
            score += 2

        if "High Mobility" in enemy_playstyles_set and "Crowd Control" in hero_playstyles:
            score += 3

        if score > 0:
            recommendations.append((hero_name, score))

    recommendations.sort(key=lambda x: x[1], reverse=True)

    return {
        "enemy_strengths": enemy_strengths,
        "enemy_weaknesses": enemy_weaknesses,
        "ally_strengths": ally_strengths,
        "recommendations": [h for h, _ in recommendations[:5]],
        "win_conditions": [
            "Play around draft advantages",
            "Avoid losing early fights",
            "Focus objectives after winning skirmishes"
        ]
    }