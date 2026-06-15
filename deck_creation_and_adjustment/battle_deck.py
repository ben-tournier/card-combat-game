import random
from copy import deepcopy
from card_creation.extract_cards import load_cards

"""
This class is the beast that makes the game work - everything for the deck that the player draws into, discards into and changes is in here as well as the players hand strategies and card playing abilities
While it is a messy class it is a lot simpler than the constant importation of seperating out into a deck and a hand class 
"""
class BattleDeck:
    
    def __init__(self):
        self.draw_pile = []
        self.hand = []
        self.discard_pile = []

        # --------------- Setup ---------------
    def fill_starting_deck(self):
        # to make a reasonably functioning starting deck there are 10 copies of the basic strike and shield cards and 1 unique copy of a hypnotize card

        cards =load_cards()

        for i in range(5):
            self.draw_pile.append(deepcopy(cards["Strike"]))
            self.draw_pile.append(deepcopy(cards["Shield"]))

        self.draw_pile.append(deepcopy(cards["Hypnotize"]))

    # this only shuffles the draw pile for the player
    def shuffle_deck(self):
        random.shuffle(self.draw_pile)
    
        #--------------- Card Movement ---------------

    # this will shuffle the discard and the draw pile together making it really useful at the end of a floor when everything should be reset
    def refresh_draw_pile(self):
        for card in range(len(self.discard_pile)):
            self.draw_pile.append(self.discard_pile.pop(0))

    # the players hand size will be 5 for now cards may eventually upgrade it in which case will need to change so cant draw from empty deck
    # as of right now just sets up a 5 card hand for the user
    def draw_hand(self):
        for card in range(5):

            if len(self.draw_pile) == 0:
                self.shuffle_piles()

            self.hand.append(self.draw_pile.pop(0))


    def discard_hand(self):
        self.discard_pile.extend(self.hand)
        self.hand.clear()

        #--------------- gameplay ---------------

    #def play_card(self):