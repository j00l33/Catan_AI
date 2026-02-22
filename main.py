import random
import string

# Initial fleshing out of the catan game itself prototype
# Proposed classes: tile, board, player, structure, card 

class road:
    def __init__(self):
        self.exists = False
        self.player = False

class structure:
    def __init__(self):
        self.exists = False
        self.player = False

class tile:
    def __init__(self, resource_type, dice_number, robbed_state):
        self.resource_type = resource_type
        self.dice_number = dice_number
        self.robbed_state = robbed_state
    def __str__(self):
        return f"Tile: {self.resource_type} R: {self.dice_number}"


class board:
    def __init__(self):
        board_template = [
        "0000sxsxsxsxsxsxs0000",
        "0000xtttxtttxtttx0000",
        "00sxsxsxsxsxsxsxsxs00",
        "00xtttxtttxtttxtttx00",
        "sxsxsxsxsxsxsxsxsxsxs",
        "xtttxtttxtttxtttxtttx",
        "sxsxsxsxsxsxsxsxsxsxs",
        "00xtttxtttxtttxtttx00",
        "00sxsxsxsxsxsxsxsxs00",
        "0000xtttxtttxtttx0000",
        "0000sxsxsxsxsxsxs0000"]

        board_map = [[0 for _ in range(21)] for _ in range(11)]

        for row in range(11):
            column = 0
            while column < 21:
                if board_template[row][column] == "s":
                    board_map[row][column] = structure()
                elif board_template[row][column] == "x":
                    board_map[row][column] = road()
                elif board_template[row][column] == "t":
                    print("C: " + str(column) + " R: " + str(row))
                    tile_first = tile(random.choice(string.ascii_lowercase), random.randint(0,4), 0)
                    board_map[row][column] = tile_first
                    board_map[row][column+1] = tile_first
                    board_map[row][column+2] = tile_first
                    column += 2
                column+=1
        
        print(board_map)
        
                    

    
Board = board()



