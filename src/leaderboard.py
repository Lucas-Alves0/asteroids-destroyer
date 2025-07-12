from config import *
import json
import os

leaderboard_file = 'leaderboard.json'
max_entries = 5

def load_leaderboard():
    if not os.path.exists(leaderboard_file):
        return []

    try:
        with open(leaderboard_file, 'r') as f:
            data = f.read().strip()
            if not data:
                return []
            return json.loads(data)
    except json.JSONDecodeError:
        print("⚠️ leaderboard.json corrompido. Resetando...")
        return []

def save_leaderboard(entries):
    with open(leaderboard_file, 'w') as f:
        json.dump(entries, f, indent=4)

def add_score(name, score):
    leaderboard = load_leaderboard()

    existing_entry = next((entry for entry in leaderboard if entry['name'] == name), None)
    if existing_entry:
        if score > existing_entry['score']:
            existing_entry['score'] = score
    else:
        leaderboard.append({'name': name, 'score': score})

    leaderboard = sorted(leaderboard, key=lambda x: x['score'], reverse=True)
    leaderboard = leaderboard[:max_entries]
    save_leaderboard(leaderboard)

def is_highest_score(score):
    leaderboard = load_leaderboard()
    return len(leaderboard) < max_entries or score > leaderboard[-1]['score']