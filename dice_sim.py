import random
import re


# choose the number of sides your dice contains
sides = input('Enter number of sides: ')
def dice_choice():
    
    if re.search('\d+',sides):
        if int(sides) < 2:
            print('You must chose a number greater than one')
        elif int(sides) > 2:
            print('Your choice in sides is:', sides)
    elif re.search("\D+",sides):
        print('You must choose a number')
    return sides
def roll_dice():
# numebr = random.randint(1,6)
    result = random.randint(1, int(sides))
    print('You rolled:', result)

dice_choice()
roll_dice()