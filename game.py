from checkers import Checkers

class Game:
    # we can assume player 1 is black and player 2 is white
    def __init__(self, player1, player2):
        self.turn = player1
        self.idle = player2
        self.checker_board = Checkers()
        self.tentative_selection = None

    def make_move(self, player, x1, y1):
        if self.turn == player:
            self.checker_board.make_move(self.tentative_selection[0], self.tentative_selection[1], x1, y1)
            temp = self.turn
            self.turn = self.idle
            self.idle = temp

    def highlight_possible_moves(self, player, move):
        if self.turn == player:
            moves = self.checker_board.get_valid_moves(move[0], move[1])
            self.checker_board.highlight_moves(moves)

    def get_board(self):
        return self.checker_board.to_display_data()

    def set_tentative_selection(self, x0, y0):
        self.tentative_selection =  (x0, y0)