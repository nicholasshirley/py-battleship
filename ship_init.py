import math
import random

# define ships
battleship = []

def set_up_ships():
    _battleship()
    print(battleship)

def _battleship():
    global battleship

    ship_number = 2

    # 0 = horizontal
    # 1 = vertical
    direction = random.randint(0, 1)

    # assign origin irrespective of boundaries
    # other than the game board boundaries
    origin = [random.randint(1, 10), random.randint(1, 10)]

    origin = _adjust_position(direction, origin[0], origin[1])

    # assign battlehsip placement
    battleship = [ship_number, origin, direction]

def _adjust_position(direction, x, y):
    # adjust the origin so the ship doesn't overrun
    # the boundaries of the game board
    if direction == 0:
        if x > 7:
            x = (x) + (7 - x)
            return [x, y]
        else:
            return [x, y]
    elif direction == 1:
        if y < 4:
            y = (y) - (y - 4)
            return [direction, x, y]
        else:
            return [direction, x, y]


