import math
import random

# define ships
carrier = []
battleship = []
cruiser = []
submarine = []
destroyer = []

def set_up_ships():
    _carrier()
    _battleship()
    _cruiser()
    _submarine()
    _destroyer()

    print(carrier)
    print(battleship)
    print(cruiser)
    print(submarine)
    print(destroyer)

def _carrier():
    global carrier

    ship_number = 1
    ship_size = 5

    # assign carrier placement
    carrier = _set_origin(ship_size, ship_number)

def _battleship():
    global battleship

    ship_number = 2
    ship_size = 4

    # assign battlehsip placement
    battleship = _set_origin(ship_size, ship_number)

def _cruiser():
    global cruiser

    ship_number = 3
    ship_size = 3

    # assign battlehsip placement
    cruiser = _set_origin(ship_size, ship_number)

def _submarine():
    global submarine

    ship_number = 4
    ship_size = 3

    # assign battlehsip placement
    submarine = _set_origin(ship_size, ship_number)

def _destroyer():
    global destroyer

    ship_number = 5
    ship_size = 2

    # assign battlehsip placement
    destroyer = _set_origin(ship_size, ship_number)
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


