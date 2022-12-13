'''
R Y C H L O M E R
'''

import random


def rychlost():
    return random.randint(30,  130)


def vystraha():
    s = rychlost()
    if s < 30 or s > 110:
        return True
    else:
        return False


if __name__ == '__main__':
    print(vystraha())