import random
import re


# choose the number of sides your dice contains
def dice_choice():
    sides = input('Enter number of sides: ')
    if re.search('\d+',sides):
        if int(sides) < 2:
            print('You must chose a number greater than one')
        elif int(sides) < 2:
            print('Your choice in sides is:', sides)
    elif re.search("\D+",sides):
        print('You must choose a number')
    
def roll_dice():
# numebr = random.randint(1,6)
    pass

dice_choice()