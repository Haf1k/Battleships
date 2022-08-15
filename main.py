class Board:

    def __init__(self, x=10, y=10, is_hidden = True):
        self.x = x
        self.y = y
        self.is_hidden = is_hidden

    def print_board(self):
        for each in range(self.x):
