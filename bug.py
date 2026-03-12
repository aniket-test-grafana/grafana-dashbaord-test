# Bug: Missing 'import random'
def roll_dice():
    return randint(1, 6) # NameError: name 'randint' is not defined
