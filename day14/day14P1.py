#correct answer: 3831
with open("day14Input.txt", "r") as inputs:
    initialString = inputs.readline().strip()
    inputs.readline()
    cleanInput = [ [path for path in line.strip().split(' -> ')] for line in inputs]

updateString = ''
charToInsert = ''
numOfSteps = 10

for step in range(numOfSteps):
    updateString = ''
    numOfPairs = len(initialString) - 1

    for x in range (numOfPairs):
        charToInsert = next(index for index, value in enumerate(cleanInput) if initialString[x: x + 2] in value[0])
        charToInsert = cleanInput[charToInsert][1]
        updateString += (initialString[x: x + 1] + charToInsert)

    updateString += initialString[len(initialString) - 1]
    initialString = updateString

charDict = {}
#build a dictionary to find most/least common
for s in initialString:
    if s in charDict:
        charDict[s] += 1
    else:
        charDict[s] = 1

print(charDict)
mostCommon = max(charDict, key = charDict.get)
leastCommon = min(charDict, key = charDict.get)
print(charDict[mostCommon] - charDict[leastCommon])