import json
import os

PROFILE_FILE = 'user_profiles.json'

def get_user_profile(user_id):
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, 'r') as f:
            profiles = json.load(f)
        return profiles.get(user_id, {}).get('allergies', [])
    return []

def save_user_profile(user_id, profile_data):
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, 'r') as f:
            profiles = json.load(f)
    else:
        profiles = {}

    profiles[user_id] = profile_data

    with open(PROFILE_FILE, 'w') as f:
        json.dump(profiles, f, indent=2)
