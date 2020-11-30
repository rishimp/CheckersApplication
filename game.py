from checkers import Checkers

class Game:

    def __init__(self, player1, player2):
        """Initializes a game with 2 players

        Args:
            player1 (String): [The player with black pieces and goes first]
            player2 (String): [The player with white piecies]
        """
        self.turn = player1
        self.idle = player2
        self.b_player = player1
        self.w_player = player2
        self.checker_board = Checkers()
        self.tentative_selection = None

    def is_correct_side(self, player, color):
        """[Checks if the player is on the correct side by checking the color]

        Args:
            player (string): [the player whose side we want to check]
            color (string): [the color of the side the player is on]

        Returns:
            [boolean]: [return if the color matches the player and his side]
        """
        if self.b_player == player:
            if color == "b":
                return True
        elif self.w_player == player:
            if color == "w":
                return True
        return False

    def make_move(self, player, x1, y1):
        """[changes the board by making a move]

        Args:
            player (string): [the player who makes the move]
            x1 (int): [the x cordinate on the board where the player wants to move the piece]
            y1 (int): [the y cordinate on the board where the player wants to move the piece]
        """
        if self.turn == player:
            x0 = self.tentative_selection[0]
            y0 = self.tentative_selection[1]
            self.checker_board.make_move(x0, y0, x1, y1)
            temp = self.turn
            self.turn = self.idle
            self.idle = temp

    def highlight_possible_moves(self, player, x0, y0):
        """[darkens squares on the board for possible moves for a player]

        Args:
            player (string): [the player the user selected for whom we want to see possible moves]
            x0 (int): [The X cordinate of the player's current position]
            y0 (int): [The Y cordinate of the player's current position]
        """
        if self.turn == player:
            moves = self.checker_board.get_valid_moves(x0, y0)
            self.checker_board.highlight_moves(moves)

    def get_board(self):
        """[returns the game board by displaying its data]

        Returns:
            [List]: [return a list of column values on the board]
        """
        return self.checker_board.to_display_data()

    def get_unhighlighted_board(self):
        """[returns the unhighlited game board by displaying its data]

        Returns:
            [List]: [return a list of column values on the board without any highliting]
        """
        self.checker_board.clear_highlighting()
        return self.checker_board.to_display_data()

    def set_tentative_selection(self, x0, y0):
        """[Sets the desired selection of the user]

        Args:
            x0 (int): [the x cordinate of the user's desired move]
            y0 (int): [the y cordinate of the user's desired move]
        """
        self.tentative_selection = (x0, y0)
    
