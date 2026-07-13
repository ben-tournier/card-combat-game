import time
from player import Player
from enemy_creation.enemy_pool import generate_encounter
from utilities.floor_view import floor_display
from combat import combat
from reward import reward
# Used to clear terminal and keep things clean throughout
import os


def clear_terminal():
    time.sleep(.5)
    os.system("cls")

# This function gets everything organized at the beginning creating player object and getting name
def startup():
    name = input("What is your name warrior?  ")
    user = Player(name)
    return user


def run():
    user = startup()
    clear_terminal()
    current_floor = 1

    while True:

        floor_display(current_floor)

        time.sleep(2)

        enemies = generate_encounter(current_floor)
        enemies_alive =  True 

        while enemies_alive:
            enemies_alive = combat(user, enemies)
        
        # before celebrating the loop can also be broken if the player is dead 
        if user.player_dead():
            break

        #cleanup after combat 
        clear_terminal()

        #go to reward system
        reward(user)
        
        #next floor
        current_floor += 1 

    

# run()