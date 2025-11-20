
import json

def load_config():
    with open("settings.json") as f:
        return json.load(f)
