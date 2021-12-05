#correct answer: 10478
#refactor goal: split into functions
def printBoard(boardArray, selectBoard):
    for entry in range(5):
        print(boardArray[selectBoard][entry])

with open("day04Input.txt", "r") as inputs:
    cleanInput = [binary.strip() for binary in inputs if binary.isspace() is False]

calledNumbers = cleanInput.pop(0)
calledNumbers = [int(n) for n in calledNumbers.split(',')]
bingoBoards = []
trueBoards = []
boardNumber = 0
linesRead = 0
boardLength = 5
winner = False
columnNumOfWinners = 0
boardXPos = 0
winningBoardNumber = ''
winningBoardSum = 0
winningNumber = 0

#P2
winningBoards = []
numOfWinningBoards = 0

for currentLine in cleanInput:
    if(linesRead == 0):
        bingoBoards.append([])
        trueBoards.append([])
    bingoBoards[boardNumber].append(currentLine.split())
    trueBoards[boardNumber].append(['false', 'false', 'false', 'false', 'false'])
    linesRead += 1
    if (linesRead >= 5):
        boardNumber += 1
        linesRead = 0

numOfBoards = len(bingoBoards)

#go through each called number
#on each board go through every line
#then remove the called number from that line
#then check if board is a winner
#if winner then calculate score
#if not then go to next board and repeat
for number in calledNumbers:
    for count, board in enumerate(bingoBoards):
        if (count in winningBoards):
            continue
        #check if a row has the number
        #if so mark it
        for y in range(boardLength):
            try:
                boardXPos = board[y].index(str(number))
                trueBoards[count][y][boardXPos] = 'true'
            except ValueError:
                pass

        for trueCount, callBoard in enumerate(trueBoards):
            if (trueCount in winningBoards):
                continue
            for line in callBoard:
                #check horizontal winners
                if (line.count('true') == 5):
                    winner = True
                    break
            if (winner == True):
                break
            #check vertical winners
            for x in range(boardLength):
                for y in range(boardLength):
                    if (callBoard[y][x] == 'true'):
                        columnNumOfWinners += 1
                if (columnNumOfWinners == 5):
                    winner = True
                    break

                columnNumOfWinners = 0

            columnNumOfWinners = 0
            if (winner == True):
                break
        if (winner == True):
            numOfWinningBoards += 1
            if (numOfWinningBoards < numOfBoards):
                winningBoards.append(count)
                winner = False
            else:
                winningBoardNumber = count
                winningNumber = number
                break

    if (winner == True):
        break

#calculate uncalled numbers sum
for y in range(boardLength):
    for x in range(boardLength):
        if (trueBoards[winningBoardNumber][y][x] != 'true'):
            winningBoardSum += int(bingoBoards[winningBoardNumber][y][x])

print(winningBoardSum, winningNumber, winningBoardNumber)
print("Sum: " + str(winningBoardSum * winningNumber))
printBoard(trueBoards, winningBoardNumber)
printBoard(bingoBoards, winningBoardNumber)