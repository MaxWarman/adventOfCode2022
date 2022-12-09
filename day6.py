"""
Author: github.com/MaxWarman
Advent of Code 2022 - Day 6
"""

def getInputLines(inputPath):
    f = open(inputPath, "rt")
    inputLines = f.readlines()
    f.close()

    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].replace("\n", "")

    return inputLines

def getStartMarker(line, howManyUnique):
    
    startMarker = 0
    stream = list(line)
    received = []

    for i, value in enumerate(stream):

        received.append(value)

        if len(received) < howManyUnique:
            continue

        uniqueInLastValues = 0
        for j in range(howManyUnique):
            lastValues = received[i - howManyUnique + 1:]
            charToCheck = lastValues[j]
            lastValues.pop(j)
            if charToCheck not in lastValues:
                uniqueInLastValues += 1
        
        if uniqueInLastValues == howManyUnique:
            startMarker = i + 1
            break

    return startMarker

def solvePartOne(inputLines):
    
    startOfPacketMarker = 0
    for line in inputLines:
        startOfPacketMarker = getStartMarker(line, 4)

    solution = startOfPacketMarker
    print(f"Day 6, part 1 solution: {solution}")

def solvePartTwo(inputLines):
    
    startOfPacketMarker = 0
    for line in inputLines:
        startOfMessageMarker = getStartMarker(line, 14)
    
    solution = startOfMessageMarker
    print(f"Day 6, part 2 solution: {solution}")

def main():
    inptuPath = "day6_input.txt"

    inputLines = getInputLines(inptuPath)

    solvePartOne(inputLines)
    solvePartTwo(inputLines) 


if __name__ == "__main__":
    main()