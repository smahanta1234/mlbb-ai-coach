from src.data_loader import items_data


def get_all_items():
    return items_data


def get_items_by_category(category):
    return items_data.get(category, {})


def find_item(item_name):
    for category, items in items_data.items():
        for item in items:
            if item.lower() == item_name.lower():
                return items[item]

    return None


def get_boots():
    return get_items_by_category("Movement")


def get_attack_items():
    return get_items_by_category("Attack")


def get_magic_items():
    return get_items_by_category("Magic")


def get_defense_items():
    return get_items_by_category("Defense")


def build_item_context():
    context = []

    for category, items in items_data.items():
        context.append(f"{category} Items:")

        for item_name, item_data in items.items():
            cost = item_data.get("cost", "Unknown")
            item_type = item_data.get("type", "Unknown")

            context.append(
                f"- {item_name} "
                f"(Type: {item_type}, Cost: {cost})"
            )

        context.append("")

    return "\n".join(context)