from deck_creation_and_adjustment.battle_deck import BattleDeck
# This is where the users information is stored
# On top of keeping a bunch of the deck information in here it will also store hp, block, etc.


class Player:

    def __init__(self, name):
        self.name = name
        self.deck = BattleDeck()
        self.deck.fill_starting_deck()
        self.deck.shuffle_deck()
        self.hp = 25
        self.block = 0
        self.gold = 10


        # ------------- Hand functions -------------
    def start_of_turn(self):
        self.block = 0
        self.deck.draw_hand()

    def relay_cards_in_hand(self):
        self.deck.show_hand()
    

    # may eventually be extended to add in removal of all temporary effects 
    def end_of_turn(self):
        self.deck.discard_hand()

        # ------------- Combat functions -------------
    def gain_block(self, amount):
        self.block += amount

    def heal(self, amount):
        self.hp += amount

    def take_damage(self, amount):
        if amount > self.block:
            amount -= self.block
            self.block = 0
            self.hp -= amount 
        else:
            self.block -= amount

    def play_card(self, position, enemy):
        card_played = self.deck.play_card_from_hand(position)

        if card_played is None:
            return "Invalid card choice"
        
        actions_from_card = []

        # this part gets a little complicated as it refers to the card class to figure out the type and bases the next part off of that
        if card_played.damage > 0:
            enemy.take_damage(card_played.damage)
            actions_from_card.append(f"dealing {card_played.damage} damage")
        
        if card_played.block > 0:
            self.gain_block(card_played.block)
            actions_from_card.append(f"gaining {card_played.block} block")


        # ------------- Spending Functions -------------
    def spend_gold(self, amount):
        if amount > self.gold:
            return False
        return True
    
    def gain_gold(self, amount):
        self.gold += amount 


    def __repr__(self):
        return f"Player(HP={self.hp}, Block={self.block}, Gold={self.gold})"
    
me = Player()
print(me)
me.start_of_turn()
print(me.relay_cards_in_hand())
