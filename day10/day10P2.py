#correct answer: 3654963618
#refactor goal: more list comprehension
with open("day10Input.txt", "r") as inputs:
    cleanInput = [ [chars for chars in line.strip()] for line in inputs]

stack = []
poppedItem = ''
incompLines = []
points = 0
badChar = False
charsToAdd = ''
addedChars = []
pointLines = []

#go through lines and grab incomplete lines
for line in cleanInput:
    poppedItem = ''
    stack = []
    badChar = False

    for char in line:
        if (char == '(' or char == '[' or char == '{' or char == '<'):
            stack.append(char)
        else:
            poppedItem = stack.pop()
            if (poppedItem == '('):
                if (char != ')'):
                    badChar = True
                    break
            elif (poppedItem == '['):
                if (char != ']'):
                    badChar = True
                    break
            elif (poppedItem == '{'):
                if (char != '}'):
                    badChar = True
                    break
            elif (poppedItem == '<'):
                if (char != '>'):
                    badChar = True
                    break
    if (badChar == True):
        continue
    else:
        incompLines.append(line)

#go through incomplete lines and get the characters which have no matching closing char
for line in incompLines:
    poppedItem = ''
    stack = []

    for char in line:
        if (char == '(' or char == '[' or char == '{' or char == '<'):
            stack.append(char)
        else:
            poppedItem = stack.pop()

    addedChars.append(list(reversed(stack)))

#go through each line and add up for total score
for line in addedChars:
    for char in line:
        if (char == '('):
            points = points * 5 + 1
        elif (char == '['):
            points = points * 5 + 2
        elif (char == '{'):
            points = points * 5 + 3
        elif (char == '<'):
            points = points * 5 + 4
    pointLines.append(points)
    points = 0

print(sorted(pointLines)[int(len(pointLines) / 2)] )