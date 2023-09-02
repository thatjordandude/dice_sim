import random
import re
import time

# choose the number of sides your dice contains
sides = input('Enter number of sides: ')
def dice_choice():
    if re.search('\d+',sides):
        if int(sides) < 2:
            print('You must chose a number greater than one')
    elif re.search("\D+",sides):
        print('You must choose a number')

# Puasing to roll
print('rolling a D{}.........................'.format(sides))
time.sleep(2)

# Rolls chosen dice
def roll_dice():
    result = random.randint(1, int(sides))
    print('You rolled a:', result)
    if int(sides) == 20:
        if result == 1:
            print('Critical fail!')
        elif result == 20:
            print('Critical success!')
        else:
            pass
dice_choice()
roll_dice()