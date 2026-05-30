from src.data_loader import heroes_data


def get_role_color(role):

    colors = {
        "Tank": "🛡️",
        "Fighter": "⚔️",
        "Assassin": "🗡️",
        "Mage": "🔮",
        "Marksman": "🏹",
        "Support": "✨"
    }

    return colors.get(role, "🎮")


def build_hero_card(hero_name):

    heroes = heroes_data["heroes"]

    if hero_name not in heroes:
        return f"❓ {hero_name}"

    data = heroes[hero_name]

    roles = " ".join([get_role_color(r) + r for r in data.get("roles", [])])
    lanes = ", ".join(data.get("lanes", []))

    return f"""
<div class="card">
    <h3>{hero_name}</h3>
    <p><b>Roles:</b> {roles}</p>
    <p><b>Lane:</b> {lanes}</p>
</div>
"""