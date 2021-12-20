#correct answer: 5725739914282
#grouping is the correct solution for part 2
with open("day14Input.txt", "r") as inputs:
    initialString = inputs.readline().strip()
    inputs.readline()
    cleanInput = [ [path for path in line.strip().split(' -> ')] for line in inputs]

charToInsert = ''
numOfSteps = 40
numOfPairs = len(initialString) - 1
pairDict = {}
for pair in cleanInput:
    pairDict[pair[0]] = 0

#setup initial pairs
for x in range(numOfPairs):
    pairDict[initialString[x: x + 2]] += 1

blankDict = {x:0 for x in pairDict}

for step in range(numOfSteps):
    tempDict = blankDict.copy()

    for key, value in pairDict.items():
        charToInsert = next(index for index, value in enumerate(cleanInput) if key in value[0])
        charToInsert = cleanInput[charToInsert][1]
        tempDict[key[0] + charToInsert] += value
        tempDict[charToInsert + key[1]] += value
        #make sure to subtract the value from the actual dict
        pairDict[key] -= value

    for key, value in pairDict.items():
        pairDict[key] += tempDict[key]

charDict = {}
#build a dictionary to find most/least common
for key, value in pairDict.items():
    if key[0] in charDict:
        charDict[key[0]] += value
    else:
        charDict[key[0]] = value
#account for the last letter on our initial string
charDict[initialString[-1]] += 1

print(charDict)
mostCommon = max(charDict, key = charDict.get)
leastCommon = min(charDict, key = charDict.get)
print(charDict[mostCommon] - charDict[leastCommon])
