from player import Player
from enemy_creation.enemy_pool import generate_encounter

# This function carries a lot of the real weight for the actual game loop
# The start of the turn, end of the turn, and combat itself are all kept inside of here
def combat(user, enemies):
    user.start_of_turn()
    
    # The outside for loop is what both allows the player and limits them to playing 3 cards each turn 
    for card in range(3):
        print(f"\n You currently have {user.block} block and {user.hp} hp")

        print("\n You are facing:")
        # This will pring out all enemies individually with an associated number but only if they are still alive
        for index, enemy in enumerate(enemies): 
            if enemy.is_alive():
                print(f"{index + 1}: {enemy}")

        print("\n Your cards in hand: \n" + user.relay_cards_in_hand())
        card_choice = int(input("\n Which card would you like to play?: "))
        #Add check for valid input later

        # This will figure out if the card type is going to deal damage and if it is then it will ask for a target
        if user.check_card_damage(card_choice - 1):
            target = int(input("Which enemy would you like to target? "))
            target = enemies[target - 1]
            user.play_card(card_choice, target)
        else:
            user.play_card(card_choice, None)

        # This loop is just like one above but should make sure that there is at least one enemy remaining
        enemies_alive = 0 
        for enemy in enemies:
            if enemy.is_alive():
                enemies_alive += 1

        if enemies_alive == 0:
            return False
    
    # This is the point after the user has played all of the cards in hand
    user.end_of_turn()

    print("Enemies turn")



def startup():
    name = input("Hello there, what name would you like to use? ")
    user = Player(name)
    return user


def run():
    user = startup()
    current_floor = 1

    while True:
        enemies = generate_encounter(current_floor)
        enemies_alive =  True 

        while enemies_alive:
            enemies_alive = combat(user, enemies)
        
        current_floor += 1 

    

run()