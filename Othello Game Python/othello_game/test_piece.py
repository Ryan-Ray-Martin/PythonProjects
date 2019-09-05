#  Ryan Martin
#  Dr. Mullen
#  CS 5001
#  12/ 05/ 2018

from piece import Piece


def test_constructor():
    width = 600
    piece = Piece(width)
    assert len(piece.first_row) == 8
    assert len(piece.second_row) == 8
    assert len(piece.third_row) == 8
    assert len(piece.fourth_row) == 8
    assert len(piece.fifth_row) == 8
    assert len(piece.sixth_row) == 8
    assert len(piece.seventh_row) == 8
    assert len(piece.eighth_row) == 8
    assert len(piece.total_row) == 8

    i = 1

    for l in range(len(piece.first_row)):
        assert piece.first_row[l].x == piece.SPACING * i
        i += 2
        assert piece.first_row[l].y == width/16

    i = 1

    for l in range(len(piece.second_row)):
        assert piece.second_row[l].x == piece.SPACING * i
        i += 2
        assert piece.second_row[l].y == width/16 + (width/8) * 1

    i = 1

    for l in range(len(piece.third_row)):
        assert piece.third_row[l].x == piece.SPACING * i
        i += 2
        assert piece.third_row[l].y == width/16 + (width/8) * 2

    i = 1

    for l in range(len(piece.fourth_row)):
        assert piece.fourth_row[l].x == piece.SPACING * i
        i += 2
        assert piece.fourth_row[l].y == width/16 + (width/8) * 3

    i = 1

    for l in range(len(piece.fifth_row)):
        assert piece.fifth_row[l].x == piece.SPACING * i
        i += 2
        assert piece.fifth_row[l].y == width/16 + (width/8) * 4

    i = 1

    for l in range(len(piece.sixth_row)):
        assert piece.sixth_row[l].x == piece.SPACING * i
        i += 2
        assert piece.sixth_row[l].y == width/16 + (width/8) * 5

    i = 1

    for l in range(len(piece.seventh_row)):
        assert piece.seventh_row[l].x == piece.SPACING * i
        i += 2
        assert piece.seventh_row[l].y == width/16 + (width/8) * 6

    i = 1

    for l in range(len(piece.eighth_row)):
        assert piece.eighth_row[l].x == piece.SPACING * i
        i += 2
        assert piece.eighth_row[l].y == width/16 + (width/8) * 7
