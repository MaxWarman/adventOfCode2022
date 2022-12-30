"""
Author: github.com/MaxWarman
Advent of Code 2022 - Day 8
"""

def getInputLines(inputPath):
    f = open(inputPath, "rt")
    inputLines = f.readlines()
    f.close()

    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].replace("\n", "")

    return inputLines

def getGrid(inputLines):
    grid = []
    for row in inputLines:
        tmp = []
        for char in row:
            tmp.append(int(char))
        grid.append(tmp)

    return grid

def solvePartOne(inputLines):
    grid = getGrid(inputLines)

    visibleTrees = []
    
    # Horizontal
    for i, row in enumerate(grid):
        
        # West to East
        highest = -1
        for j in range(len(row)):
            if row[j] > highest:
                highest = row[j]
                if (i, j) not in visibleTrees:
                    visibleTrees.append((i,j))

        # East to West
        highest = -1
        for j in range(len(row)-1, -1, -1):
            if row[j] > highest:
                highest = row[j]
                if (i, j) not in visibleTrees:
                    visibleTrees.append((i,j))
    
    # Vertical
    for i in range(len(grid[0])):
        
        column = []
        for j in range(len(grid)):
            column.append(grid[j][i])

        # North to South
        highest = -1
        for j in range(len(column)):
            if column[j] > highest:
                highest = column[j]
                if (j,i) not in visibleTrees:
                    visibleTrees.append((j, i))

        # South to North
        highest = -1
        for j in range(len(column)-1, -1, -1):
            if column[j] > highest:
                highest = column[j]
                if (j,i) not in visibleTrees:
                    visibleTrees.append((j, i))
    
    solution = len(visibleTrees)
    print(f"Day 8, part 1 solution: {solution}")

def getScenicScore(grid, rowIndex, colIndex):
        
    row = grid[rowIndex]
    col = []
    for i in range(len(grid)):
        col.append(grid[i][colIndex])

    if  colIndex == 0 or colIndex == len(row) - 1 or rowIndex == 0 or rowIndex == len(col) - 1:
        return 0

    currentTreeHeight = grid[rowIndex][colIndex]
    scores = []

    # Tree to East    
    score = 0
    for i in range(colIndex + 1, len(row)):
        score += 1
        if row[i] >= currentTreeHeight:
            break
    scores.append(score)
    
    # Tree to West
    score = 0
    for i in range(colIndex - 1, -1, -1):
        score += 1
        if row[i] >= currentTreeHeight:
            break
    scores.append(score)
    
    # Tree to South
    score = 0
    for i in range(rowIndex + 1, len(col)):
        score += 1
        if col[i] >= currentTreeHeight:
            break
    scores.append(score)
    
    # Tree to North
    score = 0
    for i in range(rowIndex -1, -1, -1):
        score += 1
        if col[i] >= currentTreeHeight:
            break
    scores.append(score)

    scenicScore = 1
    for score in scores:
        scenicScore *= score

    return scenicScore


def solvePartTwo(inputLines):
    grid = getGrid(inputLines)

    bestScore = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            currentScenicScore = getScenicScore(grid, i, j)
            if currentScenicScore > bestScore:
                bestScore = currentScenicScore
    
    solution = bestScore
    print(f"Day 8, part 2 solution: {solution}")

def main():
    inputPath = "day8_input.txt"

    inputLines = getInputLines(inputPath)

    solvePartOne(inputLines)
    solvePartTwo(inputLines) 


if __name__ == "__main__":
    main()