"""
Author: github.com/MaxWarman
Advent of Code 2022 - Day 4
"""

def getInputLines(inputPath):
    f = open(inputPath, "rt")
    inputLines = f.readlines()
    f.close()

    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].replace("\n", "")

    return inputLines

def getPairsOfElves(inputLines):
    pairs = []
    for line in inputLines:
        line = line.split(",")
        elf1Positions = line[0].split("-")
        elf2Positions = line[1].split("-")
        
        for i in range(len(elf1Positions)):
            elf1Positions[i] = int(elf1Positions[i])
            
        for i in range(len(elf2Positions)):
            elf2Positions[i] = int(elf2Positions[i])

        pairs.append([elf1Positions, elf2Positions])

    return pairs

def solvePartOne(inputLines):
    pairs = getPairsOfElves(inputLines)

    sumOfFullyOverlapping = 0
    for pair in pairs:
        elf1 = pair[0]
        elf2 = pair[1]

        if (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]) or (elf2[0] >= elf1[0] and elf2[1] <= elf1[1]):
            sumOfFullyOverlapping += 1

    solution = sumOfFullyOverlapping
    print(f"Day 4, part 1 solution: {solution}")

def solvePartTwo(inputLines):
    pairs = getPairsOfElves(inputLines)

    sumOfPartlyOverlapping = 0
    for pair in pairs:
        elf1 = pair[0]
        elf2 = pair[1]

        if  (elf2[0] <= elf1[0] <= elf2[1] or elf2[0] <= elf1[1] <= elf2[1]) or (elf1[0] <= elf2[0] <= elf1[1] or elf1[0] <= elf2[1] <= elf1[1]):
            sumOfPartlyOverlapping += 1
    
    solution = sumOfPartlyOverlapping
    print(f"Day 4, part 2 solution: {solution}")

def main():
    inptuPath = "day4_input.txt"

    inputLines = getInputLines(inptuPath)


    solvePartOne(inputLines)
    solvePartTwo(inputLines) 


if __name__ == "__main__":
    main()