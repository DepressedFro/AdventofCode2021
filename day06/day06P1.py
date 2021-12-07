#correct answer: 385391
with open("day06Input.txt", "r") as inputs:
    cleanInput = [int(fish) for fish in inputs.readline().strip().split(',')]

daysToLoop = 80
fishToAdd = []

for x in range(daysToLoop):
    for counter, fish in enumerate(cleanInput):
        if (fish - 1 < 0):
            cleanInput[counter] = 6
            fishToAdd.append(8)
        else:
            cleanInput[counter] = fish - 1

    if (len(fishToAdd) != 0):
        cleanInput += fishToAdd
        fishToAdd = []

print(len(cleanInput))