# Ryan Martin
# Dr. Mullen
# CS5001
# 11/21/2018

from move import Move

BOXES = 16
SIDES = 4
SPOT = 1
ROWS = 8


class Piece:
    """A class which implements the spaces for the player pieces to
    land in rows.
    List(Comp) -> List of lists"""
    def __init__(self, width):
        self.SPACING = width//16
        self.first_row = [Move(self.SPACING * i, width/BOXES)
                          for i in range(1, (width//self.SPACING), 2)]
        self.second_row = [Move(self.SPACING * i,
                           (width/BOXES + width/ROWS) * 1)
                           for i in range(1, (width//self.SPACING), 2)]
        self.third_row = [Move(self.SPACING * i, (width/BOXES +
                          (width/ROWS) * 2))
                          for i in range(1, (width//self.SPACING), 2)]
        self.fourth_row = [Move(self.SPACING * i, (width/BOXES +
                           (width/ROWS) * 3)) for i in range(1,
                           (width//self.SPACING), 2)]
        self.fifth_row = [Move(self.SPACING * i, (width/BOXES + (width/8) * 4))
                          for i in range(1, (width//self.SPACING), 2)]
        self.sixth_row = [Move(self.SPACING * i, (width/BOXES +
                          (width/ROWS) * 5))
                          for i in range(1, (width//self.SPACING), 2)]
        self.seventh_row = [Move(self.SPACING * i, (width/BOXES +
                            (width/ROWS) * 6))
                            for i in range(1, (width//self.SPACING), 2)]
        self.eighth_row = [Move(self.SPACING * i, (width/BOXES +
                           (width/ROWS) * 7))
                           for i in range(1, (width//self.SPACING), 2)]
        self.total_row = []
        self.total_row.append(self.first_row)
        self.total_row.append(self.second_row)
        self.total_row.append(self.third_row)
        self.total_row.append(self.fourth_row)
        self.total_row.append(self.fifth_row)
        self.total_row.append(self.sixth_row)
        self.total_row.append(self.seventh_row)
        self.total_row.append(self.eighth_row)

    def start_piece(self, width):
        """A method that uses a formula to position the pieces
        in the starting position."""
        # this formula is scalable, works for 4 X 4 and 8 X 8 and more
        black_piece_1_x = BOXES/SIDES - SPOT
        black_piece_1_y = BOXES/SIDES - SPOT
        black_piece_2_x = BOXES/SIDES
        black_piece_2_y = BOXES/SIDES
        white_piece_1_x = BOXES/SIDES - SPOT
        white_piece_1_y = BOXES/SIDES
        white_piece_2_x = BOXES/SIDES
        white_piece_2_y = BOXES/SIDES - SPOT

        # displays starting position pieces
        self.total_row[black_piece_1_x][black_piece_1_y].display('True')
        self.total_row[black_piece_2_x][black_piece_2_y].display('True')
        self.total_row[white_piece_1_x][white_piece_1_y].display('False')
        self.total_row[white_piece_2_x][white_piece_2_y].display('False')
