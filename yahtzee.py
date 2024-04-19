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
        return self.current_value
        
        
dice1 = Dice(1)
dice2 = Dice(2)
dice3 = Dice(3)
dice4 = Dice(4)
dice5 = Dice(5)

print("Dice 1: " +str(dice1.roll_dice()))
print("Dice 2: " +str(dice2.roll_dice()))
print("Dice 3: " +str(dice3.roll_dice()))
print("Dice 4: " +str(dice4.roll_dice()))
print("Dice 5: " +str(dice5.roll_dice()))
print("")
print(dice5.current_value)