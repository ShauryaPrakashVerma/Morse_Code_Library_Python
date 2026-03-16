import json
from pathlib import Path


def load_language(language = "english"):
    language = language.lower()
    
    data_path = Path(__file__).resolve().parent.parent / "data" / f"{language}.json"
    
    with open(data_path, "r", encoding="utf-8") as file:
        return json.load(file)
    
    
    
def build_lookup(language = "english"):
    morse_data = load_language(language)
    
    lookup = {}

    for category in ["letters", "numbers", "special_characters"]:
        lookup.update(morse_data.get(category, {}))

    return lookup



# lru cache --->  read, learn about this. Implement it