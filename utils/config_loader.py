# Python file placeholder

import json

def load_config(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)
