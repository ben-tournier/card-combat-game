from deck import Deck 

class Player:

    def __init__(self):
        self.deck = Deck()
        self.deck.fill_starting_deck()

    def __repr__(self):
        return self.deck
    
