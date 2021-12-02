#correct answer: 1320534480
with open("day02Input.txt", "r") as inputs:
    cleanInput = [direction.strip() for direction in inputs]

adjustedInput = []
horizontal = 0
depth = 0
aim = 0

for direction in cleanInput:
    temp = direction.split()
    adjustedInput.append((temp[0], int(temp[1])))

for input in adjustedInput:
    if (input[0] == "forward"):
        horizontal += input[1]
        depth += aim * input[1]
    elif (input[0] == "up"):
        aim -= input[1]
    elif (input[0] == "down"):
        aim += input[1]

print(depth * horizontal)