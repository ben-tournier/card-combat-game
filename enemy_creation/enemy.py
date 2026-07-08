class Enemy:
    def __init__(self, name, hp, damage, behavior, block=0):
        self.name = name
        self.max_hp = hp 
        self.hp = hp
        self.damage = damage
        self.block = block
        self.behavior = behavior

    def take_damage(self, amount):
        effective_damage = max(0, amount - self.block)
        self.hp -= effective_damage

    def is_alive(self):
        return self.hp > 0
    
    def is_dead(self):
        return not self.is_alive()
    
    def __repr__(self):
        return f"{self.name} (HP: {self.hp} / {self.max_hp})"