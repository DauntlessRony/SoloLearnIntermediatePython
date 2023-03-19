from random import randint

def roll(**dice):
    print(type(dice))
    # return print(sum(randint(1, die) for die in dice))

roll({1:2})