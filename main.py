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
    0, 0, 0, 0, 0,
    1, 0, 0, 0, 0,
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
        if t == 0:
            return SpaceTypes.EMPTY
        elif t == 1:
            return SpaceTypes.NEUTRON
        elif t == 2:
            return SpaceTypes.PLAYER1
        elif t == 3:
            return SpaceTypes.PLAYER2
        else:
            return SpaceTypes.EMPTY


class Space:
    def __init__(self, x, y, sType):
        self.x = x
        self.y = y
        self.type = SpaceTypes.getType(sType)
        self.update(self.type)

    def update(self, type=SpaceTypes.EMPTY):
        global neutronPos
        if (type == SpaceTypes.NEUTRON):
            neutronPos = (self.x, self.y)

        self.type = type
        self.draw()

    def draw(self):
        i = xy2i(self.x, self.y)
        board[i] = self.type


class Move:
    def top(ox, oy):
        global neutronPos

        for y in range(bWidth):
            if board[xy2i(ox, y)] == SpaceTypes.EMPTY:
                board[xy2i(ox, y)] = SpaceTypes.NEUTRON
                board[xy2i(ox, oy)] = SpaceTypes.EMPTY
                neutronPos = (ox, y)
                break

    def bottom(ox, oy):
        global neutronPos

        for y in range(bWidth - 1, 0, -1):
            if board[xy2i(ox, y)] == SpaceTypes.EMPTY:
                board[xy2i(ox, y)] = SpaceTypes.NEUTRON
                board[xy2i(ox, oy)] = SpaceTypes.EMPTY
                neutronPos = (ox, y)
                break

    def left(ox, oy):
        global neutronPos

        for x in range(bWidth - 1, 0, -1):
            if board[xy2i(x, oy)] == SpaceTypes.EMPTY:
                board[xy2i(x, oy)] = SpaceTypes.NEUTRON
                board[xy2i(ox, oy)] = SpaceTypes.EMPTY
                neutronPos = (x, oy)
                break

    def right(ox, oy):
        global neutronPos

        for x in range(bWidth):
            if board[xy2i(x, oy)] == SpaceTypes.EMPTY:
                board[xy2i(x, oy)] = SpaceTypes.NEUTRON
                board[xy2i(ox, oy)] = SpaceTypes.EMPTY
                neutronPos = (x, oy)
                break

    def top_left(ox, oy):
        global neutronPos

        # if oy - y >= 0 and ox >= 0:
        #     oy -= 1
        #     ox -= 1

        for y in range(oy, 0, -1):
            print(y)

        # board[xy2i(ox, oy)] = SpaceTypes.NEUTRON
        # board[xy2i(ox + 1, oy + 1)] = SpaceTypes.EMPTY
        # neutronPos = (ox, oy)

    def top_right(ox, oy):
        global neutronPos

        if oy > 0 and ox > 0:
            oy -= 1
            ox += 1

        board[xy2i(ox, oy)] = SpaceTypes.NEUTRON
        board[xy2i(ox - 1, oy + 1)] = SpaceTypes.EMPTY
        neutronPos = (ox, oy)

    def bottom_left(ox, oy):
        global neutronPos

        if oy > 0 and ox > 0:
            oy += 1
            ox -= 1

        board[xy2i(ox, oy)] = SpaceTypes.NEUTRON
        board[xy2i(ox + 1, oy - 1)] = SpaceTypes.EMPTY
        neutronPos = (ox, oy)

    def bottom_right(ox, oy):
        global neutronPos

        if oy > 0 and ox > 0:
            oy += 1
            ox += 1

        board[xy2i(ox, oy)] = SpaceTypes.NEUTRON
        board[xy2i(ox - 1, oy - 1)] = SpaceTypes.EMPTY
        neutronPos = (ox, oy)


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
        Move.top(neutronPos[0], neutronPos[1])

    if direction == 1:
        Move.top_right(neutronPos[0], neutronPos[1])

    if direction == 2:
        Move.right(neutronPos[0], neutronPos[1])

    if direction == 3:
        Move.bottom_right(neutronPos[0], neutronPos[1])

    if direction == 4:
        Move.bottom(neutronPos[0], neutronPos[1])

    if direction == 5:
        Move.bottom_left(neutronPos[0], neutronPos[1])

    if direction == 6:
        Move.left(neutronPos[0], neutronPos[1])

    if direction == 7:
        Move.top_left(neutronPos[0], neutronPos[1])

    printBoard(board)


# Gameloop
init()  # Initiate board

game_is_running = True
try:
    while game_is_running:
        os.system('clear')  # Clear terminal
        # for space in spaceList:
        #     space.update() # Update Spaces

        printBoard(board)
        direction = int(input(
            "Where to move? 1. top, 2. top-right, 3. right, 4. down-right, 5. down, 6. down-left, 7. left, 8. top-left\nDirection: ")) - 1

        handleMovement(direction)
        printInfo()


except Exception as e:
    print(e)
    game_is_running = False
    sys.exit()

# Function calls
