import random 
from enemy_creation.extract_enemies import load_enemies

ALL_ENEMIES = load_enemies()

def generate_encounter(floor):
    if floor <= 1:
        pool = ALL_ENEMIES[:2]
        count = 1
    
    elif floor <= 3:
        pool = ALL_ENEMIES[:4]

    else:
        pool = ALL_ENEMIES
        count = 2

    return random.choices(pool, k=count)