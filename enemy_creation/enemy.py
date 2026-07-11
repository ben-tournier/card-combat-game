class Enemy:
    def __init__(self, name, hp, damage, behavior, value, block=0):
        self.name = name
        self.max_hp = hp 
        self.hp = hp
        self.damage = damage
        self.block = block
        self.behavior = behavior
        self.value = value 

    def take_damage(self, amount):
        effective_damage = max(0, amount - self.block)
        self.hp -= effective_damage
        
        if effective_damage > 0:
            self.block = 0

    def is_alive(self):
        return self.hp > 0
    
    def get_damage(self):
        return self.damage
    
    def check_attack(self):
        return "attack" in self.behavior
    
    def check_block(self):
        return self.block
    
    def __repr__(self):
        return f"{self.name} (HP: {self.hp} / {self.max_hp})"