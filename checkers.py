from enum import Enum


class Square(Enum):
    WHITE_MAN = 1
    WHITE_KING = 2
    BLACK_MAN = 3
    BLACK_KING = 4
    EMPTY = 5
    INVALID = 6
    HIGHLIGHTED = 7


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
        valid_moves = []
        if y0-1 == -1:
            if self.board[x0-1][y0+1] == Square.EMPTY:
                valid_moves.append((x0-1, y0+1))
        elif y0+1 == 8:
            if self.board[x0-1][y0-1] == Square.EMPTY:
                valid_moves.append((x0-1, y0-1))
        else:
            if self.board[x0-1][y0+1] == Square.EMPTY:
                valid_moves.append((x0-1, y0+1))
            if self.board[x0-1][y0-1] == Square.EMPTY:
                valid_moves.append((x0-1, y0-1))
        return valid_moves

    # returns all possible moves that a black man piece can make or None
    def _get_valid_man_moves_black(self, x0, y0):
        valid_moves = []
        if y0-1 == -1:
            if self.board[x0+1][y0+1] == Square.EMPTY:
                valid_moves.append((x0-1, y0+1))
        elif y0+1 == 8:
            if self.board[x0+1][y0-1] == Square.EMPTY:
                valid_moves.append((x0-1, y0-1))
        else:
            if self.board[x0+1][y0+1] == Square.EMPTY:
                valid_moves.append((x0-1, y0+1))
            if self.board[x0+1][y0-1] == Square.EMPTY:
                valid_moves.append((x0-1, y0-1))
        return valid_moves

    # returns all possible moves that a king piece can make or None
    def _get_valid_king_moves(self, x0, y0):
        valid_moves = []
        if x0-1 != -1 and y0-1 != -1:
            if self.board[x0-1][y0-1] == Square.EMPTY:
                valid_moves.append((x0, y0))
        if x0+1 != 8 and y0-1 != -1:
            if self.board[x0+1][y0-1] == Square.EMPTY:
                valid_moves.append((x0, y0))
        if x0+1 != 8 and y0+1 != 8:
            if self.board[x0+1][y0+1] == Square.EMPTY:
                valid_moves.append((x0, y0))
        if x0-1 != -1 and y0+1 != 8:
            if self.board[x0-1][y0+1] == Square.EMPTY:
                valid_moves.append((x0, y0))
        return valid_moves

    def highlight_moves(self, moves):
        self.clear_highlighting()
        for m in moves:
            self.board[m[0]][m[1]] = Square.HIGHLIGHTED

    def clear_highlighting(self):
        for i in range(0, 8):
            for j in range(0, 8):
                if self.board[i][j] == Square.HIGHLIGHTED:
                    self.board[i][j] = Square.EMPTY

    def to_display_data(self):
        data = ""
        for row in self.board:
            for col in row:
                data += str(col.value)
        return data

c = Checkers()
print(c.to_display_data())
