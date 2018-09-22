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
    ship_size = 4

    # assign battlehsip placement
    battleship = _set_origin(ship_size, ship_number)

def _set_origin(ship_size, ship_number):
    # 0 = horizontal
    # 1 = vertical
    direction = random.randint(0, 1)

    # assign origin irrespective of boundaries
    # other than the game board boundaries
    origin = [random.randint(1, 10), random.randint(1, 10)]

    origin = _adjust_position(direction, origin[0], origin[1], ship_size)


    return [ship_number, origin, direction]

def _adjust_position(direction, x, y, ship_size):
    # adjust the origin so the ship doesn't overrun
    # the boundaries of the game board
    if direction == 0:
        if x > (10 - (ship_size - 1)):
            x = x + (ship_size - 1) - x
            return [x, y]
        else:
            return [x, y]
    elif direction == 1:
        if y < ship_size:
            y = (y) - (y - ship_size)
            return [x, y]
        else:
            return [x, y]


