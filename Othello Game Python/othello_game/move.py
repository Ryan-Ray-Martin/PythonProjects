# Ryan Martin
# Dr. Mullen
# CS5001
# 12/05/2018


class Move():
    """A class that differentiates the traits of player pieces."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 3
        self.flips_list = []

    def display(self, check):
        #   USE 100 FOR 4 X 4
        #   USE 50 FOR 8 X 8
        piece_x = 50
        piece_y = 50
        if check == 'True':
            self.color = 0  # Black Piece
            fill(self.color)
            ellipse(self.x, self.y, piece_x, piece_y)
        else:
            self.color = 1  # White Piece
            fill(self.color)
            ellipse(self.x, self.y, piece_x, piece_y)
