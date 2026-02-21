import random
import string

#board - hexagon (3x3x3x3x3) - tile (type + number) - peices are placed IN BETWEEN TIELES
#players - rources - points - owned structures - card 
#turn - dice (rob) - trade or build or  use card
#loop - players take turns 

class tile:
    def __init__(self, resource_type, dice_number, robbed_state):
        self.resource_type = resource_type
        self.dice_number = dice_number
        self.robbed_state = robbed_state
    def tile_print(self):
        print("Tile (r,n): " + str(self.resource_type) + " " + str(self.dice_number))

class board:
    def __init__(self, tiles):
        self.tiles = tiles
    

def create_board():
    board = []
    for i in range(-2,3):
        board_layer = []
        for j in range (5 - abs(i)):
            board_layer.append(tile(random.choice(string.ascii_lowercase), random.randint(0,4), 0))
            board_layer[-1].tile_print()
        board.append(board_layer)
    return board

the_board = board(create_board())



