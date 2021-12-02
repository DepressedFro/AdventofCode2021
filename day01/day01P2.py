#correct answer 1523
#read file
#sanitize inputs
with open("day01Input.txt", "r") as inputs:
    cleanInputOne = [int(number.strip()) for number in inputs]

biggerCounter = 0
#create our two sliding windows
cleanInputTwo = cleanInputOne[1:]
valueOne = cleanInputOne.pop(0)
valueTwo = cleanInputOne.pop(0)
valueFour = cleanInputTwo.pop(0)
valueFive = cleanInputTwo.pop(0)

readLength = len(cleanInputOne)

for currentNumber in range(readLength):
    if (currentNumber >= readLength - 1):
        break
    valueThree = cleanInputOne.pop(0)
    valueSix = cleanInputTwo.pop(0)
    sumOne = valueOne + valueTwo + valueThree
    sumTwo = valueFour + valueFive + valueSix

    if sumTwo > sumOne:
        biggerCounter += 1

    #update our values
    valueOne = valueTwo
    valueTwo = valueThree

    valueFour = valueFive
    valueFive = valueSix

print(biggerCounter)