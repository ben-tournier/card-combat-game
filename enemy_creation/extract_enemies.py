import json
from pathlib import Path
from enemy_creation.enemy import Enemy


def load_enemies(include_elite=True, include_boss=True):
    file_path = Path(__file__).parent / "enemy_info.json"

    with open(file_path, "r") as f:
        data = json.load(f)

    enemies = []


    for enemy in data["normal"]:
        enemies.append(Enemy(
            name=enemy["name"],
            hp=enemy["hp"],
            damage=enemy["damage"],
            block=enemy.get("block", 0),
            value=enemy["value"],
            behavior=enemy.get("behavior", "attack")
        ))

    return enemies


