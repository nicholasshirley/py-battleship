# Py-Battleship
I'm learning Python!

This is a project that will allow a user to play the classic
Battleship game (or something close to it) against an AI opponent
in the console.

# Planning
## Ship size
There are 5 ships in the game:
<table>
  <thead>
    <tr>
      <th>#</th>
      <th>Class</th>
      <th>Size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Carrier</td>
      <td>5</td>
    </tr>

    <tr>
      <td>2</td>
      <td>Battleship</td>
      <td>4</td>
    </tr>

    <tr>
      <td>3</td>
      <td>Cruiser</td>
      <td>3</td>
    </tr>

    <tr>
      <td>4</td>
      <td>Submarine</td>
      <td>3</td>
    </tr>

    <tr>
      <td>5</td>
      <td>Destroyer</td>
      <td>2</td>
    </tr>
  </tbody>
</table>

## Board
The board is an 10x10 grid. A player board and an computer board
will be maintained. The board will be numbered as follows:
* X-axis - numeric
* Y-axis - numeric

All numeric values are used for convenience, the more familiar
numeric/alpha combination will be added later.

The board is initialized as an empty array. Ships are then placed 
using 4 values (ship code, x pos, y pos, direction). The format is:

```
[ship_number, [x-pos, y-pos], direction]
```

where a direction of 0 = horizontal and a direction of 1 = vertical.

Examples:

battleship in the upper left corner lying horizontally:

```
battleship = [2, [1, 10], 0]
```
battleship in the middle of the board lying vertically:

```
battleship = [2, [5, 6], 1]
```

## Win conditions
One side wins when either one of two conditions are met:
1. All of a players ships are sunk
2. The players battship is sunk

