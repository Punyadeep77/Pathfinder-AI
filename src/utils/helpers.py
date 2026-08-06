from pathlib import Path
import json


def ensure_directory(path: str | Path):
    """
    Create directory if it does not exist.
    """
    Path(path).mkdir(parents=True, exist_ok=True)


def load_json(path: str | Path):
    """
    Load JSON file.
    """
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(data, path: str | Path):
    """
    Save JSON file.
    """
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def split_pipe_values(value):
    """
    Convert pipe-separated string into list.
    """
    if not value:
        return []

    return [
        item.strip()
        for item in str(value).split("|")
        if item.strip()
    ]


def join_pipe_values(values):
    """
    Convert list into pipe-separated string.
    """
    if not values:
        return ""

    return "|".join(values)