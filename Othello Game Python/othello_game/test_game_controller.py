# Ryan Martin
# Dr. Mullen
# CS5001
# 12/05/2018


from game_controller import GameController
from piece import Piece


def test_constructor():
    piece = Piece(600)
    gc = GameController(600, piece)
    assert gc.width == 600


def test_valid_helper():
    WIDTH = 600
    piece = Piece(WIDTH)
    gc = GameController(WIDTH, piece)
    gc.counter = 2
    gc.piece.total_row[3][3].color = 0  # 4 starting pieces
    gc.piece.total_row[4][4].color = 0
    gc.piece.total_row[3][4].color = 1
    gc.piece.total_row[4][3].color = 1
    gc.valid_helper()
    assert len(gc.valid_list) == 4  # First move: 4 valids moves for player


def test_on_edge():
    WIDTH = 600
    piece = Piece(WIDTH)
    gc = GameController(WIDTH, piece)
    assert gc.on_edge(0, 8) is True
    assert gc.on_edge(3, 0) is True
    assert gc.on_edge(4, 7) is True
    assert gc.on_edge(7, 4) is True
    assert gc.on_edge(1, 8) is None
    assert gc.on_edge(3, 4) is None
    assert gc.on_edge(2, 6) is None
    assert gc.on_edge(5, 5) is None


def test_on_corner():
    WIDTH = 600
    piece = Piece(WIDTH)
    gc = GameController(WIDTH, piece)
    assert gc.on_corner(0, 0) is True
    assert gc.on_corner(7, 7) is True
    assert gc.on_corner(0, 7) is True
    assert gc.on_corner(7, 0) is True
    assert gc.on_corner(1, 8) is None
    assert gc.on_corner(3, 4) is None
    assert gc.on_corner(2, 6) is None
    assert gc.on_corner(5, 5) is None


def test_on_third():
    WIDTH = 600
    piece = Piece(WIDTH)
    gc = GameController(WIDTH, piece)
    assert gc.on_third(2, 2) is True
    assert gc.on_third(5, 1) is True
    assert gc.on_third(1, 2) is True
    assert gc.on_third(2, 5) is True
    assert gc.on_third(1, 8) is None
    assert gc.on_third(6, 4) is None
    assert gc.on_third(3, 3) is None
    assert gc.on_third(4, 4) is None


def test_valid_move():
    WIDTH = 600
    piece = Piece(WIDTH)
    gc = GameController(WIDTH, piece)
    gc.counter = 2

    gc.piece.total_row[3][3].color = 0
    gc.piece.total_row[4][4].color = 0
    gc.piece.total_row[3][4].color = 1
    gc.piece.total_row[4][3].color = 1
    assert gc.valid(4, 2) is True
    assert gc.valid(5, 3) is True
    assert gc.valid(2, 4) is True
    assert gc.valid(3, 5) is True
    assert gc.valid(3, 4) is False
    assert gc.valid(2, 2) is False
    assert gc.valid(0, 0) is False
    assert gc.valid(7, 7) is False

    gc.counter = 1
    gc.piece.total_row[3][3].color = 0
    gc.piece.total_row[4][4].color = 0
    gc.piece.total_row[3][4].color = 1
    gc.piece.total_row[4][3].color = 1
    assert gc.valid(3, 2) is True
    assert gc.valid(4, 5) is True
    assert gc.valid(5, 4) is True
    assert gc.valid(2, 3) is True
    assert gc.valid(3, 4) is False
    assert gc.valid(2, 2) is False
    assert gc.valid(0, 0) is False
    assert gc.valid(7, 7) is False


def test_current_color():
    WIDTH = 600
    piece = Piece(WIDTH)
    gc = GameController(WIDTH, piece)
    gc.counter = 2
    assert gc.current_color() == 0


def test_other_color():
    WIDTH = 600
    piece = Piece(WIDTH)
    gc = GameController(WIDTH, piece)
    gc.counter = 2
    assert gc.other_color() == 1
