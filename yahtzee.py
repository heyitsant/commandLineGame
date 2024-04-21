import random
from os import system

class Dice():
    def __init__(self, id):
        # the dice object will receive it's ID when it is initiated.
        # it will have a default value of -1 to indicate it hasn't been rolled
        # it will also not be 'held' by default.
        # If a dice is 'held' then it won't be rolled.
                
        self.id = id
        self.current_value = -1
        self.held = False
        
    def roll(self):
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
        self.upper_score = 0
        self.lower_score = 0
        self.total_score = self.upper_score + self.lower_score
        self.scores_used = []
        self.rolls_this_turn = 0
        self.score_sheet = [["Upper Section", {"Aces (Ones): ": 0}],["Lower Section", {"3 of a kind: ": 0}]]
        self.dice = [Dice(1), Dice(2), Dice(3), Dice(4), Dice(5)]  
        self.last_roll = []  
    
    def roll_dice(self): 
        for dice in self.dice:
            self.last_roll.append(dice.roll())

        return self.last_roll

    def hold_dice(self, values_to_hold):
        index = 0
        held_dice = []
        for value in values_to_hold:
            for score in range(index, len(self.last_roll) + 1):
                if int(value) == self.last_roll[score]:
                    print(self.last_roll[score])
                    self.dice[index].hold_dice()
                    held_dice.append(index + 1)
                    index += 1
                    break
                else:
                    index += 1
        print(f"You held the following dice {held_dice}")



def clear_screen():
    _ = system('cls')
        


player1 = Player("Antony")
player2 = Player("James")


# print(f"First roll: {player1.roll_dice()}")
# print("Holding dice 1 and 3.")
# player1.dice[0].hold_dice()
# player1.dice[2].hold_dice()
# print(f"Second roll: {player1.roll_dice()}")



# Need to do: Add a dictionary for possible scores.
# Add a scoring method to update the scores dictionary.


def round(player):
    clear_screen()
    print(f"{player.name}, it's your turn. Your current score (not including any bonuses) is {player.total_score} points.")
    input("Press enter to roll your dice.")
    print(f"You rolled: {player.roll_dice()}")
    roll_or_score = input("Would you like to\n1: Roll again \n2: Score your dice\n")

    if roll_or_score == "1":
        hold = input("Would you like to hold any of your dice?\nY or N: ")
        if hold.lower() == "y":
            values = input("Please enter to values of any dice that you would like to hold.\nEnter your choice with no spaces: ")
            value_list = []
            for i in values:
                value_list.append(i)
            player.hold_dice(value_list)




round(player1)