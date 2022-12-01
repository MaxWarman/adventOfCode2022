"""
Author: github.com/MaxWarman
Advent of Code 2022 - Day 1
"""

def getInputLines(inputPath):
    f = open(inputPath, "rt")
    inputLines = f.readlines()
    f.close()

    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].replace("\n", "")

    return inputLines

def getElvesInventory(inputLines):
    elvesInventory = []
    inventory = []
    for line in inputLines:
        if line == "":
            elvesInventory.append(inventory)
            inventory = []
        else:
            inventory.append(int(line))

    return elvesInventory

def solvePartOne(inputLines):
    elvesInventory = getElvesInventory(inputLines)
    totalCalories = [sum(inventory) for inventory in elvesInventory]
    solution = max(totalCalories)
    
    print(f"Day 1, part 1 solution: {solution}")

def solvePartTwo(inputLines):
    elvesInventory = getElvesInventory(inputLines)
    totalCalories = [sum(inventory) for inventory in elvesInventory]

    top3calories = []
    for calories in totalCalories:
        if len(top3calories) < 3:
            top3calories.append(calories)
            continue

        if calories > min(top3calories):
            indexToSwap = top3calories.index(min(top3calories))
            top3calories[indexToSwap] = calories

    solution = sum(top3calories)
    print(f"Day 1, part 2 solution: {solution}")

def main():
    inputPath = "day1_input.txt"

    inputLines = getInputLines(inputPath)

    solvePartOne(inputLines)
    solvePartTwo(inputLines)    

if __name__ == "__main__":
    main()