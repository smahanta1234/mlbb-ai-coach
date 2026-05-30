from src.data_loader import items_data, emblems_data


def get_relevant_items(hero, lane, playstyle):
    """
    Lightweight filtering of items based on hero intent
    """

    items = []

    # simple heuristic mapping (we improve later)
    if "Mage" in playstyle or lane == "Mid Lane":
        items.extend(items_data.get("Magic", {}).keys())

    if "Marksman" in playstyle or lane == "Gold Lane":
        items.extend(items_data.get("Attack", {}).keys())

    if "Tank" in playstyle or lane == "Roam":
        items.extend(items_data.get("Defense", {}).keys())

    if lane == "Jungle":
        items.extend(items_data.get("Jungling", {}).keys())

    return list(set(items))[:8]


def get_relevant_emblems(hero, playstyle):
    """
    Pick best emblem sets based on hero role intent
    """

    emblems = []

    if "Tank" in playstyle:
        emblems.append("Custom Tank Emblem")

    if "Mage" in playstyle:
        emblems.append("Custom Mage Emblem")

    if "Marksman" in playstyle:
        emblems.append("Custom Marksman Emblem")

    if "Assassin" in playstyle:
        emblems.append("Custom Assassin Emblem")

    if "Support" in playstyle:
        emblems.append("Custom Support Emblem")

    if "Fighter" in playstyle:
        emblems.append("Custom Fighter Emblem")

    return list(set(emblems))