#correct answer: FGKCKBZG
def printGrid(grid, right, down):
    for y in range(down):
        print(grid[y][:right])

with open("day13Input.txt", "r") as inputs:
    cleanInput = [ [path for path in line.strip().split(',')] for line in inputs]

gridCoordinates = cleanInput[:cleanInput.index([''])]

folds = []
#11 is how many characters until we hit either x or y in fold along
for fold in cleanInput[cleanInput.index(['']) + 1:]:
    folds.append(fold[0][11:].split('='))

timesToFold = len(folds)
minRight = 0
maxRight = 2 * max([int(x[1]) for x in folds if x[0] == 'x']) + 1
minDown = 0
maxDown = 2 * max([int(y[1]) for y in folds if y[0] == 'y']) + 1
markedGrid = [['.' for x in range(maxRight)]for y in range(maxDown)]
#actually mark the grid
for coords in gridCoordinates:
    markedGrid[int(coords[1])][int(coords[0])] = '#'

for foldDir in folds:
    if (foldDir[0] == 'x'):
        xDepth = int(foldDir[1])
        for y in range(maxDown):
            for x in range(xDepth + 1, maxRight):
                if (markedGrid[y][x] == '#'):
                    markedGrid[y][maxRight - 1 - x] = '#'
        maxRight -= (xDepth + 1)
    else:
        yDepth = int(foldDir[1])
        for y in range(yDepth + 1, maxDown):
            for x in range(maxRight):
                if (markedGrid[y][x] == '#'):
                    markedGrid[maxDown - 1 - y][x] = '#'
        maxDown -= (yDepth + 1)

printGrid(markedGrid, maxRight, maxDown)