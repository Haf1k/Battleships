import string


class Board:

    def __init__(self, x=10, y=10, is_hidden=True):
        self.x = x
        self.y = y
        self.board = [[" – " for _ in range(x)] for _ in range(y)]
        self.hidden = [[" ~ " for _ in range(x)] for _ in range(y)]
        self.is_hidden = is_hidden
        self.ship_list = [Ship(5), Ship(5)]

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

    def shoot(self):
        x_coordinate = int(input("Please enter coordinate of X axis you want to shoot at: "))
        y_coordinate = int(input("Please enter coordinate of Y axis you want to shoot at: "))
        if self.board[y_coordinate-1][x_coordinate-1] == " X ":
            self.board[y_coordinate - 1][x_coordinate - 1] = " # "
            self.hidden[y_coordinate - 1][x_coordinate - 1] = " # "
            print("HIT")
        else:
            self.board[y_coordinate - 1][x_coordinate - 1] = " O "
            self.hidden[y_coordinate - 1][x_coordinate - 1] = " O "
            print("MISS")


class Ship:

    def __init__(self, size):
        self.size = size
        self.damage = 0
        self.is_destroyed = False
        self.x_pos = 0
        self.y_pos = 0
        self.coordinates = []
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
                            self.coordinates.append([self.x_pos + i, self.y_pos])
                else:
                    if (self.x_pos - 1) > player_board.x or (
                            self.y_pos - 1) + self.size > player_board.y or self.check_collision():
                        raise IndexError
                    else:
                        for i in range(self.size):
                            player_board.board[(self.y_pos - 1) + i][self.x_pos - 1] = " X "
                            self.coordinates.append([self.x_pos, self.y_pos + i])

            # TODO: meant to do something here, but forgot what > change X axis to letter in input

            except IndexError:
                print("Wrong coordinates")
                self.ship_placement()
        print(self.coordinates)

    def check_collision(self):
        if self.orientation == "v":
            for i in range(self.size):
                if player_board.board[(self.y_pos - 1) + i][self.x_pos - 1] == " X ":
                    return True
        elif self.orientation == "h":
            for i in range(self.size):
                if player_board.board[self.y_pos - 1][(self.x_pos - 1) + i] == " X ":
                    return True

    def get_damage(self):
        self.damage += 1


player_board = Board()

player_board.print_hidden()
player_board.print_board()


player_board.ship_list[0].ship_placement()
player_board.print_board()
player_board.ship_list[1].ship_placement()
player_board.print_board()
player_board.shoot()

# player_board.board[1][3] = " X "

player_board.print_hidden()
player_board.print_board()
