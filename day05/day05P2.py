#correct answer: 20012
#refactor goal: both parts can be combined
def printGrid (grid, length):
    for y in range(length):
        print(grid[y])

def calcOverlap (grid, xLength, yLength):
    points = 0
    for y in range(yLength):
        for x in range(xLength):
            if (grid[y][x] >= 2):
                points += 1
    return points

with open("day05Input.txt", "r") as inputs:
    cleanInput = [[tuple(int(xY) for xY in coords.split(',')) for coords in line.strip().split(' -> ')] for line in inputs]

xLength = max(max((x1, x2) for (x1, x2), (y1, y2) in cleanInput)) + 2
yLength = max(max((y1, y2) for (x1, x2), (y1, y2) in cleanInput)) + 2
maxLength = max(xLength, yLength)
ventGrid = [[0 for x in range(xLength)] for y in range(yLength)]

for coordinates in cleanInput:
    #x1 = x2
    iterLength = 0
    if (coordinates[0][0] == coordinates[1][0]):
        iterLength = abs(coordinates[0][1] - coordinates[1][1]) + 1

        if (coordinates[0][1] > coordinates[1][1]):
            direction = coordinates[1][1]
        else:
            direction = coordinates[0][1]

        for y in range(iterLength):
            ventGrid[direction + y][coordinates[0][0]] += 1
    #y1 = y2
    elif (coordinates[0][1] == coordinates[1][1]):
        iterLength = abs(coordinates[0][0] - coordinates[1][0]) + 1

        if (coordinates[0][0] > coordinates[1][0]):
            direction = coordinates[1][0]
        else:
            direction = coordinates[0][0]

        for x in range(iterLength):
            ventGrid[coordinates[0][1]][direction + x] += 1
    #handle diagonals
    else:
        iterLength = abs(coordinates[0][0] - coordinates[1][0]) + 1

        if (coordinates[0][0] > coordinates[1][0]):
            directionX = -1
        else:
            directionX = 1

        if (coordinates[0][1] > coordinates[1][1]):
            directionY = -1
        else:
            directionY = 1

        for iteration in range(iterLength):
            ventGrid[coordinates[0][1] + (iteration * directionY)][coordinates[0][0] + (iteration * directionX)] += 1

print(calcOverlap(ventGrid, xLength, yLength))