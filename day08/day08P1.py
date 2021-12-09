#correct answer: 255
with open("day08Input.txt", "r") as inputs:
    cleanInput = [ [[nums] for nums in line.strip().split(' | ')] for line in inputs]

digitCounter = 0
#this is the simplest solution
for line in cleanInput:
    for output in line[1]:
        for segment in output.split(' '):
            if (len(segment) == 2 or len(segment) == 3 or len(segment) == 4 or len(segment) ==7):
                digitCounter += 1

print(digitCounter)