from enum import Enum


class Square(Enum):
    WHITE_MAN = 1
    WHITE_KING = 2
    BLACK_MAN = 3
    BLACK_KING = 4
    EMPTY = 5
    INVALID = 6


class Checkers:

    def __init__(self):
        self.board = [[Square.INVALID for x in range(8)] for y in range(8)]
        self._init_board()

    def _init_board(self):
        for row in [0, 2]:
            for col in [1, 3, 5, 7]:
                self.board[row][col] = Square.BLACK_MAN

        for row in [6]:
            for col in [1, 3, 5, 7]:
                self.board[row][col] = Square.WHITE_MAN

        for row in [1]:
            for col in [0, 2, 4, 6]:
                self.board[row][col] = Square.BLACK_MAN

        for row in [5, 7]:
            for col in [0, 2, 4, 6]:
                self.board[row][col] = Square.WHITE_MAN

        for row in [3]:
            for col in [0, 2, 4, 6]:
                self.board[row][col] = Square.EMPTY

        for row in [4]:
            for col in [1, 3, 5, 7]:
                self.board[row][col] = Square.EMPTY

    def get_valid_moves(self, x0, y0):
        try:
            square = self.board[x0][y0]
            if square == Square.INVALID or square == Square.EMPTY:
                return None
            elif square == Square.WHITE_MAN:
                return self._get_valid_man_moves_white(x0, y0)
            elif square == Square.BLACK_MAN:
                return self._get_valid_man_moves_black(x0, y0)
            else:
                return self._get_valid_king_moves(x0, y0)
        except IndexError:
            return None

    # returns all possible moves that the white man piece can make or None
    def _get_valid_man_moves_white(self, x0, y0):
        return None

    # returns all possible moves that a black man piece can make or None
    def _get_valid_man_moves_black(self, x0, y0):
        return None

    # returns all possible moves that a king piece can make or None
    def _get_valid_king_moves(self, x0, y0):
        return None

    # for debug
    def print(self):
        for i in self.board:
            print(str(i) + "\n")

    def to_display_data(self):
        data = ""
        for s in self.board:
            data += s.value