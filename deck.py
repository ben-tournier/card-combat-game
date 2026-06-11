from card_creation.extract_cards import load_cards

"""
This class is the one that holds all of the information neccicary for the battle deck to actually work
The only deck that will actually be created and interacted with is going to be in the player class to track the combat deck into the players hand into the discard pile 
"""
class Deck:
    
    def __init__(self):
        self.draw_pile = []
        self.hand = []
        self.discard_pile = []

    def fill_starting_deck(self):
        self.draw_pile = load_cards()
