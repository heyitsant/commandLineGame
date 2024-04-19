import random

class Dice():
    def __init__(self, id):
        # the dice object will receive it's ID when it is initiated.
        # it will have a default value of -1 to indicate it hasn't been rolled
        # it will also not be 'held' by default.
        
        self.id = id
        self.current_value = -1
        self.held = False
        
    def roll_dice(self):
        if self.held == False:
            self.current_value = random.randint(1, 6)
        else:
            self.current_value = self.current_value
            self.held = False
        return self.current_value
    
    def hold_dice(self):
        self.held = True
        
class Player():
    def __init__(self, name):
        self.name = name
        self.top_score = 0
        self.bottom_score = 0
        self.total_score = self.top_score + self.bottom_score
        self.scores_used = []
        self.rolls_this_turn = 0
    
                
        
dice1 = Dice(1)
dice2 = Dice(2)
dice3 = Dice(3)
dice4 = Dice(4)
dice5 = Dice(5)
