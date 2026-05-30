import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def load_json(filename):
    filepath = DATA_DIR / filename

    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


heroes_data = load_json("heroes.json")
items_data = load_json("items.json")
emblems_data = load_json("emblems.json")
meta_data = load_json("meta.json")