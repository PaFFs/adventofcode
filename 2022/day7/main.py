import common


class Directory:
    directoriesFileSum = 0

    def __init__(self, name, parent=None):
        self.name = name
        self.directories = []
        self.files = []
        self.parent = parent
        self.directoryFileSum = 0
        self.directorySizes = []

    def addDirectory(self, directory):
        self.directories.append(directory)

    def addFile(self, file):
        self.files.append(file)

    def fileSize(self):
        for files in self.files:
            self.directoryFileSum += int(files.size)
        for directory in self.directories:
            self.directoryFileSum += directory.fileSize()
        if self.directoryFileSum <= 100000:
            Directory.directoriesFileSum += self.directoryFileSum
        return self.directoryFileSum

    def returnDirectories(self):
        for directory in self.directories:
            for subDirectory in directory.returnDirectories():
                self.directorySizes.append([subDirectory[0], subDirectory[1]])
            # self.directorySizes.append(directory.returnDirectories())
        self.directorySizes.append([self.name, self.directoryFileSum])
        return self.directorySizes


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


f = common.readFile('indata')

# Create the file system
Dir = Directory('/')
topDir = Dir
currentDir = Dir
for line in range(2, len(f)):
    if f[line].startswith('$'):
        if f[line].startswith('$ cd ..'):
            # open parent dir
            currentDir = currentDir.parent
        elif f[line].startswith('$ cd '):
            # open child dir
            newDirName = f[line].split('cd ')[1][:-1]
            for dirs in currentDir.directories:
                if str(dirs.name) == str(newDirName):
                    currentDir = dirs
                    break
        elif f[line].startswith('$ ls'):
            continue
    elif f[line].startswith('dir '):
        # new child dir with name f[line][4:-1] and parent currentDir
        newDir = Directory(f[line][4:-1], currentDir)
        currentDir.addDirectory(newDir)
    else:
        # new file with size = f[line].split(' ')[0] and name f[line].split(' ')[1]
        newFile = File(f[line].split(' ')[1], f[line].split(' ')[0])
        currentDir.addFile(newFile)

# add sizes of all directories with size <= 100000
topDir.fileSize()
print(Directory.directoriesFileSum)
unusedSpace = 70000000 - topDir.directoryFileSum
neededSpace = 30000000 - unusedSpace
dirToDelete = topDir.returnDirectories()[0][1]
possibleDirs = []
for dir in topDir.returnDirectories()[1:]:
    if dir[1] >= neededSpace:
        if dir[1] > dirToDelete:
            possibleDirs.append(dir[1])
possibleDirs.sort()
print(possibleDirs[0])
