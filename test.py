import os
from typing import Counter, Type


class Types:
    EMPTY = '.'
    NEUTRON = '*'
    PLAYER1 = 'F'
    PLAYER2 = 'S'

    def getTypeOf(grid):
        if grid == '.':
            return Types.EMPTY
        if grid == '*':
            return Types.NEUTRON
        if grid == 'F':
            return Types.PLAYER1
        if grid == 'S':
            return Types.PLAYER2


class Grid:
    def __init__(self) -> None:
        self.row = 5
        self.col = 5
        self.grid = [
            ['F', 'F', 'F', 'F', 'F'],
            ['.', '.', '.', '.', '.'],
            ['.', '.', '', '.', '.'],
            ['.', '.', '.', '.', '*'],
            ['S', 'S', 'S', 'S', 'S'],
        ]

    def drawGrid(self):
        os.system('clear')
        for i in self.grid:
            print(' '.join(k for k in i) + '\n')

    def updateGrid(self, row, col, itemType):
        self.grid[row][col] = itemType
        self.drawGrid()


class GridManager(Grid):
    def __init__(self) -> None:
        super().__init__()

    # Check grid types
    def isTopGridType(self, row, col, gridType):
        return (Types.getTypeOf(self.grid[row - 1][col]) == gridType)

    def isTopRightGridType(self, row, col, gridType):
        return (Types.getTypeOf(self.grid[row - 1][col + 1]) == gridType)

    def isRightGridType(self, row, col, gridType):
        return (Types.getTypeOf(self.grid[row][col + 1]) == gridType)

    def isBottomRightGridType(self, row, col, gridType):
        return (Types.getTypeOf(self.grid[row + 1][col + 1]) == gridType)

    def isBottomGridType(self, row, col, gridType):
        return (Types.getTypeOf(self.grid[row + 1][col]) == gridType)

    def isBottomLeftGridType(self, row, col, gridType):
        return (Types.getTypeOf(self.grid[row + 1][col - 1]) == gridType)

    def isLeftGridType(self, row, col, gridType):
        return (Types.getTypeOf(self.grid[row][col - 1]) == gridType)

    def isTopLeftGridType(self, row, col, gridType):
        return (Types.getTypeOf(self.grid[row - 1][col - 1]) == gridType)


class MovementSystem(GridManager):
    def __init__(self) -> None:
        super().__init__()

    def moveUp(self, row, col, itemType):
        self.grid[row][col] = Types.EMPTY

        counter = row
        while counter >= 0:
            counter -= 1
            if not self.isTopGridType(counter, col, Types.EMPTY):
                break

        self.grid[counter][col] = itemType
        self.drawGrid()

    def moveUpLeft(self, row, col, item):
        self.grid[row][col] = Types.EMPTY

        counter = col
        while counter >= 0:
            counter -= 1
            if not self.isTopLeftGridType(counter, counter, Types.EMPTY):
                break

        self.grid[counter][counter] = item
        self.drawGrid()

    def moveLeft(self, row, col, item):
        self.grid[row][col] = Types.EMPTY
        counter = col
        while counter >= 0:
            counter -= 1
            if not self.isLeftGridType(row, counter, Types.EMPTY):
                break

        self.grid[row][counter]
        self.drawGrid()

    def moveRight(self, row, col, item):
        self.grid[row][col] = Types.EMPTY
        counter = 0
        while counter <= col:
            counter += 1
            if not self.isLeftGridType(row, counter, Types.EMPTY):
                break

        self.grid[row][counter]
        self.drawGrid()

    def moveDown(self, row, col, item):
        # Clear old position
        self.grid[row][col] = Types.EMPTY
        counter = 0

        while counter <= row:
            counter += 1
            if not self.isBottomGridType(counter, col, Types.EMPTY):
                break

        self.grid[counter][col] = item
        self.drawGrid()


class Item:
    def __init__(self, type) -> None:
        self.type = type


gridManager = GridManager()
gridManager.drawGrid()

movementSystem = MovementSystem()
movementSystem.moveUpLeft(3, 4, Types.NEUTRON)
