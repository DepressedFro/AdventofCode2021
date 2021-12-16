#correct answer: 3369
#refactor goal: redo input formatter to handle start or end being on either side of dash
def recursive(graph, start, end, path=[], smallVisited=[]):
    path = path + [start]

    if (start == end):
        return [path]

    if (start not in graph):
        return []

    if (start.islower() and start != 'end' and start != 'start'):
        smallVisited.append(start)

    paths = []

    for node in graph[start]:
        if (len(path) < len(smallVisited) or all([x in path for x in smallVisited]) == False ):
            smallVisited = [x for x in smallVisited if x in path]

        if node not in smallVisited:
            newpaths = recursive(graph, node, end, path, smallVisited)
            for newpath in newpaths:
                paths.append(newpath)

    return paths

with open("day12TestInput2.txt", "r") as inputs:
    cleanInput = [ [path for path in line.strip().split('-')] for line in inputs]

pathDict = {}

#create dict
for line in cleanInput:
    pathDict.setdefault(line[0], []).append(line[1])
    #plot the reverse course too
    if (line[0] != 'start' and line[1] != 'end'):
        pathDict.setdefault(line[1], []).append(line[0])

allPaths = recursive(pathDict, 'start', 'end')
print(len(allPaths))