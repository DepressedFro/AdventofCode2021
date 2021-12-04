#correct answer: 3242606
with open("day03Input.txt", "r") as inputs:
    cleanInput = [binary.strip() for binary in inputs]

zeroCount = 0
oneCount = 0
gamma = ''
epsilon = ''

flippedBinaries = []
inputLength = len(cleanInput[0])
counter = 0

for increment in range(inputLength):
    flippedBinaries.append([])

for binary in cleanInput:
    for x in binary:
        flippedBinaries[counter] += x
        counter += 1
    counter = 0

for sequence in flippedBinaries:
    zeroCount = sequence.count('0')
    oneCount = sequence.count('1')

    if (zeroCount > oneCount):
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print(int(gamma, 2) * int(epsilon, 2))

