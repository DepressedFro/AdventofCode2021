#correct answer: 498
with open("day15Input.txt", "r") as inputs:
    cleanInput = [ [int(risk) for risk in line.strip()] for line in inputs]

rows = len(cleanInput)
cols = len(cleanInput[0])
risk = 0
#format: (risk, (vertices) )
queue = [(0, (0, 0))]
visited = []
goal = (rows - 1, cols - 1)
lowestRisk = {(0,0): 0}

while queue:
    risk, vertices = queue.pop(0)
    x = vertices[0]
    y = vertices[1]

    #if we're deciding which direction to go at the goal node, stop
    if ((x, y) == goal):
        break

    #explore up, down, left, right from where we are
    for nextX, nextY in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        #if we already visited that node or we're out of bounds skip these coordinates
        if (nextX, nextY) in visited or nextX < 0 or nextX > cols - 1 or nextY < 0 or nextY > rows - 1:
            continue
        nextRisk = risk + cleanInput[nextY][nextX]
        #if there's no entry in our dicitonary for these coordinates
        #or we our current risk is lower than the one stored
        #then we update the lowest risk and add this path to the queue
        if (nextX, nextY) not in lowestRisk or lowestRisk[(x, y)] > nextRisk:
            lowestRisk[(nextX, nextY)] = nextRisk
            queue.append((nextRisk, (nextX, nextY)))

    visited.append((nextX, nextY))
    # sort to increase speed
    queue.sort()

print(risk)