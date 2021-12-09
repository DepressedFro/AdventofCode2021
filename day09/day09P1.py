#correct answer: 564
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
            lowPoints.append(int(height) + 1)

        currentNeighbors = []

#subtract 1 for actual low points
print(lowPoints)
print(sum(lowPoints))