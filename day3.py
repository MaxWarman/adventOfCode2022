"""
Author: github.com/MaxWarman
Advent of Code 2022 - Day 3
"""

def getInputLines(inputPath):
    f = open(inputPath, "rt")
    inputLines = f.readlines()
    f.close()

    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].replace("\n", "")

    return inputLines

def solvePartOne(inputLines):
    rucksacks = []
    for line in inputLines:
        rucksack = [line[:len(line)//2], line[len(line)//2:]]
        rucksacks.append(rucksack)
    
    priority = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    sumOfPriorites = 0

    for rucksack in rucksacks:
        compartment1 = rucksack[0]
        compartment2 = rucksack[1]
        foundCommon = False
        
        for item1 in compartment1:
            for item2 in compartment2:
                if item1 == item2:
                    sumOfPriorites += priority.index(item1) + 1
                    foundCommon = True
                    break
            if foundCommon:
                break
        
    solution = sumOfPriorites
    print(f"Day 3, part 1 solution: {solution}")

def solvePartTwo(inputLines):
    groups = []
    for i in range(0, len(inputLines), 3):
        group = []
        for j in range(3):
            group.append(inputLines[i+j])
        groups.append(group)

    priority = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    sumOfPriorites = 0

    for group in groups:
        rucksack1 = group[0]
        rucksack2 = group[1]
        rucksack3 = group[2]

        foundCommon = False
        commonItem = ""
        for item1 in rucksack1:
            for item2 in rucksack2:
                if item1 == item2:
                    commonItem = item1
                    break

            for item3 in rucksack3:
                if commonItem == item3:
                    foundCommon = True
                    sumOfPriorites += priority.index(commonItem) + 1
                    break
            if foundCommon:
                break

    solution = sumOfPriorites
    print(f"Day 3, part 2 solution: {solution}")

def main():
    inputPath = "day3_input.txt"

    inputLines = getInputLines(inputPath)

    solvePartOne(inputLines)
    solvePartTwo(inputLines) 


if __name__ == "__main__":
    main()