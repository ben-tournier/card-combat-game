from player import Player
from enemy_creation.enemy import Enemy
from enemy_creation.enemy_pool import generate_encounter

# This functin gets everything organized at the beginning creating player object and getting name
def startup():
    name = input("Hello there, what name would you like to use? ")
    user = Player(name)
    return user

# This function carries a lot of the real weight for the actual game loop
# The start of the turn, end of the turn, and combat itself are all kept inside of here
def combat(user, enemies):
    user.start_of_turn()
    
    # The outside for loop is what both allows the player and limits them to playing 3 cards each turn 
    for card in range(3):
        user.combat_state()

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
            user.end_of_turn()
            return False
    
    # This is the point after the user has played all of the cards in hand
    user.end_of_turn()

    print("Enemies turn")

    for enemy in enemies: 
        if enemy.check_attack():
            user.take_damage(enemy)

    return True

# This function will happen after a user successsfuly gets through a floor of combar 
# It will cleanup money for the user, heal, and offer a deck change
def reward(user):
    user.cleanup_gold()
    
    options = ["Heal up 5 hp", "Buy a new card", "Upgrade an existing card"]
    print(f"You currently have {user.gold} gold")
    
    for index, choice in enumerate(options):
        print(f"{index+1} {choice}")

    choice = int(input("What would you like to do? "))


    if choice == 1:
        print(user.heal(5))

    elif choice == 2: 
        print("Sorry Option Currently Unavailible")

    else:
        #print out full deck and ask which card wanted to upgrade
        #replace card chosen
        #must figure out way to change card so able to tell difference (Ex. 'strike' vs 'strike+')



def run():
    user = startup()
    current_floor = 1

    while True:
        enemies = generate_encounter(current_floor)
        enemies_alive =  True 

        while enemies_alive:
            enemies_alive = combat(user, enemies)
        
        reward(user)
        
        current_floor += 1 

    

run()