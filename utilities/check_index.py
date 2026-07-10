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

        print("Please enter a valid card number or i#.")
    
# this function saves time making sure the response to given text is either y/n 
def get_valid_input(txt):
    while True:
        response = input(f"{txt} please respond with either y/n: ").lower()
        if response == 'y':
            return True
        if response == 'n':
            return False

        print(f"Error, {response} is not a valid input")
