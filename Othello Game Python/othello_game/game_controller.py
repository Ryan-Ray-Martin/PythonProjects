# Ryan Martin
# Dr. Mullen
# CS5001
# 12/05/2018

from piece import Piece
from move import Move
import sys


class GameController:
    """Indicates the beginnning and ending of the game."""
    def __init__(self, width, piece):
        self.width = width
        self.counter = 0
        self.piece = piece
        self.area = [[0, 1], [1, 1], [1, 0], [1, -1],
                     [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        self.valid_list = []
        self.second_turn_counter = 0

    def start_game(self, row, column):
        if self.valid(row, column):
            if self.counter % 2 == 0:
                self.piece.total_row[row][column].display('True')
                self.flip_piece(row, column)
                self.counter += 1
                print("Computers's turn.")

    def valid_helper(self):
        """ A method that checks for available legal moves for player"""
        self.valid_list = []
        if self.counter % 2 == 0:
            current_player = 'player'
            other_player = 'Computer'
        else:
            current_player = 'Computer'
            other_player = 'Player'

        for i in range(8):
            for j in range(8):
                if self.valid(i, j):
                    self.valid_list.append([i, j])
        if len(self.valid_list) > 0:
            valid_helper = True
        else:
            print("No valid move for {}. {}'s turn.".format(current_player,
                  other_player))
            valid_helper = False
            self.counter += 1
        return valid_helper

    def on_edge(self, row, column):
        """A helper method that will help the computer choose the best move
        int"""
        if row == 0 or column == 7 or column == 0 or row == 7:
            return True

    def on_corner(self, row, column):
        """A helper method that will help the computer choose the second best move
        int"""
        if (row == 0 and column == 0) or (row == 0 and column == 7) or \
           (row == 7 and column == 0) or (row == 7 and column == 7):
            return True

    def on_third(self, row, column):
        """A helper method that will help the computer choose the third best move
        int"""
        if row == 2 or column == 5 or column == 2 or row == 5:
            return True

    def computer_moves(self):
        """An AI that ranks the best moves and makes the moves based on open spaces
        List -> List"""
        self.second_turn_counter = 0
        best_move = ''
        if self.valid_helper():
            temp_y, temp_x = self.valid_list[0]
            temp = len(self.piece.total_row[temp_y][temp_x].flips_list)
            for row, column in self.valid_list:
                if self.on_corner(row, column):
                    y = row
                    x = column
                    break
                elif self.on_edge(row, column):
                    y = row
                    x = column
                    best_move = 'Second'
                    continue
                elif self.on_third(row, column):
                    if best_move == 'Second':
                        continue
                    else:
                        y = row
                        x = column
                        best_move = 'Third'
                        continue
                else:
                    if best_move == 'Second' or best_move == 'Third':
                        continue
                    else:
                        if len(self.piece.total_row[row][column].flips_list)\
                         >= temp:
                            y = row
                            x = column
                            temp = len(self.piece.total_row[y][x].flips_list)
                        else:
                            continue

            self.piece.total_row[y][x].display('False')
            self.flip_piece(y, x)
            self.counter += 1
            print("Player's turn.")
            if not self.valid_helper():
                self.second_turn_counter += 1
                if not self.valid_helper():
                    self.second_turn_counter += 1
        else:
            self.second_turn_counter += 1
            if not self.valid_helper():
                self.second_turn_counter += 1

        if self.second_turn_counter == 2:
            print('No moves for either player. Gameover.')
            self.game_over()

    def valid(self, row, column):
        valid_area = False
        other_color = self.other_color()
        current_color = self.current_color()

        for y_value, x_value in self.area:
            y = row
            x = column
            y += y_value
            x += x_value
            if not self.on_board(y, x):
                continue
            else:
                if self.piece.total_row[row][column].color == 3 \
                 and self.piece.total_row[y][x].color == other_color:
                    while True:
                        x += x_value
                        y += y_value
                        if not self.on_board(y, x):
                            break
                        elif self.piece.total_row[y][x].color == current_color:
                            valid_area = True
                            while True:
                                x -= x_value
                                y -= y_value
                                if y == row and x == column:
                                    break
                                self.piece.total_row[row][column].flips_list\
                                    .append(self.piece.total_row[y][x])
                            break
        return valid_area

    def flip_piece(self, row, column):
        """A method which displays the pieces after they are captured"""
        for move in self.piece.total_row[row][column].flips_list:
            if self.counter % 2 == 0:
                move.display('True')
            else:
                move.display('False')

    def current_color(self):
        other_color = self.other_color()
        if other_color == 1:
            current_color = 0
        else:
            current_color = 1
        return current_color

    def on_board(self, x, y):
        """A helper method for in bounds"""
        if x <= 7 and x >= 0 and y <= 7 and y >= 0:
            return True

    def other_color(self):
        if self.counter % 2 == 0:
            other_color = 1
        else:
            other_color = 0

        return other_color

    def game_over(self):
        """A method which provides the scores at the end of the game"""
        black_score = 0
        white_score = 0
        for row in self.piece.total_row:
            for move in row:
                if move.color == 0:
                    black_score += 1
                elif move.color == 1:
                    white_score += 1
        if black_score > white_score:
            score_1 = black_score
            score_2 = white_score
            winner = 'Player wins:'
            fill(255, 0, 0)
            textSize(20)
            text("Gameover. {} {} - {}". format(winner, score_1, score_2),
                 self.width/2 - self.width/3, self.width/2)
            #  If the player wins, the program will prompt the user for their
            #  name to be placed in the scores file. If the user's score is
            #  greater than the highest score, their name and score will be
            #  listed on the top of the scores list.

            def input(self, message=''):
                from javax.swing import JOptionPane
                return JOptionPane.showInputDialog(frame, message)
            answer = input('enter your name')
            if answer:
                print('Hi ' + answer)
            elif answer == '':
                print('[empty string]')
            else:
                print(answer)
            scores_list = []
            f = open('scores.txt', 'r+')
            data_list = []
            result = answer + " " + str(score_1)
            for line in f:
                data_list.append(line)
            if len(data_list) == 0:
                f.write(result)
            else:
                first_line = data_list[0].split()
                score = int(first_line[-1])
                if score_1 > score:
                    for i in range(len(data_list)):
                        result += '\n' + data_list[i]
                    f.seek(0)
                    f.write(result)
                else:
                    result = '\n' + result
                    f.write(result)
            f.close()
        elif white_score > black_score:
            score_1 = black_score
            score_2 = white_score
            winner = 'Computer wins:'
            fill(255, 0, 0)
            textSize(20)
            text("Gameover. {} {} - {}". format(winner, score_2, score_1),
                 self.width/2 - self.width/3, self.width/2)
        else:
            score_1 = black_score
            score_2 = white_score
            winner = 'Tie game:'
            fill(255, 0, 0)
            textSize(20)
            text("Gameover. {} {} - {}". format(winner, score_2, score_1),
                 self.width/2 - self.width/3, self.width/2)
