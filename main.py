import string

POSSIBLE_SHIPS = [5, 4, 3, 2, 3]

class Board:

    def __init__(self, x=10, y=10, is_hidden=True):
        self.x = x
        self.y = y
        self.play_field = [[" – " for _ in range(x)] for _ in range(y)]
        self.hidden_play_field = [[" ~ " for _ in range(x)] for _ in range(y)]
        self.is_hidden = is_hidden
        self.ship_list = []

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
                print(self.play_field[row][col], end='')
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
                print(self.hidden_play_field[row][col], end='')
            print("")
        print("")

    def shoot(self):
        x_coordinate = int(input("Please enter coordinate of X axis you want to shoot at: "))
        y_coordinate = int(input("Please enter coordinate of Y axis you want to shoot at: "))
        if self.play_field[y_coordinate - 1][x_coordinate - 1] == " X ":
            self.play_field[y_coordinate - 1][x_coordinate - 1] = " # "
            self.hidden_play_field[y_coordinate - 1][x_coordinate - 1] = " # "
            print("HIT")
            self.find_ship([x_coordinate, y_coordinate]).deal_damage()
        else:
            self.play_field[y_coordinate - 1][x_coordinate - 1] = " O "
            self.hidden_play_field[y_coordinate - 1][x_coordinate - 1] = " O "
            print("MISS")

    def find_ship(self, shoot_coordinates):
        for each in self.ship_list:
            if shoot_coordinates in each.ship_coordinates:
                return each


class Ship:

    def __init__(self, size, board):
        self.size = size
        self.damage = 0
        self.destroyed = False
        self.x_pos = 0
        self.y_pos = 0
        self.ship_coordinates = []
        self.orientation = ""
        self.ships_board = board

    def ship_placement(self):
        letter_to_num = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}
        try:
            self.x_pos = letter_to_num[input("Please enter coordinate of X axis: ").upper()]
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
                    if (self.x_pos - 1) + self.size > self.ships_board.x or (
                            self.y_pos - 1) > self.ships_board.y or self.check_collision():
                        raise IndexError
                    else:
                        for i in range(self.size):
                            self.ships_board.play_field[self.y_pos - 1][(self.x_pos - 1) + i] = " X "
                            self.ship_coordinates.append([self.x_pos + i, self.y_pos])
                else:
                    if (self.x_pos - 1) > self.ships_board.x or (
                            self.y_pos - 1) + self.size > self.ships_board.y or self.check_collision():
                        raise IndexError
                    else:
                        for i in range(self.size):
                            self.ships_board.play_field[(self.y_pos - 1) + i][self.x_pos - 1] = " X "
                            self.ship_coordinates.append([self.x_pos, self.y_pos + i])

            except IndexError:
                print("Wrong coordinates")
                self.ship_placement()
        print(self.ship_coordinates)

    def check_collision(self):
        if self.orientation == "v":
            for i in range(self.size):
                if self.ships_board.play_field[(self.y_pos - 1) + i][self.x_pos - 1] == " X ":
                    return True
        elif self.orientation == "h":
            for i in range(self.size):
                if self.ships_board.play_field[self.y_pos - 1][(self.x_pos - 1) + i] == " X ":
                    return True

    def deal_damage(self):
        self.damage += 1

    def is_destroyed(self):
        if self.damage >= self.size:
            self.destroyed = True


def playervsplayer():
    while True:
        try:
            playfield = int(input("Select size of play-field (5 - 10): "))
            print(type(playfield))
            print(playfield)
            if playfield != (5 or 6 or 7 or 8 or 9 or 10):
                raise ValueError
            break
        except ValueError:
            print("Not a valid option!")

    player1_board = Board(playfield, playfield)
    player2_board = Board(playfield, playfield)

    # TODO there is really not a point to continue this because it is nonsense to play battleships on one computer in
    #  this form


def playervspc():
    while True:
        try:
            playfield = int(input("Select size of play-field (5 - 10): "))
            print(type(playfield))
            print(playfield)
            if playfield not in range(5, 11):
                raise ValueError
            break
        except ValueError:
            print("Not a valid option!")

    player1_board = Board(playfield, playfield)
    computer_board = Board(playfield, playfield)

    while True:
        try:
            number_of_ships = int(input("How many ships do you want in the game? (1 - 5): "))
            if number_of_ships not in range(1, 6):
                raise ValueError
            break
        except ValueError:
            print("Not a valid option!")

    for i in range(number_of_ships):
        player1_board.print_board()
        player1_board.ship_list.append(Ship(POSSIBLE_SHIPS[i], player1_board))
        player1_board.ship_list[i].ship_placement()


def game():
    print("Welcome to the game of BATTLESHIPS!\n\n")
    print("""88                                     88                      88          88  
88                       ,d      ,d    88                      88          ""    
88                       88      88    88                      88                
88,dPPYba,  ,adPPYYba, MM88MMM MM88MMM 88  ,adPPYba, ,adPPYba, 88,dPPYba,  88  8b,dPPYba,  ,adPPYba, 
88P'    "8a ""     `Y8   88      88    88 a8P_____88 I8[    "" 88P'    "8a 88  88P'    "8a I8[    "" 
88       d8 ,adPPPPP88   88      88    88 8PP\"\"\"\"\"\"\"  `"Y8ba,  88       88 88  88       d8  `"Y8ba,
88b,   ,a8" 88,    ,88   88,     88,   88 "8b,   ,aa aa    ]8I 88       88 88  88b,   ,a8" aa    ]8I 
8Y"Ybbd8"'  `"8bbdP"Y8   "Y888   "Y888 88  `"Ybbd8"' `"YbbdP"' 88       88 88  88`YbbdP"'  `"YbbdP"'    
									                                           88           
									                                           88  
""")
    print("Which game mode do you want to play?\n")
    print("Player vs Player: A \tPlayer vs. Computer: B\n\n")

    gamemode = input("Input letter according to your choice: ").upper()

    match gamemode:
        case "A":
            print("PLAYER vs PLAYER")

            playervsplayer()

        case "B":
            print("PLAYER VS PC")

            playervspc()
        case other:
            print("invalid input")


game()

"""
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
print(player_board.ship_list[0].damage)
print(player_board.ship_list[1].damage)
"""
