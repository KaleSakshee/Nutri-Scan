import json
import os

HISTORY_FILE = 'search_history.json'

def save_search(user_id, product_name, analysis):
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            history = json.load(f)
    else:
        history = {}

    if user_id not in history:
        history[user_id] = []

    history[user_id].append({
        'product': product_name,
        'analysis': analysis
    })

    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)

def get_search_history(user_id):
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            history = json.load(f)
        return history.get(user_id, [])
    return []
