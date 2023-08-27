import random

# choose the number of sides your dice contains
def dice_choice():
    sides = input('Enter number of sides: ')
    if map(sides.isalpha()):
        print('You must choose a number')
    if sides.isnumeric():
        print('Your choice in sides is:', sides)
def roll_dice():
# numebr = random.randint(1,6)
    pass

dice_choice()