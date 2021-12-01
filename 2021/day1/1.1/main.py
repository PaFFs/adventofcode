def readFile(filepath):
    with open(filepath) as file:
        lines = file.readlines()
    return lines


path = 'input'
lines = readFile(path)
biggerNums = 0

pastNum = 1000
for line in lines:
    newNum = int(line)
    if newNum > pastNum:
        biggerNums += 1
    pastNum = int(line)

print(biggerNums)
