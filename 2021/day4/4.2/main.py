def readFile(filepath):
    with open(filepath) as file:
        lines = file.readlines()
    return lines


class Board:
    # when board is initiated, creates a 5x5 array
    def __init__(self):
        w, h = 5, 5
        self.cells = [[0 for x in range(w)] for y in range(h)]


    # takes a list of 5 strings and writes them to the cells
    def setCells(self, lines):
        if len(lines) != 5:
            print('setCells error, lines not 5 in length')
            return
        for line in lines:
            lineIndex = lines.index(line)
            line = line.split()
            for num in line:
                numIndex = line.index(num)
                self.cells[lineIndex][numIndex] = num


    # marks any matching value with 'x'
    def markValue(self, val):
        for row in self.cells:
            rowIndex = self.cells.index(row)
            for col in row:
                colIndex = row.index(col)
                if col == val:
                    self.cells[rowIndex][colIndex] = 'x'


    # checks if the board has won
    def winState(self):
        self.row = ['', '', '', '', '']
        for row in self.cells:
            self.row = row
            boolListRow = [cell == 'x' for cell in self.row]
            if all(boolListRow):
                return True

        for i in range(5):
            self.col = []
            for row in self.cells:
                self.col.append(row[i])
            boolListCol = [cell == 'x' for cell in self.col]
            if all(boolListCol):
                return True
        return False


    # calculates points for a board
    def points(self, lastCall):
        sum = 0
        for row in self.cells:
            for col in row:
                if col != 'x':
                    sum += int(col)
        return int(sum) * int(lastCall)


lines = readFile('input')
drawOrder = lines[0].split(',')

boards = []
row = 2
while row < len(lines):
    board = Board()
    board.setCells(lines[row:row+5])
    boards.append(board)
    row += 6

for drawNum in drawOrder:
    for board in boards:
        board.markValue(drawNum)
    boardsLogic = boards
    for board in boards:
        if board.winState():
            if len(boardsLogic) > 1:
                boardsLogic.remove(board)
            else:
                print(board.points(drawNum))
                break
    else:
        continue
    break