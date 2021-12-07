#correct answer: 90040997
with open("day07Input.txt", "r") as inputs:
    cleanInput = [int(crabs) for crabs in inputs.readline().strip().split(',')]

maxInput = max(cleanInput)
minInput = min(cleanInput)
averageInput = int((maxInput + minInput ) / 2 )
numOfLower = 0
numOfHigher = 0
totalFuelArray = []
startPosition = 0
endPosition = 0
currentFuelTotal = 0
sumOfFuel = 0

for crab in cleanInput:
    if (crab >= averageInput):
        numOfHigher += 1
    else:
        numOfLower += 1

if (numOfHigher > numOfLower):
    startPosition = averageInput
    endPosition = maxInput + 1
elif (numOfHigher < numOfLower):
    startPosition = minInput
    endPosition = averageInput + 1
else:
    startPosition = minInput
    endPosition = maxInput + 1

for x in range(startPosition, endPosition):
    currentFuelTotal = 0
    sumOfFuel = 0
    for crabs in cleanInput:
        sumOfFuel = sum(range(abs(crabs - x) + 1))
        currentFuelTotal += sumOfFuel

    totalFuelArray.append([x, currentFuelTotal])

print(min(totalFuelArray, key=lambda y: y[1])[1])