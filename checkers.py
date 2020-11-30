from enum import Enum
"""
Module which handles all game board logic. This includes validating moves
and highlighting possible moves.
"""

class Square(Enum):
    """
    This is an enum used for representing the state of a game board.
    """

    WHITE_MAN = 1
    WHITE_KING = 2
    BLACK_MAN = 3
    BLACK_KING = 4
    EMPTY = 5
    INVALID = 6
    HIGHLIGHTED = 7


class Checkers:
    """
    This is a class used to represent a checkers board.
    """

    def __init__(self):
        """
        Initializes the game board to a standard checkers starting game.
        """
        self.board = [[Square.INVALID for _ in range(8)] for _ in range(8)]
        self._init_board()

    def _init_board(self):
        """
        Helper method for initializing the game board.
        """
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
        """
        Gets the valid moves for a piece at a give coordinate on the game board.
        :param x0: row that piece is located on
        :param y0: column that piece is located on
        :return: tuples of possible coordinates the piece can move to
        """
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

    def _get_valid_man_moves_white(self, x0, y0):
        """
        Helper method to get the valid moves that a white piece can make.
        :param x0: row that white piece is located on
        :param y0: column that white piece is located on
        :return: tuples of possible coordinates the white piece can move to
        """
        valid_moves = []
        if y0-1 == -1:
            if self.board[x0-1][y0+1] == Square.EMPTY \
                    or self.board[x0-1][y0+1] == Square.HIGHLIGHTED:
                valid_moves.append((x0 - 1, y0 + 1))
        elif y0+1 == 8:
            if self.board[x0-1][y0-1] == Square.EMPTY \
                    or self.board[x0-1][y0-1] == Square.HIGHLIGHTED:
                valid_moves.append((x0 - 1, y0 - 1))
        else:
            if self.board[x0-1][y0+1] == Square.EMPTY \
                    or self.board[x0-1][y0+1] == Square.HIGHLIGHTED:
                valid_moves.append((x0 - 1, y0 + 1))
            if self.board[x0-1][y0-1] == Square.EMPTY \
                    or self.board[x0-1][y0-1] == Square.HIGHLIGHTED:
                valid_moves.append((x0 - 1, y0 - 1))
        return valid_moves

    def _get_valid_man_moves_black(self, x0, y0):
        """
        Helper method to get the valid moves that a black piece can make.
        :param x0: row that black piece is located on
        :param y0: column that black piece is located on
        :return: tuples of possible coordinates the black piece can move to
        """
        valid_moves = []
        if y0-1 == -1:
            if self.board[x0+1][y0+1] == Square.EMPTY \
                    or self.board[x0+1][y0+1] == Square.HIGHLIGHTED:
                valid_moves.append((x0+1, y0+1))
        elif y0+1 == 8:
            if self.board[x0+1][y0-1] == Square.EMPTY \
                    or self.board[x0+1][y0-1] == Square.HIGHLIGHTED:
                valid_moves.append((x0+1, y0-1))
        else:
            if self.board[x0+1][y0+1] == Square.EMPTY \
                    or self.board[x0+1][y0+1] == Square.HIGHLIGHTED:
                valid_moves.append((x0+1, y0+1))
            if self.board[x0+1][y0-1] == Square.EMPTY \
                    or self.board[x0+1][y0-1] == Square.HIGHLIGHTED:
                valid_moves.append((x0+1, y0-1))
        return valid_moves

    def _get_valid_king_moves(self, x0, y0):
        """
        Helper method to get the valid moves that a king piece can make.
        :param x0: row that king piece is located on
        :param y0: column that king piece is located on
        :return: tuples of possible coordinates the king piece can move to
        """
        valid_moves = []
        if x0-1 != -1 and y0-1 != -1:
            if self.board[x0-1][y0-1] == Square.EMPTY \
                    or self.board[x0-1][y0-1] == Square.HIGHLIGHTED:
                valid_moves.append((x0, y0))
        if x0+1 != 8 and y0-1 != -1:
            if self.board[x0+1][y0-1] == Square.EMPTY \
                    or self.board[x0+1][y0-1] == Square.HIGHLIGHTED:
                valid_moves.append((x0, y0))
        if x0+1 != 8 and y0+1 != 8:
            if self.board[x0+1][y0+1] == Square.EMPTY \
                    or self.board[x0+1][y0+1] == Square.HIGHLIGHTED:
                valid_moves.append((x0, y0))
        if x0-1 != -1 and y0+1 != 8:
            if self.board[x0-1][y0+1] == Square.EMPTY \
                    or self.board[x0-1][y0+1] == Square.HIGHLIGHTED:
                valid_moves.append((x0, y0))
        return valid_moves

    def highlight_moves(self, moves):
        """
        Method which highlights specific squares on the game board given possible coordinates.
        :param moves: a list of tuples which represents possible coordinates
        """
        self.clear_highlighting()
        for m in moves:
            self.board[m[0]][m[1]] = Square.HIGHLIGHTED

    def clear_highlighting(self):
        """
        Clears the highlighting on a game board.
        """
        for i in range(0, 8):
            for j in range(0, 8):
                if self.board[i][j] == Square.HIGHLIGHTED:
                    self.board[i][j] = Square.EMPTY

    def to_display_data(self):
        """
        Converts the game board in a string of 64 numbers to be parsed by the client.
        :return: string of 64 numbers representing the state of the game
        """
        data = ""
        for row in self.board:
            for col in row:
                data += str(col.value)
        return data

    def make_move(self, x0, y0, x1, y1):
        """
        Updates the board for moving a piece.
        :param x0: row that piece is on
        :param y0: column that piece is on
        :param x1: row that piece is being moved to
        :param y1: column that piece is being moved to
        :return:
        """
        self.clear_highlighting()
        if (x1, y1) in self.get_valid_moves(x0, y0):
            self.board[x1][y1] = self.board[x0][y0]
            self.board[x0][y0] = Square.EMPTY
