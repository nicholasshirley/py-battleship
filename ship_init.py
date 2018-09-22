import math
import random

# define ships
carrier = []
battleship = []
cruiser = []
submarine = []
destroyer = []

def set_up_ships():
    # Ship numbers are as follows:
    # 1 - Carrier
    # 2 - Battleship
    # 3 - Cruiser
    # 4 - Submarine
    # 5 - Destroyer

    ship_list = [
            ["carrier", 1, 5],
            ["battleship", 2, 4],
            ["cruiser", 3, 3],
            ["submarine", 4, 3],
            ["destroyer", 5, 2]
            ]

    for x in ship_list:
        _set_origin(x[0], x[1], x[2])

    print(carrier)
    print(battleship)
    print(cruiser)
    print(submarine)
    print(destroyer)

def _set_origin(ship, ship_number, ship_size):
    global carrier
    global battleship
    global cruiser
    global submarine
    global destroyer

    # 0 = horizontal
    # 1 = vertical
    direction = random.randint(0, 1)

    # assign origin irrespective of boundaries
    # other than the game board boundaries
    origin = [random.randint(1, 10), random.randint(1, 10)]

    origin = _adjust_position(direction, origin[0], origin[1], ship_size)

    globals()[ship] = [ship_number, origin, direction]

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


