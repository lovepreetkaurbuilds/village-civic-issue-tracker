import json
from pathlib import Path


DATA_FILE = Path("data/issues.json")


def load_issues():
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_issues(issues):
    DATA_FILE.parent.mkdir(exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(issues, file, indent=4)