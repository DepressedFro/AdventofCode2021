#correct answer: 1728611055389
with open("day06Input.txt", "r") as inputs:
    cleanInput = [int(fish) for fish in inputs.readline().strip().split(',')]

daysToLoop = 256
maxAge = 9
#only keep track of how many in each age group
fishBuckets = [[x, 0] for x in range(maxAge)]
fishToSubtract = 0
totalFish = 0

for ageGroup in fishBuckets:
    for fish in cleanInput:
        if (ageGroup[0] == fish):
            fishBuckets[ageGroup[0]][1] += 1

for x in range(daysToLoop):
    for fish in fishBuckets:
        if (fish[1] != 0):
            #handle 0 age spawn
            if (fish[0] - 1 < 0):
                fishToSubtract = fish[1]
                fish[1] -= fish[1]
            else:
                fishBuckets[fish[0] - 1][1] = fish[1]
                fishBuckets[fish[0]][1] -= fish[1]
    if (fishToSubtract > 0):
        fishBuckets[8][1] += fishToSubtract
        fishBuckets[6][1] += fishToSubtract
        fishToSubtract = 0

for fish in fishBuckets:
    totalFish += fish[1]

print(totalFish)