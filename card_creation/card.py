class Card:

    def __init__(self, name, card_type, cost, damage, block):
        self.name = name
        self.card_type = card_type
        self.cost = cost
        self.damage = damage
        self.block = block

    def __repr__(self):
        return self.name