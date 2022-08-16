import string


class Board:

    def __init__(self, x=10, y=10, is_hidden=True):
        self.x = x
        self.y = y
        self.board = [[" _ " for j in range(x)] for i in range(y)]
        self.is_hidden = is_hidden

    def print_board(self):
        print(" ", end='')
        for col in range(self.x):
            print(" ", string.ascii_uppercase[col], end='')
        print("")
        for row in range(self.x):
            if row + 1 < 10:
                print(row + 1, end=' ')
            else:
                print(row + 1, end='')
            for col in range(self.y):
                print(self.board[row][col], end='')
            print("")


player_board = Board()

player_board.print_board()
