import json
from pathlib import Path


def load_language(language = "English"):
    data_path = Path(__file__).resolve().parent.parent / "data" / "english.json"
    
    with open(data_path, "r") as file:
        return json.load(file)
    
    
    
def build_lookup():
    lookup = {}

    for category in ["letters", "numbers", "special_characters"]:
        lookup.update(load_language().get(category, {}))

    return lookup