"""
Author: github.com/MaxWarman
Advent of Code 2022 - Day 6
"""

class Filesystem():
    
    def __init__(self):
        self.allDirectories = []
        self.currentDirectory = None

    def createDirectory(self, _dirName):
        
        newDir = Directory(_dirName, self.currentDirectory)
        self.allDirectories.append(newDir)

        if self.currentDirectory != None:
            self.currentDirectory.addDirectory(newDir)

    def createFile(self, _fileName, _fileSize, _parentDirectory):
        newFile = File(_fileName, _fileSize, _parentDirectory)
        self.currentDirectory.addFile(newFile)

    def changeDirectory(self, _dirName):
        
        if _dirName == "..":
            if self.currentDirectory != "/":
                self.currentDirectory = self.currentDirectory.getParentDir()
                
        elif _dirName == "/":
            self.currentDirectory = self.getAllDirectories()[0]

        else:
            destinationDirectory = None
            for directory in self.getCurrentDir().getDirContents():
                if directory.getName() == _dirName:
                    destinationDirectory = directory

            if destinationDirectory == None:
                print(f"Got None destDir on:\t{self.currentDirectory.getName()} -> {_dirName}")
            self.currentDirectory = destinationDirectory

    def displayDirectories(self):
        print(f"- {self.allDirectories[0].getName()} (dir) [totalSize: {self.allDirectories[0].getTotalSize()}]")
        self.allDirectories[0].displayContent()

    def getCurrentDir(self):
        return self.currentDirectory

    def getAllDirectories(self):
        return self.allDirectories


class Directory():

    def __init__(self, _name, _parentDirectory=None):
        self.name = _name
        self.totalSize = 0
        self.dirContents = []

        if _parentDirectory == None:
            self.parentDirectory = self
            self.depth = 0
        else:
            self.parentDirectory = _parentDirectory
            self.depth = self.parentDirectory.getDepth() + 1

    def addFile(self, _file):
        self.dirContents.append(_file)

    def addDirectory(self, _directory):
        self.dirContents.append(_directory)

    def calculateTotalSize(self):
        self.totalSize = 0

        for entity in self.dirContents:

            if isinstance(entity, Directory):
                self.totalSize += entity.calculateTotalSize()
            
            elif isinstance(entity, File):
                self.totalSize += entity.getSize()

        return self.totalSize

    def getName(self):
        return self.name

    def getParentDir(self):
        if self.getName() == "/":
            return self
        else:
            return self.parentDirectory

    def getTotalSize(self):
        return self.totalSize

    def getDirContents(self):
        return self.dirContents

    def getDepth(self):
        return self.depth

    def displayContent(self):

        for entity in self.dirContents:
            tabs = "  " * entity.getDepth()

            if isinstance(entity, Directory):
                print(f"{tabs}- {entity.getName()} (dir) [totalSize: {entity.getTotalSize()}]")
                entity.displayContent()
            
            elif isinstance(entity, File):
                print(f"{tabs}- {entity.getName()} (file, {entity.getSize()})")

    def getInfo(self):
        txt = f"{self.getName()} (dir):\t"
        for entity in self.getDirContents():
            if isinstance(entity, File):
                txt += f"{entity.getName()} (file, {entity.getSize()}), "

            elif isinstance(entity, Directory):
                txt += f"{entity.getName()} (dir), "
        return txt

class File():
    
    def __init__(self, _name, _size, _partentDirectory):
        self.name = _name
        self.size = _size
        self.parentDirectory = _partentDirectory
        self.depth = self.parentDirectory.getDepth() + 1

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

    def getDepth(self):
        return self.depth

def getInputLines(inputPath):
    f = open(inputPath, "rt")
    inputLines = f.readlines()
    f.close()

    for i in range(len(inputLines)):
        inputLines[i] = inputLines[i].replace("\n", "")

    return inputLines

def getInitialFileSystem(inputLines):
    fs = Filesystem()
    isListing = False

    for i, line in enumerate(inputLines):
        line = line.split(" ")
        if i == 0:
            dirName = line[2]
            fs.createDirectory(dirName)
            fs.changeDirectory(dirName)
            continue

        if line[0] == "dir" and isListing == True:
            dirName = line[1]

            dirExistsInCurrentDir = False
            for entity in fs.getCurrentDir().getDirContents():
                if entity.getName() == dirName:
                    dirExistsInCurrentDir = True
                    break
            
            if dirExistsInCurrentDir == False:
                fs.createDirectory(dirName)
        
        elif line[0].isdigit() and isListing == True:
            fileName = line[1]
            fileSize = int(line[0])

            fileExists = False
            for entity in fs.getCurrentDir().getDirContents():
                if entity.getName() == fileName:
                    fileExists = True
                    break

            if fileExists == False:
                fs.createFile(fileName, fileSize, fs.getCurrentDir())

        elif line[0] == "$":
            isListing = False
            command = line[1]

            if command == "ls":
                isListing = True
            
            elif command == "cd":
                destinationDirName = line[2]
                fs.changeDirectory(destinationDirName)

    a = fs.getAllDirectories()[0].calculateTotalSize()

    return fs

def solvePartOne(inputLines):
    
    fs = getInitialFileSystem(inputLines)
    # fs.displayDirectories()

    sumOfSizes = 0
    for directory in fs.getAllDirectories():
        if directory.getTotalSize() <= 100000:
            sumOfSizes += directory.getTotalSize()
    
    solution = sumOfSizes
    print(f"Day 6, part 1 solution: {solution}")


def solvePartTwo(inputLines):
    
    fs = getInitialFileSystem(inputLines)
    # fs.displayDirectories()

    totalFreeSpace = 70000000
    requiredFreeSpace = 30000000

    currentFreeSpace = totalFreeSpace - fs.getAllDirectories()[0].getTotalSize()
    smallestSizeToDelete = fs.getAllDirectories()[0].getTotalSize()

    for directory in fs.getAllDirectories():
        if directory.getTotalSize() + currentFreeSpace >= requiredFreeSpace and directory.getTotalSize() < smallestSizeToDelete:
            smallestSizeToDelete = directory.getTotalSize()
    
    solution = smallestSizeToDelete
    print(f"Day 6, part 2 solution: {solution}")

def main():
    inputPath = "day6_input.txt"

    inputLines = getInputLines(inputPath)

    solvePartOne(inputLines)
    solvePartTwo(inputLines) 


if __name__ == "__main__":
    main()