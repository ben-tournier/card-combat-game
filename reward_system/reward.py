from reward_system.reward_choices import add_card, remove_card, upgrade_card
import random, os, time

def clear_terminal():
    time.sleep(.5)
    os.system("cls")

def boss_reward(player):
    print("Boss defeated!")
    player.max_energy += 1
    print(f"Maximum energy has increased to {player.max_energy}")

def elite_reward(player):

    print("Elite defeated!")
    player.deck.change_hand_size(1)
    print(f"Your hand has been expanded to hold {player.deck.hand_size}")


# This function will happen after a user successsfuly gets through a floor of combar 
# It will cleanup money for the user, heal, and offer a deck change
def reward(game):
    player = game.player
    
    player.cleanup_gold()

    # Every cleared floor the user will heal up 5 hp
    player.heal(5)
    print(f"{player.name} healed 5 hp")

    # let user know funding before going through shops and whatnot
    print(f"\nYou currently have {player.gold} gold")

    if game.is_boss_floor():
        boss_reward(player)
    elif game.is_elite_floor():
        elite_reward(player)


    add_card(player)

    upgrade_card(player)
   
    remove_card(player)

    # cleans up screen after reward
    clear_terminal()
