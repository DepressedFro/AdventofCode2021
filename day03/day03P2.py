#correct answer: 4856080
with open("day03Input.txt", "r") as inputs:
    cleanInput = [binary.strip() for binary in inputs]

trimInputOxyScrubber = cleanInput
trimInputCOGenerator = cleanInput
tempList = []
zeroCount = 0
oneCount = 0
currentBitCounter = 0
currentBitToKeep = ''

#this is for oxygen scrubber
#loop until there's only one element
while (len(trimInputOxyScrubber) != 1):
    #count the bits in the current position
    for x in trimInputOxyScrubber:
        if (int(x[currentBitCounter]) == 0):
            zeroCount += 1
        else:
            oneCount += 1

    #determine which bit to trim
    if (zeroCount > oneCount):
        currentBitToKeep = 0
    else:
        currentBitToKeep = 1

    for y in trimInputOxyScrubber:
        if (int(y[currentBitCounter]) == currentBitToKeep):
            tempList.append(y)

    trimInputOxyScrubber = tempList
    tempList = []
    currentBitToKeep = ''
    currentBitCounter += 1
    zeroCount = 0
    oneCount = 0

currentBitCounter = 0

#this is for C02 Generator
#loop until there's only one element
while (len(trimInputCOGenerator) != 1):
    # count the bits in the current position
    for x in trimInputCOGenerator:
        if (int(x[currentBitCounter]) == 0):
            zeroCount += 1
        else:
            oneCount += 1

    # determine which bit to keep
    if (zeroCount <= oneCount):
        currentBitToKeep = 0
    else:
        currentBitToKeep = 1

    for y in trimInputCOGenerator:
        if (int(y[currentBitCounter]) == currentBitToKeep):
            tempList.append(y)

    trimInputCOGenerator = tempList
    tempList = []
    currentBitToKeep = ''
    currentBitCounter += 1
    zeroCount = 0
    oneCount = 0

print(int(trimInputOxyScrubber[0], 2) * int(trimInputCOGenerator[0], 2))