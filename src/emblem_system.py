from src.data_loader import emblems_data


def get_all_emblems():
    return emblems_data


def get_emblem(emblem_name):
    for emblem in emblems_data:
        if emblem.lower() == emblem_name.lower():
            return emblems_data[emblem]

    return None


def get_core_talents(emblem_name):
    emblem = get_emblem(emblem_name)

    if not emblem:
        return {}

    return emblem.get("coreTalents", {})


def get_standard_talents(emblem_name):
    emblem = get_emblem(emblem_name)

    if not emblem:
        return {}

    return emblem.get("standardTalents", {})


def build_emblem_context():
    context = []

    for emblem_name, emblem_data in emblems_data.items():
        context.append(f"{emblem_name}")
        context.append("")

        attributes = emblem_data.get("attributes", {})

        context.append("Attributes:")

        for attr, value in attributes.items():
            context.append(f"- {attr}: {value}")

        context.append("")
        context.append("Standard Talents:")

        for talent, data in emblem_data.get("standardTalents", {}).items():
            context.append(f"- {talent}: {data.get('effect', '')}")

        context.append("")
        context.append("Core Talents:")

        for talent, data in emblem_data.get("coreTalents", {}).items():
            context.append(f"- {talent}: {data.get('effect', '')}")

        context.append("")
        context.append("-----------------------------------")
        context.append("")

    return "\n".join(context)