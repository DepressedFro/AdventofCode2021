#correct answer 1477
#read file in
inputs = open("day1Input.txt", "r")
oldValue = inputs.readline()
biggerCounter = 0

#loop through the file and compare the next value to the old value
for currentNumber in inputs:
    newValue = currentNumber

    if (int(newValue) > int(oldValue)):
        biggerCounter += 1

    oldValue = newValue

print(biggerCounter)


