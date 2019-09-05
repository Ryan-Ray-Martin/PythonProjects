# Ryan Martin
# Dr. Mullen
# CS5001
# 12/05/2018

from board import Board
from piece import Piece
from game_controller import GameController


WIDTH = 600
HEIGHT = 600
# USE 8 BOXES FOR 4 X 4
#BOXES = 8
# USE 16 BOXES FOR 8 X 8
BOXES = 16
board = Board(WIDTH)
piece = Piece(WIDTH)
gc = GameController(WIDTH, piece)
SPACING = WIDTH/8
DELAY = 30


def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)
    background(0, 0.7, 0)
    board.display(WIDTH)
    piece.start_piece(WIDTH)
    



def draw():
    global DELAY
    if gc.counter % 2 != 0 and gc.second_turn_counter != 2 and gc.second_turn_counter != 3:
        DELAY -= 1
        if DELAY == 0:
            gc.computer_moves()
            DELAY = 30
    

def mousePressed():
    for i in range(8):
        for j in range(8):
            if i == (mouseY//SPACING) and j == (mouseX//SPACING):
                gc.start_game(i, j)
                
def input(self, message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)
