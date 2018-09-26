import math
import random

# define ships
ship_list = {
        'computer': {},
        'user': {}
        }

def set_up_ships():
    # Ship numbers are as follows:
    # 1 - Carrier (size: 5)
    # 2 - Battleship (size: 4)
    # 3 - Cruiser (size: 3)
    # 4 - Submarine (size: 3)
    # 5 - Destroyer (size: 2)

    ship_list = [
            ["computer", "carrier", 1, 5],
            ["computer", "battleship", 2, 4],
            ["computer", "cruiser", 3, 3],
            ["computer", "submarine", 4, 3],
            ["computer", "destroyer", 5, 2],
            ["user", "carrier", 1, 5],
            ["user", "battleship", 2, 4],
            ["user", "cruiser", 3, 3],
            ["user", "submarine", 4, 3],
            ["user", "destroyer", 5, 2]
            ]

    for ships in ship_list:
        _set_origin(ships[0], ships[1], ships[2], ships[3])

    return ship_list

def _set_origin(owner, ship, ship_number, ship_size):
    # 0 = horizontal
    # 1 = vertical
    direction = random.randint(0, 1)

    # assign origin irrespective of boundaries
    # other than the game board boundaries
    origin = [random.randint(1, 10), random.randint(1, 10)]

    # now adjust the position so it doesn't overrun
    origin = _adjust_position(direction, origin[0], origin[1], ship_size)

    # assign global ship variable with data
    ship_list[str(owner)].update({ ship_number: { 'origin': origin, 'direction': direction } })

def _adjust_position(direction, x, y, ship_size):
    # adjust the origin so the ship doesn't overrun
    # the boundaries of the game board

    # relevant dimensions are either x or y depending on
    # how the ship is positioned, but the other can be ignored
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


