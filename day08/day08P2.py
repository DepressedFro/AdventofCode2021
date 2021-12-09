#correct answer: 982158
with open("day08Input.txt", "r") as inputs:
    cleanInput = [ [[nums] for nums in line.strip().split(' | ')] for line in inputs]

digitLengths = [2, 5, 5, 4, 5, 6, 3, 7]
digitMaps = [0 for x in range(10)]
outputString = ''
outputAmount = 0

for line in cleanInput:
    for input in line[0]:
        for segment in input.split(' '):
            if (len(segment) == 2):
                digitMaps[1] = segment
            elif(len(segment) == 4):
                digitMaps[4] = segment
            elif (len(segment) == 3):
                digitMaps[7] = segment
            elif (len(segment) == 7):
                digitMaps[8] = segment

        #after we find basics then we loop again
        for segment in input.split(' '):
            #5's group segment (2, 3, 5)
            if (len(segment) == 5):
                #in the 5's group only 3 contains all parts of 1
                if (all([s in segment for s in digitMaps[1]])):
                    digitMaps[3] = segment
                #in the 5's group only 5 contains exactly 3 parts of 4
                elif ([s in segment for s in digitMaps[4]].count(True) == 3):
                    digitMaps[5] = segment
                # else it must be 2
                else:
                    digitMaps[2] = segment
            #6's group segment (0, 6, 9)
            elif (len(segment) == 6):
                # in the 6's group only 9 contains all parts of 4
                if (all([s in segment for s in digitMaps[4]])):
                    digitMaps[9] = segment
                # in the 6's group only 0 contains all of 7
                elif (all([s in segment for s in digitMaps[7]])):
                    digitMaps[0] = segment
                #else it must be 0
                else:
                    digitMaps[6] = segment

    #go through each output line and transform them into ints
    for output in line[1]:
        for segment in output.split(' '):
            for count, number in enumerate(digitMaps):
                if (len(number) == len(segment) and all([s in segment for s in number])):
                    outputString += str(count)
        outputAmount += int(outputString)
        outputString = ''

print(outputAmount)