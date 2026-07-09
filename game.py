from player import Player
from enemy_creation.enemy import Enemy
from enemy_creation.enemy_pool import generate_encounter

# This functin gets everything organized at the beginning creating player object and getting name
def startup():
    name = input("Hello there, what name would you like to use? ")
    user = Player(name)
    return user

# this function should be used to check and return the index however if the information is needed it should check for i instead to get the card details if the user needs info
def check_index(user):
    while True:
        choice = input("\nWhich card would you like to play? ").strip().lower()

        # This checks if the user asked for information about the card 
        if choice.startswith("i"):
            number = choice[1:]

            if number.isdigit():
                index = int(number)

                if 1 <= index <= len(user.deck.hand):
                    card = user.deck.hand[index - 1]

                    print()
                    print(card)
                    print()

                    continue

            print("Invalid card number.")
            continue

        # Normal card selection
        if choice.isdigit():
            index = int(choice)

            if 1 <= index <= len(user.deck.hand):
                return index

        print("Please enter a valid card number or i<number>.")
    
# this function saves time making sure the response to given text is either y/n 
def get_valid_input(txt):
    while True:
        response = input(f"{txt} please respond with either y/n: ").lower()
        if response == 'y':
            return True
        if response == 'n':
            return False

        print(f"Error, {response} is not a valid input")

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

    print("Enemies turn")

    for enemy in enemies: 
        if enemy.check_attack():
            user.take_damage(enemy)

    return True


# This function will happen after a user successsfuly gets through a floor of combar 
# It will cleanup money for the user, heal, and offer a deck change
def reward(user):
    user.cleanup_gold()

    # Every cleared floor the user will heal up 5 hp
    user.heal(5)
    print(f"{user.name} healed 5 hp")

    # let user know funding before going through shops and whatnot
    print(f"\nYou currently have {user.gold} gold")





    """
    figures out if the user would like to add a card or not - not always, sometimes thinner deck can be better
    this chunk is going to print out all of the availible cards in a list for the user to chose from - same as combat 'i#' will give info about that #

    
    """
    if get_valid_input("Would you like to add a card?"):

        print("\nAvailable Cards:")

        available_cards = []

        for card_id, versions in user.deck.cards.items():

            # This prevents the starter cards from being shown
            if card_id > 3:
                available_cards.append(card_id)
                print(f"{len(available_cards)}. {versions['basic'].name}")


        while True:

            choice = input("\nWhich card would you like to add? ").strip().lower()


            # This checks if the user wants information about the card
            if choice.startswith("i"):

                number = choice[1:]

                if number.isdigit():

                    index = int(number)

                    if 1 <= index <= len(available_cards):

                        card_id = available_cards[index - 1]

                        card = user.deck.cards[card_id]["basic"]

                        print()
                        print(card)
                        print()

                        continue

                print("Invalid card number.")
                continue



            # Normal card selection
            if choice.isdigit():

                index = int(choice)

                if 1 <= index <= len(available_cards):

                    card_id = available_cards[index - 1]

                    user.deck.add_card(card_id)

                    print(f"{user.deck.cards[card_id]['basic'].name} has been added to your deck!")

                    break


            print("Please enter a valid card number or i<number>.")










    """
    does the user want to upgrade a card? (probably...) and then gives the user all the cards in the deck that can be upgraded
    this section will work a lot like the one above where it will print out the deck that the user currently has and allow them to chose which card they want to upgrade
    same as above 'i#' will get info about that # option
    """
    if get_valid_input("Would you like to upgrade a card?"):

        print("\nYour Deck:")
        print(user.deck.show_full_deck())

        deck = user.deck.get_full_deck()

        while True:
            choice = input("\nWhich card would you like to upgrade? ").strip().lower()

            # This checks if the user wants information about the upgraded card
            if choice.startswith("i"):

                number = choice[1:]

                if number.isdigit():
                    index = int(number)

                    if 1 <= index <= len(deck):

                        card = deck[index - 1]

                        upgraded_card = user.deck.cards[card.card_id]["upgraded"]

                        print()
                        print("Upgraded version:")
                        print(upgraded_card)
                        print()

                        continue

                print("Invalid card number.")
                continue


            # Normal card selection
            if choice.isdigit():

                index = int(choice)

                if 1 <= index <= len(deck):

                    selected_card = deck[index - 1]

                    user.deck.upgrade_card(selected_card)

                    print(f"{selected_card.name} has been upgraded!")
                    break


            print("Please enter a valid card index")





    # this function is still being worked out but will eventually allow for the deck to be shaped how the user wants it to be
    if get_valid_input("Would you like to remove a card?"):
        print("Not implemented yet.")



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