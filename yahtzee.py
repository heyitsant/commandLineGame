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
        self.score_sheet = [["Upper Section", {"Aces (Ones): ": 0}],["Lower Section", {"3 of a kind: ": 0}]]
        self.dice = [Dice(1), Dice(2), Dice(3), Dice(4), Dice(5)]    
    
                
        


player1 = Player("Antony")
player2 = Player("James")

player1.dice[0].roll_dice()
print(f"{player1.name} just rolled a {player1.dice[0].current_value}")


player2.dice[0].roll_dice()
print(f"{player2.name} just rolled a {player2.dice[0].current_value}")

if player1.dice[0].current_value > player2.dice[0].current_value:
    print(f"{player1.name} rolled higher than {player2.name}.")
elif player1.dice[0].current_value == player2.dice[0].current_value:
    print(f"{player1.name} and {player2.name} rolled the same, what are the chances?")
else:
    print(f"{player2.name} rolled higher than {player1.name}.")