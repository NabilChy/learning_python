from random import randint

class Dice:
    '''Create a dice'''

    def __init__(self, sides=6):
        '''Initializes the dice attributes'''
        self.sides = sides
    

    def roll_dice(self):
        '''Rolls the dice'''
        current_number = randint(1, self.sides)
        print(f"You have rolled {current_number}.") 

dice = Dice(10)
dice.roll_dice()