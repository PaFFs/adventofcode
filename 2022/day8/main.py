import common

f = common.readFile('indata')

# construct grid and fill it, borders with -1
width = len(f[0]) - 1
row = []
for i in range(0, width + 2):
    row.append(-1)
grid = [row]
for line in f:
    row = [-1]
    for char in line[:-1]:
        row.append(int(char))
    row.append(-1)
    grid.append(row)
row = []
for i in range(0, width + 2):
    row.append(-1)
grid.append(row)

# go through each cell apart from the borders
rowIndex = 1
visibleTrees = 0
highestScenicScore = 0
treeScenicScore = 0
for row in grid[1:-1]:
    colIndex = 1
    for cell in row[1:-1]:
        leftView, rightView, upView, downView = 0, 0, 0, 0
        # do the magic here
        # check left
        left = False
        print(grid[rowIndex][:colIndex])
        for subCell in reversed(grid[rowIndex][:colIndex]):
            print(subCell)
            if subCell >= cell:
                left = True
                leftView += 1
                break
            elif subCell != -1:
                leftView += 1

        # check right
        right = False
        for subCell in grid[rowIndex][colIndex+1:]:
            if subCell >= cell:
                right = True
                rightView += 1
                break
            elif subCell != -1:
                rightView += 1

        # check up
        up = False
        for subRow in grid[:rowIndex]:
            subCell = subRow[colIndex]
            if subCell >= cell:
                up = True
                upView += 1
                break
            elif subCell != -1:
                upView += 1

        # check down
        down = False
        for subRow in grid[rowIndex+1:]:
            subCell = subRow[colIndex]
            if subCell >= cell:
                down = True
                downView += 1
                break
            elif subCell != -1:
                downView += 1

        # check if the tree is visible
        if not up or not down or not left or not right:
            visibleTrees += 1
        # check if the trees scenic score is higher than the record
        treeScenicScore = leftView * rightView * upView * downView
        if treeScenicScore > highestScenicScore:
            highestScenicScore = treeScenicScore

        colIndex += 1

    rowIndex += 1

print(visibleTrees)
print(highestScenicScore)
