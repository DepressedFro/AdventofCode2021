#correct answer: 85883
#refactor goal: make it handle start/end being in either column
with open("day12Input.txt", "r") as inputs:
    cleanInput = [ [path for path in line.strip().split('-')] for line in inputs]

pathDict = {}

#create dict
for line in cleanInput:
    pathDict.setdefault(line[0], []).append(line[1])
    #plot the reverse course too
    if (line[0] != 'start' and line[1] != 'end'):
        pathDict.setdefault(line[1], []).append(line[0])

bfsQueue = []
#second element stores the dupe
bfsQueue.append([['start'], ''])
paths = []

#breadth first search approach
while (bfsQueue):
    #pops the last item
    currentNodes, dupe = bfsQueue.pop()

    #look at the last node in the current path
    #then go through each node that one connects to
    for node in pathDict[currentNodes[-1]]:
        if (node == 'end'):
            paths.append(currentNodes + [node])
        #if a small node isn't in our current path then we can add it to the path
        #or if it's a large node we can add it anyway
        elif node not in currentNodes or node.isupper():
            bfsQueue.append([currentNodes + [node], dupe])
        #if we haven't encounted a small node dupe
        #then we can go to a small node again
        elif dupe == '':
            bfsQueue.append([currentNodes + [node], node])

#print(paths)
print(len(paths))