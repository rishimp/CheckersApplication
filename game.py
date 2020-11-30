class game:
    # we can assume player 1 is black and player 2 is white
    def __init__(self, player1, player2):
        self.turn = player1
        self.idle = player2

    def make_move(self, player):
        if self.turn == player:
            return None

