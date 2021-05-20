# Add Player Pieces [done]
# Draw the board [done]
# Add Neutron [done]
# Move Neutron
# Move Pieces
# Check for endgame

import math
import os 
import sys

# Board Related 
board = [
    2, 2, 2, 2, 2,
    0, 0, 0, 0, 0,
    0, 0, 1, 0, 0,
    0, 0, 0, 0, 0, 
    3, 3, 3, 3, 3
]

bWidth = 5 
neutronPos = (0, 0)

INFO = []

# useful functions 
def i2xy(i):
    x = math.floor(i / bWidth)
    y = i % bWidth
    return (x, y)

def xy2i(x, y):
    return ((y * bWidth) + x)


# Custom Types 
class SpaceTypes:
    EMPTY = '.'
    NEUTRON = '*'
    PLAYER1 = 'F'
    PLAYER2 = 'S'

    def getType(t):
        if t == 0: return SpaceTypes.EMPTY
        elif t == 1: return SpaceTypes.NEUTRON
        elif t == 2: return SpaceTypes.PLAYER1
        elif t == 3: return SpaceTypes.PLAYER2
        else: return SpaceTypes.EMPTY


class Space:
    def __init__(self, x, y, sType):
        self.x = x 
        self.y = y
        self.type = SpaceTypes.getType(sType)
        self.update(self.type)
    
    def update(self, type = SpaceTypes.EMPTY):
        if (type == SpaceTypes.NEUTRON): 
            neutronPos = (self.x, self.y)

        self.type = type
        self.draw()
    
    def draw(self):
        i = xy2i(self.x, self.y)
        board[i] = self.type

class Move:
    def top(neutronIndex): 
        ox, oy = i2xy(neutronIndex)
        if (oy > 0): ny = oy - 1 
        else: ny = oy
        neutronPos = (ox, ny)
        spaceList[xy2i(neutronPos)].update(SpaceTypes.NEUTRON) # Replace new index with neutron
        spaceList[xy2i(ox, oy)].update(SpaceTypes.EMPTY) # Replace new index with neutron

    def bottom(neutronIndex): pass 
    def left(neutronIndex): pass 
    def right(neutronIndex): pass 
    def top_left(neutronIndex): pass 
    def top_right(neutronIndex): pass 
    def bottom_left(neutronIndex): pass 
    def bottom_right(neutronIndex): pass 



# Initiate 
spaceList = []
def init():
    for x in range(bWidth):
        for y in range(bWidth):
            spaceList.append(Space(x, y, board[xy2i(x, y)]))
        
# Draw Board
def printBoard(board):
    k = 0
    for i in range(len(board)):
        if i % 5 == 0:
            print("\n\n\t", end=" ")
            k += 5
            print("\t", end=" ")
        print(board[i] + " ", end=" ")
    print("\n") 

def printInfo():
    for i in INFO:
        print(i)
    
    INFO.clear()

def handleMovement(direction):
    if direction < 1 and direction > 8: 
        INFO.append('Please select a value from (1 - 8)')
        return None 
    
    if direction == 0:
        Move.top(xy2i(neutronPos))


# Gameloop
init() #Initiate board

game_is_running = True 
try:
    while game_is_running:
        os.system('clear') # Clear terminal 
        # for space in spaceList:
        #     space.update() # Update Spaces 
        
        printBoard(board) 
        direction = int(input("Where to move? (1-8): ")) - 1

        handleMovement(direction)
        printInfo()


except Exception as e:
    print(e)
    game_is_running = False 
    sys.exit()

# Function calls
