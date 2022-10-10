import string
import random

POSSIBLE_SHIPS = [5, 4, 3, 2, 3]
LETTER_TO_NUM = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}


class Board:

    def __init__(self, x=10, y=10):
        self.x = x
        self.y = y
        self.play_field = [[" – " for _ in range(x)] for _ in range(y)]
        self.hidden_play_field = [[" ~ " for _ in range(x)] for _ in range(y)]
        self.ship_list = []

    # Function prints row with letters and column with numbers according to chosen size of playfield
    # Then it's filled either with character for visible board or invisible board according to variable "visibility"
    def print_board(self, visibility=True):
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
                if visibility:
                    print(self.play_field[row][col], end='')
                else:
                    print(self.hidden_play_field[row][col], end='')
            print("")
        print("")

    # Function for shooting, takes input and checks if on selected coordinates is ship or not. On the coordinates it
    # changes character depending on whether there was hit or not. If hit, calls find_ship and deal_damage
    # If there is computer round for shooting, it selects random coordinates
    def shoot(self, player_input=True):
        while True:
            try:
                if player_input:
                    x_coordinate = LETTER_TO_NUM[
                        input("Please enter coordinate of X axis you want to shoot at: ").upper()]
                    y_coordinate = int(input("Please enter coordinate of Y axis you want to shoot at: "))
                else:
                    x_coordinate = random.randint(1, self.x)
                    y_coordinate = random.randint(1, self.x)
                if self.play_field[y_coordinate - 1][x_coordinate - 1] == " X ":
                    self.play_field[y_coordinate - 1][x_coordinate - 1] = " # "
                    self.hidden_play_field[y_coordinate - 1][x_coordinate - 1] = " # "
                    print("HIT\n")
                    self.find_ship([x_coordinate, y_coordinate]).deal_damage()
                elif self.play_field[y_coordinate - 1][x_coordinate - 1] == " # ":
                    print("MISS\n")
                else:
                    self.play_field[y_coordinate - 1][x_coordinate - 1] = " O "
                    self.hidden_play_field[y_coordinate - 1][x_coordinate - 1] = " O "
                    print("MISS\n")
                break
            except (KeyError, ValueError, IndexError):
                print("Enter coordinates in right form: ")

    def find_ship(self, shoot_coordinates):
        for each in self.ship_list:
            if shoot_coordinates in each.ship_coordinates:
                return each

    def fleet_status(self):
        destroyed_ships = 0
        for each in self.ship_list:
            if each.destroyed:
                destroyed_ships += 1
        if destroyed_ships == len(self.ship_list):
            return False
        else:
            return True


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

    # Function checks if ship can be placed in selected coordinates, if it's out of boundaries of playfield, throws
    # exception. Also checks for collision with other ships by calling check_collision
    # IF it's computers turn, coordinates are selected randomly until all ships are placed.
    def ship_placement(self, size=10, player_input=True):
        try:
            if player_input:
                self.x_pos = LETTER_TO_NUM[input("Please enter coordinate of X axis: ").upper()]
                self.y_pos = int(input("Please enter coordinate of Y axis: "))
                self.orientation = input("Please choose orientation of your ship > horizontal or vertical (h  / v): ")
                if self.orientation not in ("h", "v"):
                    raise ValueError
            else:
                self.x_pos = random.randint(1, size)
                self.y_pos = random.randint(1, size)
                orientation = ["h", "v"]
                self.orientation = random.choice(orientation)
        except (ValueError, KeyError):
            print("Enter coordinates in right form: ")
            self.ship_placement(size, player_input)

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
                self.ship_placement(size, player_input)

    # Checks if position of new ship is not colliding with already existing ship. If it is, returns True
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
        print("Damage dealt", self.damage, "/", self.size)
        self.is_destroyed()

    def is_destroyed(self):
        if self.damage >= self.size:
            self.destroyed = True
            print("Ship destroyed\n\n")

# Function for setting up playarea in player vs pc mode. Player selects size of playarea and number of ships.
def player_vs_pc():
    while True:
        try:
            playarea = int(input("Select size of play-area (5 - 10): "))
            if playarea not in range(5, 11):
                raise ValueError
            break
        except ValueError:
            print("Not a valid option!")

    player1_board = Board(playarea, playarea)
    computer_board = Board(playarea, playarea)

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
        player1_board.ship_list[i].ship_placement(playarea, True)

        computer_board.print_board()
        computer_board.ship_list.append(Ship(POSSIBLE_SHIPS[i], computer_board))
        computer_board.ship_list[i].ship_placement(playarea, False)
    return player1_board, computer_board


# Body of the game. After selecting gamemode and setting play area, player and computer changes turns with shooting
# until some of them destroys all the enemy ships.
def game():
    while True:
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
        print("Player vs Player: A \tPlayer vs. Computer: B \t\tQuit: Q\n\n")

        gamemode = input("Input letter according to your choice: ").upper()

        match gamemode:

            # case "A":
            #   print("PLAYER vs PLAYER")
            #  return
            # playervsplayer()

            case "B":
                print("PLAYER VS PC")

                player, computer = player_vs_pc()

            case "Q":
                break

            case _other:
                print("Invalid input")
                continue

        print("Alright everything is set! Let the fight begin!")

        while True:

            if gamemode == "A":
                pass

            elif gamemode == "B":

                print("Players turn!\n")
                player.print_board()
                computer.print_board(False)
                computer.shoot(True)

                if not computer.fleet_status():
                    print("Game is OVER!\nPlayer WON!\n")
                    break

                print("Computers turn!\n")
                player.shoot(False)

                if not player.fleet_status():
                    print("Game is OVER!\nComputer WON!\n")
                    break

        print("Do you want to play again?")
        print("Yes: Y \tNo: N\n\n")

        play_again = input("Input letter according to your choice: ").upper()

        match play_again:
            case "Y":
                continue

            case "N":
                break
            case _other:
                print("Invalid input")


game()
