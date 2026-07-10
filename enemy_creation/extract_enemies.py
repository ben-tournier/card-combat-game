import json
from pathlib import Path
from enemy_creation.enemy import Enemy

# This function will load all of the enemies into the game and sort them based on normal, elite, or boss level difficulty
def load_enemies():

    file_path = Path(__file__).parent / "enemy_info.json"

    with open(file_path, "r") as f:
        data = json.load(f)

    enemy_pools = {
        "normal": [],
        "elite": [],
        "boss": []}


    for category in enemy_pools:

        for enemy in data[category]:

            enemy_pools[category].append(
                Enemy(
                    name=enemy["name"],
                    hp=enemy["hp"],
                    damage=enemy["damage"],
                    block=enemy.get("block", 0),
                    value=enemy["value"],
                    behavior=enemy.get("behavior", "attack")))


    return enemy_pools