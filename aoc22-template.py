"""
Author: github.com/MaxWarman
Advent of Code 2022 - Day X
"""

def getInputLines(inputPath):
    f = open(inputPath, "rt")
    inputLines = f.readlines()
    f.close()

    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].replace("\n", "")

    return inputLines

def solvePartOne(inputLines):
    pass
    
    #solution = None
    #print(f"Day X, part 1 solution: {solution}")

def solvePartTwo(inputLines):
    pass
    
    #solution = None
    #print(f"Day X, part 2 solution: {solution}")

def main():
    inputPath = "dayX_input.txt"

    inputLines = getInputLines(inputPath)

    solvePartOne(inputLines)
    solvePartTwo(inputLines) 


if __name__ == "__main__":
    main()