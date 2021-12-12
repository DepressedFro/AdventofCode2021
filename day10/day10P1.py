#use a stack
#push left operands in
#pop on right operand
#check if right operand matches left
#if not it's corrupted
#correct answer: 299793
with open("day10Input.txt", "r") as inputs:
    cleanInput = [ [chars for chars in line.strip()] for line in inputs]

stack = []
poppedItem = ''
badChars = []
points = 0

for line in cleanInput:
    for char in line:
        if (char == '(' or char == '[' or char == '{' or char == '<'):
            stack.append(char)
        else:
            poppedItem = stack.pop()
            if (poppedItem == '('):
                if (char != ')'):
                    badChars.append(char)
            elif (poppedItem == '['):
                if (char != ']'):
                    badChars.append(char)
            elif (poppedItem == '{'):
                if (char != '}'):
                    badChars.append(char)
            elif (poppedItem == '<'):
                if (char != '>'):
                    badChars.append(char)
    poppedItem = ''
    stack = []

for char in badChars:
    if (char == ')'):
        points += 3
    elif (char == ']'):
        points += 57
    elif (char == '}'):
        points += 1197
    elif (char == '>'):
        points += 25137

print(points)