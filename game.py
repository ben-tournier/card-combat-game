from player import Player

class Game:

    def __init__(self, player):
        self.player = player
        self.current_floor = 1
        self.game_over = False

    def is_boss_floor(self):
        return self.current_floor % 10 == 0
    
    def is_elite_floor(self):
        return self.current_floor % 5 ==0 and not self.is_boss_floor()