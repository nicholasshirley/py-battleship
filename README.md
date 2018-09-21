# Py-Battleship
I'm learning Python!

This is a project that will allow a user to play the classic
Battleship game (or something close to it) against an AI opponent
in the console.

# Planning
## Board
The board is an 10x10 grid. A player board and an computer board
will be maintained. The board will be numbered as follows:
* X-axis - numeric
* Y-axis - alpha

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

## Win conditions
One side wins when either one of two conditions are met:
1. All of a players ships are sunk
2. The players battship is sunk

