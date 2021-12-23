#correct answer: 2901
#refactor goal: slow, find ways to speed up
with open("day15Input.txt", "r") as inputs:
    cleanInput = [ [int(risk) for risk in line.strip()] for line in inputs]

rows = len(cleanInput)
cols = len(cleanInput[0])
repeatAmount = 5
bigGrid = [[cleanInput[y][x] if x in range(cols) and y in range(rows) else 0 for x in range (5 * cols) ] for y in range(rows * 5) ]

#can cut this down
for iterationY in range(0, repeatAmount):
    if (iterationY == 0):
        pass
    else:
        #handle y expansion
        for y in range(rows):
            setY = y + (iterationY * rows)
            for x in range(cols):
                bigGrid[setY][x] = bigGrid[y][x] + iterationY
                if (bigGrid[setY][x] > 9):
                    bigGrid[setY][x] = bigGrid[setY][x] % 9
    for iterationX in range(1, repeatAmount):
        #handle x expansion
        for y in range(rows):
            setY = y + (iterationY * rows)
            for x in range(cols):
                setX = x + (iterationX * cols)
                bigGrid[setY][setX] = bigGrid[setY][x] + iterationX
                if (bigGrid[setY][setX] > 9):
                    bigGrid[setY][setX] = bigGrid[setY][setX] % 9


risk = 0
#risk, vertices
queue = [(0, (0, 0))]
visited = set()
rows = len(bigGrid)
cols = len(bigGrid[0])
goal = (rows - 1, cols - 1)
lowestRisk = {(0,0): 0}

while queue:
    risk, vertices = queue.pop(0)
    x = vertices[0]
    y = vertices[1]

    if ((x, y) == goal):
        break

    for nextX, nextY in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if (nextX, nextY) in visited or nextX < 0 or nextX > cols - 1 or nextY < 0 or nextY > rows - 1:
            continue
        nextRisk = risk + bigGrid[nextY][nextX]

        if (nextX, nextY) not in lowestRisk or lowestRisk[(x, y)] > nextRisk:
            lowestRisk[(nextX, nextY)] = nextRisk
            queue.append((nextRisk, (nextX, nextY)))

    visited.add((nextX, nextY))
    #sort to increase speed
    queue.sort()

print(risk)