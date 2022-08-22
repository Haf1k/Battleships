import string


class Board:

    def __init__(self, x=10, y=10, is_hidden=True):
        self.x = x
        self.y = y
        self.board = [[" – " for _ in range(x)] for _ in range(y)]
        self.hidden = [[" ~ " for _ in range(x)] for _ in range(y)]
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
        print("")

    def print_hidden(self):
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
                print(self.hidden[row][col], end='')
            print("")
        print("")


class Ship:

    def __init__(self, size):
        self.size = size
        self.damage = 0
        self.is_destroyed = False
        self.x_pos = 0
        self.y_pos = 0
        self.orientation = ""

    def ship_placement(self):
        try:
            self.x_pos = int(input("Please enter coordinate of X axis: "))
            self.y_pos = int(input("Please enter coordinate of Y axis: "))
            self.orientation = input("Please choose orientation of your ship > horizontal or vertical (h  / v): ")
            if self.orientation not in ("h", "v"):
                raise ValueError
        except ValueError:
            print("Enter coordinates in right form: ")
            self.ship_placement()
        else:
            try:
                if self.orientation == "h":
                    if (self.x_pos - 1) + self.size > player_board.x or (
                            self.y_pos - 1) > player_board.y or self.check_collision():
                        raise IndexError
                    else:
                        for i in range(self.size):
                            player_board.board[self.y_pos - 1][(self.x_pos - 1) + i] = " X "
                else:
                    if (self.x_pos - 1) > player_board.x or (
                            self.y_pos - 1) + self.size > player_board.y or self.check_collision():
                        raise IndexError
                    else:
                        for i in range(self.size):
                            player_board.board[(self.y_pos - 1) + i][self.x_pos - 1] = " X "
            except IndexError:
                print("Wrong coordinates")
                self.ship_placement()

    def check_collision(self):
        if self.orientation == "v":
            for i in range(self.size):
                if player_board.board[(self.y_pos - 1) + i][self.x_pos - 1] == " X ":
                    return True
        elif self.orientation == "h":
            for i in range(self.size):
                if player_board.board[self.y_pos - 1][(self.x_pos - 1) + i] == " X ":
                    return True


player_board = Board()

player_board.print_hidden()
player_board.print_board()

ship_list = [Ship(5), Ship(5)]

ship_list[0].ship_placement()
player_board.print_board()
ship_list[1].ship_placement()

# player_board.board[1][3] = " X "

# player_board.print_hidden()
player_board.print_board()
