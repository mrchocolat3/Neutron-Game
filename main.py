import os
from typing import Counter, Type


class Types:
	''' Custom predefiend types for the grid '''

	EMPTY = '.'
	NEUTRON = '*'
	PLAYER1 = 'F'
	PLAYER2 = 'S'

	def getTypeOf(grid):
		''' Get the item type from the grid index '''
		if grid == '.':
			return Types.EMPTY
		if grid == '*':
			return Types.NEUTRON
		if grid.startswith('F'):
			return Types.PLAYER1
		if grid.startswith('S'):
			return Types.PLAYER2


class Item:
	''' Grid has 4 items: * (Neutron), . (Empty space), F1-F5 (first player), S1-S5 (Second player) '''
	def __init__(this) -> None:
		# Get Player Orders
		this.p1Order = [(int(item) - 1) for item in input(
			"Enter the list orders for player 1. e.g (1 2 3 4 5): ").split()]
		this.p2Order = [(int(item) - 1) for item in input(
			"Enter the list orders for player 2. e.g (5 4 3 2 1): ").split()]
		
		# Set player pieces positions on grid [[y, x]]
		this.p1OrderPos = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]
		this.p2OrderPos = [[4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
		this.neutronPosition = [2, 2]

	def get_position_of(this, item: str):
		''' Takes string as input '-', '*', 'F', 'S' and returns the item position from grid '''
		if item == Types.NEUTRON:
			return this.neutronPosition, None
		if item == Types.PLAYER1:
			this.p1Order.reverse()  # [1, 2, 3] -> [3, 2, 1]
			iTemNumber = this.p1Order.pop()  # Get last item from [3, 2, 1]: 1
			this.p1Order.reverse()  # [3, 2]->[2, 3]
			this.p1Order.append(iTemNumber)  # [2, 3, 1]
			return this.p1OrderPos[iTemNumber], iTemNumber # (position, item)
		if item == Types.PLAYER2:
			this.p2Order.reverse()  # [1, 2, 3] -> [3, 2, 1]
			iTemNumber = this.p2Order.pop()  # 1
			this.p2Order.reverse()  # [3, 2]->[2, 3]
			this.p2Order.append(iTemNumber)  # [2, 3, 1]
			return this.p2OrderPos[iTemNumber], iTemNumber

	def set_position_of(this, item: str, position: list, order: int = None) -> None:
		''' Sets the position of item on grid '''
		if item == Types.NEUTRON:
			this.neutronPosition = position
		if item == Types.PLAYER1:
			this.p1OrderPos[order] = position
		if item == Types.PLAYER2:
			this.p2OrderPos[order] = position


class Grid:
	def __init__(this, item: Item) -> None:
		this.row = 5
		this.col = 5
		this.grid = [
			['F1', 'F2', 'F3', 'F4', 'F5'], # y:0, x:0-4 	(0, 0) ----------> (0, x)
			['.',  '.',  '.',  '.',  '.'], 	# y:1, x:0-4 	  |  ------------  (1, x)
			['.',  '.',  '*',  '.',  '.'], 	# y:2, x:0-4 	  |  ------------  (2, x)
			['.',  '.',  '.',  '.',  '.'], 	# y:3, x:0-4 	  |  ------------  (3, x)
			['S1', 'S2', 'S3', 'S4', 'S5'],	# y:4, x:0-4 	(y, 0) ----------  (y, x)
		]
		
		this.item = item
		this.drawGrid()

	def drawGrid(this):
		os.system('clear') # Clear the terminal
		for i in this.grid:
			print('\n', ''.join(f'{str(j):8}' for j in i), '\n') #draw the grid


	def updateGrid(this, position, itemType, order=None):
		''' Updates the grid with new item positions '''
		this.item.set_position_of(itemType, position, order)
		
		# grid[y][x] = F1-5 or S1-5 if Item is not Empty or Neutron
		this.grid[position[0]][position[1]] = f'{itemType}{f"{order + 1}" if (itemType != Types.EMPTY and itemType != Types.NEUTRON) else ""}'

		this.drawGrid()

	# Check grid types
	def isTopGridType(this, row, col, gridType):
		''' Checks if the item above current item is desired type '''
		r = row - 1 if (row - 1) >= 0 else row
		return (Types.getTypeOf(this.grid[r][col]) == gridType)

	def isTopRightGridType(this, row, col, gridType):
		''' Checks if the item on top right is desired type '''
		r = row - 1 if (row - 1) >= 0 else row
		c = col + 1 if (col + 1) < (this.col) else col
		return (Types.getTypeOf(this.grid[r][c]) == gridType)

	def isRightGridType(this, row, col, gridType):
		''' Checks if the item on right from current item is desired type '''
		c = (col + 1) if (col + 1) < (this.col) else col
		return (Types.getTypeOf(this.grid[row][c]) == gridType)

	def isBottomRightGridType(this, row, col, gridType):
		''' Checks if the item on bottom right is desired type '''
		r = row + 1 if (row + 1) <= (this.row - 1) else row
		c = col + 1 if (col + 1) <= (this.col - 1) else col
		return (Types.getTypeOf(this.grid[r][c]) == gridType)

	def isBottomGridType(this, row, col, gridType):
		''' Checks if the item bottom from current item is desired type '''
		r = row + 1 if (row + 1) <= (this.row - 1) else row
		return (Types.getTypeOf(this.grid[r][col]) == gridType)

	def isBottomLeftGridType(this, row, col, gridType):
		''' Checks if the item on bottom left is desired type '''
		r = row + 1 if (row + 1) <= (this.row - 1) else row
		c = col - 1 if (col - 1) >= 0 else col
		return (Types.getTypeOf(this.grid[r][c]) == gridType)

	def isLeftGridType(this, row, col, gridType):
		''' Checks if the item on left from current item is desired type '''
		c = col - 1 if (col - 1) >= 0 else col
		return (Types.getTypeOf(this.grid[row][c]) == gridType)

	def isTopLeftGridType(this, row, col, gridType):
		''' Checks if the item on top left is desired type '''
		r = row - 1 if (row - 1) >= 0 else row
		c = col - 1 if (col - 1) >= 0 else col
		return (Types.getTypeOf(this.grid[r][c]) == gridType)

	def moveUp(this, position, item, order=None):
		''' Moves the position of current item 1 grid top '''
		
		this.updateGrid(position, Types.EMPTY) # clear old position
		row = position[0] 
		col = position[1]
		counter = row
		
		# since we have to move maximum distance, if next grid of next grid is not empty, you can move to next grid. Else continue finding the next occupied grid and set the position to the grid before.
		while counter > 0:
			if not this.isTopGridType(counter, col, Types.EMPTY):
				break

			if counter <= 0:
				counter = 0
				break

			counter -= 1

		this.updateGrid([counter, col], item, order)

		# Check If Postion row is 0 and if so then changed by whom.

	def moveUpLeft(this, position, item, order=None):
		this.updateGrid(position, Types.EMPTY)
		row = position[0]
		col = position[1]

		r = row
		c = col
		while r > 0 and c > 0:
			r -= 1
			c -= 1
			if not this.isTopLeftGridType(r, c, Types.EMPTY):
				break

			if (c <= 0 and r <= 0):
				c = 0
				r = 0
				break

		this.updateGrid([r, c], item, order)

	def moveDownLeft(this, position, item, order=None):
		this.updateGrid(position, Types.EMPTY)
		row = position[0]
		col = position[1]

		r = row
		c = col
		while r < this.row and c > 0:
			r += 1
			c -= 1
			if not this.isBottomLeftGridType(r, c, Types.EMPTY):
				break

			if (r >= (this.row - 1) and c <= 0):
				r = this.row - 1
				c = 0
				break

		this.updateGrid([r, c], item, order)

	def moveRight(this, position, item, order=None):
		this.updateGrid(position, Types.EMPTY)
		row = position[0]
		col = position[1]

		counter = col
		while counter < this.col:
			if not this.isRightGridType(row, counter, Types.EMPTY):
				break

			if counter >= (this.col - 1):
				counter = this.col - 1
				break

			counter += 1

		this.updateGrid([row, counter], item, order)

	def moveLeft(this, position, item, order=None):
		this.updateGrid(position, Types.EMPTY)
		row = position[0]
		col = position[1]

		counter = col
		while counter > 0:
			counter -= 1
			if not this.isLeftGridType(row, counter, Types.EMPTY):
				break

			if counter <= 0:
				counter = 0
				break

		this.updateGrid([row, counter], item, order)

	def moveUpRight(this, position, item, order=None):
		this.updateGrid(position, Types.EMPTY)
		row = position[0]
		col = position[1]

		r = row
		c = col
		while r > 0 and c < this.col:
			r -= 1
			c += 1

			if (c >= (this.col - 1)):
				c = this.col - 1
				break

			if r <= 0:
				r = 0
				break

			if not this.isTopRightGridType(r, c, Types.EMPTY):
				break

		this.updateGrid([r, c], item, order)

	def moveDownRight(this, position, item, order=None):
		this.updateGrid(position, Types.EMPTY)
		row = position[0]
		col = position[1]

		r = row
		c = col
		while r < this.row and c < this.col:
			r += 1
			c += 1
			if not this.isBottomRightGridType(r, c, Types.EMPTY):
				break

			if (c >= (this.col - 1) and r >= (this.row - 1)):
				c = this.col - 1
				r = this.row - 1
				break

		this.updateGrid([r, c], item, order)

	def moveDown(this, position, item, order=None):
		this.updateGrid(position, Types.EMPTY)
		row = position[0]
		col = position[1]

		counter = 0

		while counter < this.row:
			if not this.isBottomGridType(counter, col, Types.EMPTY):
				break

			counter += 1
			if counter >= (this.row - 1):
				counter = this.row - 1
				break

		this.updateGrid([counter, col], item, order)


class Game_Manager:
	''' Manages the game '''

	def __init__(this) -> None:
		this.gameOver = None #is game over?
		this.turn = None # who is playing now? 0-1: player 1, 2-4: player 2
		this.grid = None # the grid 
		this.item = None # Item class that manages all the times on grid
		this.neutron = None # Neutron
		this.neutronPos = None # Neutrons position
		this.player1Piece = None # Current Piece that should be moved according to given order for player 1
		this.player2Piece = None # Current Piece that should be moved according to given order for player 2

	def init(this) -> None:
		''' Initiate Game Manager '''
		this.gameOver = False
		this.turn = 0
		this.item = Item()  # initiate Item
		this.grid = Grid(this.item)  # initiate Grid
		this.neutron = Types.NEUTRON
		this.player1Piece = Types.PLAYER1
		this.player2Piece = Types.PLAYER2

	def getItemType(this) -> str:
		''' Get item type based on player turn. Return Neutron if turn is 0 and 2 else return player piece '''
		if this.turn == 0 or this.turn == 2:
			return this.neutron
		if this.turn == 1:
			return this.player1Piece
		if this.turn == 3:
			return this.player2Piece
		# return this.neutron

	def getItemPosition(this, item) -> list:
		''' Get the item position from grid '''
	
		if item == this.neutron:
			return this.item.get_position_of(this.neutron)
		if item == this.player1Piece:
			return this.item.get_position_of(this.player1Piece)
		if item == this.player2Piece:
			return this.item.get_position_of(this.player2Piece)

	def handleMovement(this, direction):
		''' Handle the movement based on input '''
		item = this.getItemType()
		position, order = this.getItemPosition(item)

		if direction == 1:
			this.grid.moveUp(position, item, order)
		elif direction == 2:
			this.grid.moveUpRight(position, item, order)
		elif direction == 3:
			this.grid.moveRight(position, item, order)
		elif direction == 4:
			this.grid.moveDownRight(position, item, order)
		elif direction == 5:
			this.grid.moveDown(position, item, order)
		elif direction == 6:
			this.grid.moveDownLeft(position, item, order)
		elif direction == 7:
			this.grid.moveLeft(position, item, order)
		elif direction == 8:
			this.grid.moveUpLeft(position, item, order)

	def isGameOver(this, position):
		if this.turn < 2 and position[0] == 0:
			return True
		elif this.turn > 1 and position[0] == (this.grid.row - 1):
			return True
		else:
			return False

	def overTheGame(this):
		os.system('clear')
		if this.turn < 2:
			print("Player 1 Won!")
		if this.turn > 1:
			print("Player 2 Won!")

		this.gameOver = True

	def game_loop(this):
		try:
			while not this.gameOver:
				# Check if Game is over
				if this.isGameOver(this.getItemPosition(this.neutron)[0]):
					this.overTheGame()
					break

				if this.turn <= 1:
					d = int(input(f'player 1 direction: (1 - 8): ')) # get input and convert string to int
					this.handleMovement(d)
					this.turn += 1
				else:
					d = int(input('player 2 direction: (1 - 8): '))
					this.handleMovement(d)
					this.turn += 1

				this.turn %= 4
		except Exception as e:
			 this.game_is_running = False
			 print(e)


if __name__ == "__main__":
	GM = Game_Manager()
	GM.init()
	GM.game_loop()
