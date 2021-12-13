#correct answer: 368
flashCount = 0

def recursive (grid, x, y, minLeft, maxRight, minUp, maxDown, alreadyFlashed):
    if ((x, y) in alreadyFlashed):
        return False

    grid[y][x] += 1

    if (grid[y][x] > 9):
        global flashCount
        flashCount += 1
        alreadyFlashed.append((x, y))
        grid[y][x] = 0
        if ((x > minLeft and recursive(grid, x - 1, y, minLeft, maxRight, minUp, maxDown, alreadyFlashed) ) or
                (x < maxRight and recursive(grid, x + 1, y, minLeft, maxRight, minUp, maxDown, alreadyFlashed)) or
                (y > minUp and recursive(grid, x, y - 1, minLeft, maxRight, minUp, maxDown, alreadyFlashed)) or
                (y < maxDown and recursive(grid, x, y + 1, minLeft, maxRight, minUp, maxDown, alreadyFlashed)) or
                (x > minLeft and y > minUp and recursive(grid, x - 1, y - 1, minLeft, maxRight, minUp, maxDown, alreadyFlashed)) or
                (x < maxRight and y > minUp and recursive(grid, x + 1, y - 1, minLeft, maxRight, minUp, maxDown, alreadyFlashed)) or
                (x > minLeft and y < maxDown and recursive(grid, x - 1, y + 1, minLeft, maxRight, minUp, maxDown, alreadyFlashed)) or
                (x < maxRight and y < maxDown and recursive(grid, x + 1, y + 1, minLeft, maxRight, minUp, maxDown, alreadyFlashed))):
            pass

    return False

with open("day11Input.txt", "r") as inputs:
    cleanInput = [ [int(octos) for octos in line.strip()] for line in inputs]

minLeft = 0
maxRight = len(cleanInput[0]) - 1
minUp = 0
maxDown = len(cleanInput) - 1
alreadyFlashed = []
totalFlashes = 0
runCounter = 0

while (True):
    for y, line in enumerate(cleanInput):
        for x, element in enumerate(line):

            if ((x, y) in alreadyFlashed):
                continue
            cleanInput[y][x] += 1
            if (cleanInput[y][x] > 9):
                recursive(cleanInput, x, y, minLeft, maxRight, minUp, maxDown, alreadyFlashed)

    if (len(alreadyFlashed) == 100):
        print(runCounter + 1)
        break

    runCounter += 1
    alreadyFlashed = []

print(flashCount)