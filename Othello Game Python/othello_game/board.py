# Ryan Martin
# Dr. Mullen
# CS5001
# 12/05/2018

# USE 4 FOR 4 X 4, 8 FOR 8 X 8
BOXES_PER_ROW = 8


class Board:
    """A class which displays the grid-like structure of the board
    for playing Othello."""
    def __init__(self, width):
        pass

    def display(self, width):
        for i in range(width/BOXES_PER_ROW, width, width/BOXES_PER_ROW):
            strokeWeight(5)
            line(i, 0, i, width)
            line(0, i, width, i)
