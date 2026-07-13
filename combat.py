from utilities.check_index import check_index
import os, time

def clear_terminal():
    time.sleep(.5)
    os.system("cls")


# This function carries a lot of the real weight for the actual game loop
# The start of the turn, end of the turn, and combat itself are all kept inside of here
def combat(user, enemies):
    user.deck.draw_hand()

    user.fill_energy()
    print(f"Energy has been set to {user.max_energy} energy.")
    # The outside for loop is what both allows the player and limits them to playing 3 cards each turn 
    while user.energy > 0:
        
        # the location of this clear terminal call will wipe the board clean right before reanouncing what the user is playing against
        # it should wipe the text every time that a card has been played
        clear_terminal()
        
        user.combat_state()

        print(f"\n You currently have {user.current_energy()} energy ")

        print("\n You are facing:")
        # This will pring out all enemies individually with an associated number but only if they are still alive
        for index, enemy in enumerate(enemies): 
            if enemy.is_alive():
                if enemy.check_block() > 0:
                    print(f"{index + 1}: {enemy} and has: {enemy.check_block()} block")
                else:
                    print(f"{index + 1}: {enemy}")

        print("\n Your cards in hand: \n" + user.relay_cards_in_hand())

        # This will get the index that the user wants to use while also checking to make sure it is valid
        card_choice = check_index(user)


        # This will figure out if the card type is going to deal damage and if it is then it will ask for a target
        # There is now a check in here if there is only 1 enemy left alive so that the user does not have to chose and the damage will just be delt
        if user.check_card_damage(card_choice - 1):

            alive_enemies = []

            for enemy in enemies:
                if enemy.is_alive():
                    alive_enemies.append(enemy)

            if len(alive_enemies) == 1:
                target = alive_enemies[0]

            else:
                target = int(input("Which enemy would you like to target? "))
                target = alive_enemies[target - 1]

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


    for enemy in enemies: 
        if enemy.is_alive():
            if enemy.check_attack():
                user.take_damage(enemy)

    time.sleep(2)

    user.remove_all_block()

    # this should break out of the combat system if the player dies
    if user.player_dead():
        return False
                
    return True