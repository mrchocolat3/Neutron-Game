import math
x = [i for i in range(25)]


def printBoard(board):
    k = 0
    for i in range(len(board)):
        if i % 5 == 0:
            print("\n\n\t", end=" ")
            k += 5
            print("\t", end=" ")
        print(f"{(board[i]):4} ", end=" ")
    print("\n")


def xy2i(x, y): return (y * 5) + x


printBoard(x)

m = 2
n = 4

print(f'i = {xy2i(m, n)}')
# top-right
if m == 0:
    tr = x[xy2i(m, n):: -4]
if m <= 2 and m >= 1:
    tr = x[xy2i(m, n): m * n: -4]
if m == 3:
    tr = x[xy2i(m, n): (m * n) + 1: -4]
if m == 4:
    tr = x[xy2i(m, n)]

print(f'tr: {str(tr):4}')

# top-left
if m == 0:
    tl = x[xy2i(m, n)]
if m == 1:
    tl = x[xy2i(m, n):: -6]
if m >= 2 and m <= 4:
    tl = x[xy2i(m, n):: -6]
# if m == 4:
#     tl = x[xy2i(m, n)]

print(f'tl: {str(tl):4}')

# top-right
print(f'br: {str(x[xy2i(m, n): : 6]):4}')

# top-right
print(f'bl: {str(x[xy2i(m, n): len(x) - int(m / 5): 4]):4}')
