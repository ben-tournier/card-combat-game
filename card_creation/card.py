class Card:

    def __init__(self, card_id, name, card_type, cost, damage, block):
        self.card_id = card_id
        self.name = name
        self.card_type = card_type
        self.cost = cost
        self.damage = damage
        self.block = block

    def __str__(self):
        return (
            f"{self.name}\n"
            f"Cost: {self.cost}\n"
            f"Damage: {self.damage}\n"
            f"Block: {self.block}\n")

    def __repr__(self):
        return self.name