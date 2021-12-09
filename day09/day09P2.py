#correct answer: 1038240
def recursive (grid, x, y, minLeft, maxRight, minUp, maxDown, lastValue, visited):
    if (grid[y][x]  == '9'):
        return False
    elif (int(grid[y][x]) < lastValue):
        return False
    elif ((x, y) in visited):
        return False

    visited.append((x, y))
    lastValue = int(grid[y][x])

    if ((x > minLeft and recursive(grid, x - 1, y, minLeft, maxRight, minUp, maxDown, lastValue, visited) ) or
            (x < maxRight and recursive(grid, x + 1, y, minLeft, maxRight, minUp, maxDown, lastValue, visited)) or
            (y > minUp and recursive(grid, x, y - 1, minLeft, maxRight, minUp, maxDown, lastValue, visited)) or
            (y < maxDown and recursive(grid, x, y + 1, minLeft, maxRight, minUp, maxDown, lastValue, visited))):
        pass

    return False

with open("day09Input.txt", "r") as inputs:
    cleanInput = [ [nums for nums in line.strip()] for line in inputs]

minLeft = 0
maxRight = len(cleanInput[0]) - 1
minUp = 0
maxDown = len(cleanInput) - 1
lowPoints = []
currentNeighbors = []

for yPosition, line in enumerate(cleanInput):
    for xPosition, height in enumerate(line):
        #if we're not the left most position then we can check to the left of the current height
        if (xPosition > minLeft):
            currentNeighbors.append(cleanInput[yPosition][max(xPosition - 1, minLeft)])
        #if we're not at the right most position then check to the right of it
        if (xPosition < maxRight):
            currentNeighbors.append(cleanInput[yPosition][min(xPosition + 1, maxRight)])
        #if we're not at the top most position then we can check above it
        if (yPosition > minUp):
            currentNeighbors.append(cleanInput[max(yPosition - 1, minUp)][xPosition])
        #if we're not at the bottom most position then we can check beneath it
        if (yPosition < maxDown):
            currentNeighbors.append(cleanInput[min(yPosition + 1, maxDown)][xPosition])

        if (all([x > height for x in currentNeighbors])):
            lowPoints.append([int(height), [xPosition, yPosition] ])

        currentNeighbors = []

tempList = []
basinPoints = []
#basin search
for point in lowPoints:
    recursive(cleanInput, point[1][0], point[1][1], minLeft, maxRight, minUp, maxDown, point[0], tempList)
    basinPoints.append(len(tempList))
    tempList =[]
#just need the last 3 elements after sorting
resultList = sorted(basinPoints)[len(basinPoints) - 3:]
result = resultList[0] * resultList[1] * resultList[2]
print(result)
