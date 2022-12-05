"""
Author: github.com/MaxWarman
Advent of Code 2022 - Day 5
"""

def getInputLines(inputPath):
    f = open(inputPath, "rt")
    inputLines = f.readlines()
    f.close()

    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].replace("\n", "")

    return inputLines

def getInputParameters(inputLines):
    stacks = []
    rearrangementProcedures = []
    readInitialState = False
    for line in inputLines:

        if line == "":
            readInitialState = True
            continue

        if readInitialState == False:
            i = 0
            stackRow = []
            while i < len(line):
                stackRow.append(line[i:i+3])
                if i + 4 >= len(line):
                    break
                i += 4
            stacks.append(stackRow)

        else:
            line = line.split(" ")
            procedure = [int(line[1]), int(line[3])-1, int(line[5])-1]
            rearrangementProcedures.append(procedure)

    # Remove stack numeration row
    stacks = stacks[:-1]
    # Reverse list to have the lowest row on index '0'
    stacks = stacks[::-1]

    return stacks, rearrangementProcedures

def expandStacks(stacks):
    stacks.append(["   " for i in range(len(stacks[0]))])
    return stacks

def moveCrates(stacks, moveFrom, moveTo, howMany=1):

    cratesToMove = []

    reversedStacks = stacks[::-1]

    startPicking = False
    for i in range(len(reversedStacks)):
        if reversedStacks[i][moveFrom] != "   ":
            startPicking = True
        
        if startPicking == True:
            if howMany == 1:
                cratesToMove.append(reversedStacks[i][moveFrom])
                reversedStacks[i][moveFrom] = "   "
            else:
                for j in range(i, i+howMany):
                    cratesToMove.append(reversedStacks[j][moveFrom])
                    reversedStacks[j][moveFrom] = "   "

            break
    
    cratesToMove = cratesToMove[::-1]

    emptyFieldsCount = 0
    for i in range(len(reversedStacks)):
        if reversedStacks[i][moveTo] == "   ":
            emptyFieldsCount += 1
        else:
            break

    stacks = reversedStacks[::-1]

    if emptyFieldsCount < howMany:
        for i in range(howMany - emptyFieldsCount):
            stacks = expandStacks(stacks)

    for i, stackRow in enumerate(stacks):
        if stackRow[moveTo] == "   ":
            stacks[i][moveTo] = cratesToMove[0]
            cratesToMove.pop(0)

        if len(cratesToMove) == 0:
            break

    lastRowEmpty = True
    while lastRowEmpty == True:
        for i in range(len(stacks[-1])):
            if stacks[-1][i] != "   ":
                lastRowEmpty = False
                break
        if lastRowEmpty == True:
            stacks.pop(-1)

    return stacks

def printStacks(stacks):
    for stackRow in stacks[::-1]:
        print(stackRow)

def solvePartOne(inputLines):

    stacks, rearrangementProcedures = getInputParameters(inputLines)

    printStacks(stacks)

    for procedure in rearrangementProcedures:
        howMany = procedure[0]
        moveFrom = procedure[1]
        moveTo = procedure[2]

        for i in range(howMany):
            stacks = moveCrates(stacks, moveFrom, moveTo)

    print("#" * 15)
    printStacks(stacks)

    cratesOnTop = ""
    for i in range(len(stacks[0])):
        for stackRow in stacks[::-1]:
            if stackRow[i] != "   ":
                cratesOnTop += stackRow[i][1]
                break

    solution = cratesOnTop
    print(f"Day 5, part 1 solution: {solution}")

def solvePartTwo(inputLines):
    
    stacks, rearrangementProcedures = getInputParameters(inputLines)
    
    printStacks(stacks)

    for procedure in rearrangementProcedures:
        howMany = procedure[0]
        moveFrom = procedure[1]
        moveTo = procedure[2]

        stacks = moveCrates(stacks, moveFrom, moveTo, howMany)

    print("#" * 15)
    printStacks(stacks)

    cratesOnTop = ""
    for i in range(len(stacks[0])):
        for stackRow in stacks[::-1]:
            if stackRow[i] != "   ":
                cratesOnTop += stackRow[i][1]
                break

    solution = cratesOnTop
    print(f"Day 5, part 2 solution: {solution}")

def main():
    inptuPath = "day5_input.txt"

    inputLines = getInputLines(inptuPath)

    solvePartOne(inputLines)
    solvePartTwo(inputLines) 


if __name__ == "__main__":
    main()