from src.data_loader import heroes_data, meta_data


def get_hero_data(hero_name):
    heroes = heroes_data.get("heroes", {})

    for hero in heroes:
        if hero.lower() == hero_name.lower():
            return heroes[hero]

    return None


def validate_hero(
    hero_name,
    lane=None,
    playstyle=None
):

    hero_info = get_hero_data(hero_name)

    if not hero_info:
        return False, f"{hero_name} does not exist."

    valid_lanes = hero_info.get("lanes", [])

    if lane and lane != "Auto Detect":

        if lane not in valid_lanes:

            return (
                False,
                f"{hero_name} is not commonly played in {lane} lane."
            )

    return True, "Valid hero selection"


def get_hero_meta_tier(hero_name):

    for tier, heroes in meta_data.items():

        for hero in heroes:

            if hero.lower() == hero_name.lower():
                return tier

    return "Unknown"


def build_hero_context(hero_name):

    hero_info = get_hero_data(hero_name)

    if not hero_info:
        return ""

    meta_tier = get_hero_meta_tier(hero_name)

    playstyles_text = "\n- ".join(
        hero_info.get("playstyles", [])
    )

    return f"""
Hero Intelligence Data

Hero:
{hero_name}

Roles:
{", ".join(hero_info.get("roles", []))}

Recommended Lanes:
{", ".join(hero_info.get("lanes", []))}

Playstyles:
- {playstyles_text}

Difficulty:
{hero_info.get("difficulty", "Unknown")}

Current Meta Tier:
{meta_tier}
"""