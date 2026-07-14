import random
from copy import deepcopy
from card_creation.extract_cards import load_cards

"""
This class is the beast that makes the game work - everything for the deck that the player draws into, discards into and changes is in here as well as the players hand strategies and card playing abilities
While it is a messy class it is a lot simpler than the constant importation of seperating out into a deck and a hand class
"""
class BattleDeck:

    def __init__(self):
        self.cards = load_cards()

        self.draw_pile = []
        self.hand = []
        self.discard_pile = []
        self.hand_size = 5

        # --------------- Setup ---------------
    def fill_starting_deck(self):
        # to make a reasonably functioning starting deck there are 10 copies of the basic strike and shield cards and 1 unique copy of a hypnotize card

        for _ in range(5):
            self.draw_pile.append(deepcopy(self.cards[1]["basic"]))
            self.draw_pile.append(deepcopy(self.cards[2]["basic"]))

        self.draw_pile.append(deepcopy(self.cards[3]["basic"]))

    # this only shuffles the draw pile for the player
    def shuffle_deck(self):
        random.shuffle(self.draw_pile)

    # still in the design phase but there may be points where changed hand size are rewards for certain points
    def change_hand_size(self, amount):
        self.hand_size += amount

        #--------------- Card Movement ---------------

    # The piles are reshuffled after all of the cards are drawn from the deck
    def reshuffle_discard_to_draw(self):
        self.draw_pile.extend(self.discard_pile)
        self.discard_pile.clear()
        self.shuffle_deck()

    # This is where the discard will be called to shuffle in provided the draw is empty
    def draw_card(self):
        if len(self.draw_pile) == 0:
            if len(self.discard_pile) == 0:
                # Ideally never executes - means all cards are gone
                return None

            # this means all cards are in discard or hand
            self.reshuffle_discard_to_draw()

        drawn_card = self.draw_pile.pop(0)
        self.hand.append(drawn_card)
        return drawn_card

    def draw_hand(self):
        for _ in range(self.hand_size):
            card = self.draw_card()
            if card is None:
                break

    # part of the gameplay loop is going to be discarding what is left with the hand at the end of the turn
    def discard_hand(self):
        self.discard_pile.extend(self.hand)
        self.hand.clear()

        #--------------- gameplay ---------------
    def get_card(self, index):
        if 0 <= index < len(self.hand):
            return self.hand[index]
        return None

    def get_type(self, index):
        return self.hand[index].card_type

    def get_damage(self, index):
        return self.hand[index].damage > 0
    
    def get_energy(self, index):
        print("didit")
        return self.hand[index].cost 

    def show_hand(self):
        if len(self.hand) == 0:
            return "Your hand is empty."

        output = []
        for index, card in enumerate(self.hand, start=1):
            output.append(f"{index}. {card.name} [{card.cost}] energy")

        return "\n".join(output)

    # the parameter will not be checked before being passed in - some sort of error message can be implemented later
    def play_card_from_hand(self, position):
        if position < 1 or position > len(self.hand):
            return None

        card_played = self.hand.pop(position - 1)
        self.discard_pile.append(card_played)
        return card_played

    #--------------- Upgrading Cards ---------------

    def remove_card(self, card):

        if card in self.draw_pile:
            self.draw_pile.remove(card)
            return True

        if card in self.discard_pile:
            self.discard_pile.remove(card)
            return True

        if card in self.hand:
            self.hand.remove(card)
            return True

        return False

    def add_card(self, card_id):
        return self.discard_pile.append(deepcopy(self.cards[card_id]["basic"]))

    def upgrade_card(self, card):
        upgraded = self.cards[card.card_id]["upgraded"]

        upgraded = deepcopy(upgraded)

        for pile in [self.draw_pile, self.hand, self.discard_pile]:
            for index, current_card in enumerate(pile):
                if current_card is card:
                    pile[index] = upgraded
                    return True
                
        return False
                
    def show_full_deck(self):
        deck = self.get_full_deck()

        if len(deck) == 0:
            return "Your deck is empty."

        output = []

        for index, card in enumerate(deck, start=1):
            output.append(f"{index}. {card.name}")

        return "\n".join(output)
    
    
    def get_full_deck(self):
        full_deck = []

        full_deck.extend(self.draw_pile)
        full_deck.extend(self.hand)
        full_deck.extend(self.discard_pile)

        return full_deck



    def get_random_cards(self, num):

        available_cards = []

        for card in self.get_full_deck():

            if "+" not in card.name:
                available_cards.append(card)

        if len(available_cards) <= num:
            return available_cards

        return random.sample(available_cards, num)