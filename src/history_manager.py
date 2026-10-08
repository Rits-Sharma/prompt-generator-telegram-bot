import os
import json
import datetime

HISTORY_FILE = 'prompt_history.json'

def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [(item['prompt'], datetime.datetime.fromisoformat(item['timestamp'])) for item in data]
        except Exception:
            return []
    return []

def save_history(history):
    data = [{'prompt': prompt, 'timestamp': time.isoformat()} for prompt, time in history]
    try:
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        pass
