import random
from enemy_creation.extract_enemies import load_enemies
from copy import deepcopy

ALL_ENEMIES = load_enemies()


def generate_encounter(floor):

    # Every 10th floor is a boss
    if floor % 10 == 0:
        boss = random.choice(ALL_ENEMIES["boss"])

        return [boss]


    # Every 5th floor is an elite
    elif floor % 5 == 0:
        elite = random.choice(ALL_ENEMIES["elite"])

        return [elite]


    # Normal floors
    else:

        if floor <= 2:
            pool = ALL_ENEMIES["normal"][:3]
            count = 1
        elif floor <= 5:
            pool = ALL_ENEMIES["normal"][:6]
            count = 1
        else:
            pool = ALL_ENEMIES["normal"]
            count = 2

        return [deepcopy(enemy) for enemy in random.sample(pool, count)]