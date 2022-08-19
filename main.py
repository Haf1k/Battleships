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

    def __init__(self, size, x_pos, y_pos, damage=0, is_destroyed=False):
        self.size = size
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.damage = damage
        self.is_destroyed = is_destroyed

    def ship_placement(self):
        try:
            x = int(input("Please enter coordinate of X axis: "))
            y = int(input("Please enter coordinate of Y axis: "))
            orientation = input("Please choose orientation of your ship > horizontal or vertical (h  / v): ")
            if orientation not in ("h", "v"):
                raise ValueError
        except ValueError:
            print("Enter coordinates in right form: ")
            self.ship_placement()
        else:
            try:
                if orientation == "v":
                    if (x - 1) + self.size > player_board.x or (y - 1) + self.size > player_board.y:
                        raise IndexError
                    else:
                        for i in range(self.size):
                            player_board.board[(x - 1) + i][y - 1] = " X "
                else:
                    if (x - 1) + self.size > player_board.x or (y - 1) + self.size > player_board.y:
                        raise IndexError
                    else:
                        for i in range(self.size):
                            player_board.board[x - 1][(y - 1) + i] = " X "
            except IndexError:
                print("Wrong coordinates")
                self.ship_placement()

    def check_collision(self):
        pass


player_board = Board()

ship_list = [Ship(5, 1, 1), Ship(5, 1, 1)]

ship_list[0].ship_placement()

player_board.print_hidden()
player_board.print_board()
