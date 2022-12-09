"""
Author: github.com/MaxWarman
Advent of Code 2022 - Day 2
"""

def getInputLines(inputPath):
    f = open(inputPath, "rt")
    inputLines = f.readlines()
    f.close()

    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].replace("\n", "")

    return inputLines

def getMatchScore(enemyPick, myPick):

    matchScore = 0
    shapePointsDict = {
            "X":1,
            "Y":2,
            "Z":3
        }
    standingsDict = {
            "A":[("X", 3), ("Y", 6), ("Z", 0)],
            "B":[("X", 0), ("Y", 3), ("Z", 6)],
            "C":[("X", 6), ("Y", 0), ("Z", 3)]
        }
    
    matchScore += shapePointsDict[myPick]

    for standing in standingsDict[enemyPick]:
        if standing[0] == myPick:
            matchScore += standing[1]

    return matchScore

def getExpectedShape(enemyPick, expectedResult):
    # X - lose, Y - draw, Z - win
    resultsDict = {
            "A":[("X", "Z"), ("Y", "X"), ("Z", "Y")],
            "B":[("X", "X"), ("Y", "Y"), ("Z", "Z")],
            "C":[("X", "Y"), ("Y", "Z"), ("Z", "X")]
        }

    for result in resultsDict[enemyPick]:
        if result[0] == expectedResult:
            return result[1]


def solvePartOne(inputLines):
    
    score = 0
    for match in inputLines:
        match = match.split(" ")
        score += getMatchScore(match[0], match[1])

    solution = score
    print(f"Day 2, part 1 solution: {solution}")

def solvePartTwo(inputLines):
    
    score = 0
    for match in inputLines:
        match = match.split(" ")
        myPick = getExpectedShape(match[0], match[1])
        score += getMatchScore(match[0], myPick)
    
    solution = score
    print(f"Day 2, part 2 solution: {solution}")

def main():
    inputPath = "day2_input.txt"

    inputLines = getInputLines(inputPath)

    solvePartOne(inputLines)
    solvePartTwo(inputLines) 


if __name__ == "__main__":
    main()