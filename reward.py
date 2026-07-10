from utilities.check_index import get_valid_input
import random, os, time

def clear_terminal():
    time.sleep(.5)
    os.system("cls")




"""
figures out if the user would like to add a card or not - not always, sometimes thinner deck can be better
this chunk is going to print out all of the availible cards in a list for the user to chose from - same as combat 'i#' will give info about that #
"""
def add_card(user):

    if get_valid_input("Would you like to add a card?"):

        print("\nAvailable Cards:")

        available_cards = []

        for card_id, versions in user.deck.cards.items():

            # This prevents the starter cards from being shown
            if card_id > 3:
                available_cards.append(card_id)

        # This only allows the user to have 3 cards to choose from when adding to the deck
        # The cards are always randomly chosen but always unique from the list of availible cards
        selected_available_cards = random.sample(
            available_cards,
            min(3, len(available_cards))
        )

        # Every time a valid card is found and added to the list it will be printed and offered to the user
        for index, card_id in enumerate(selected_available_cards, start=1):
            print(f"{index}. {user.deck.cards[card_id]['basic'].name}")

        while True:

            choice = input("\nWhich card would you like to add? ").strip().lower()

            # This checks if the user wants information about the card
            if choice.startswith("i"):

                number = choice[1:]

                if number.isdigit():

                    index = int(number)

                    if 1 <= index <= len(selected_available_cards):

                        card_id = selected_available_cards[index - 1]

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

                if 1 <= index <= len(selected_available_cards):

                    card_id = selected_available_cards[index - 1]

                    user.deck.add_card(card_id)

                    print(f"{user.deck.cards[card_id]['basic'].name} has been added to your deck!")

                    break

            print("Please enter a valid card number or i#")


"""
does the user want to upgrade a card? (probably...) and then gives the user all the cards in the deck that can be upgraded
this section will work a lot like the one above where it will print out the deck that the user currently has and allow them to chose which card they want to upgrade
same as above 'i#' will get info about that # option
"""
def upgrade_card(user):

    if get_valid_input("Would you like to upgrade a card?"):

        print("\nYour Deck:")

        available_cards = user.deck.get_random_cards(5)

        for index, card in enumerate(available_cards, start=1):
            print(f"[{index}]. {card.name}")

        while True:
            choice = input("\nWhich card would you like to upgrade? ").strip().lower()

            # This checks if the user wants information about the upgraded card
            if choice.startswith("i"):

                number = choice[1:]

                if number.isdigit():
                    index = int(number)

                    if 1 <= index <= len(available_cards):

                        card = available_cards[index - 1]

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

                if 1 <= index <= len(available_cards):

                    selected_card = available_cards[index - 1]

                    user.deck.upgrade_card(selected_card)

                    print(f"{selected_card.name} has been upgraded!")
                    break

            print("Please enter a valid card index")


def remove_card(user):
    if len(user.deck.get_full_deck()) <= 5:
        print("Your deck is too small to remove another card")
        return



    if get_valid_input("Would you like to remove a card?"):

            print("\nAvailable Cards:")

            available_cards = user.deck.get_full_deck()



            for index, card_id in enumerate(available_cards, start=1):
                print(f"{index}. {card_id.name}")

            while True:

                choice = input("\nWhich card would you like to remove? ").strip().lower()

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

                        selected_card = available_cards[index - 1]

                        user.deck.remove_card(selected_card)

                        print(f"{selected_card.name} has been removed from your deck!")

                        break

                print("Please enter a valid card number or i<number>.")

# This function will happen after a user successsfuly gets through a floor of combar 
# It will cleanup money for the user, heal, and offer a deck change
def reward(user):
    user.cleanup_gold()

    # Every cleared floor the user will heal up 5 hp
    user.heal(5)
    print(f"{user.name} healed 5 hp")

    # let user know funding before going through shops and whatnot
    print(f"\nYou currently have {user.gold} gold")

    add_card(user)

    upgrade_card(user)
   
    remove_card(user)

    # cleans up screen after reward
    clear_terminal()
