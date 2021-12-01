def readFile(filepath):
    with open(filepath) as file:
        lines = file.readlines()
    return lines


path = 'input'
lines = readFile(path)
biggerBlocks = 0
output = []

for x in range(len(lines)):
    try:
        line1 = int(lines[x])
        line2 = int(lines[x+1])
        line3 = int(lines[x+2])
        linesSum = line1 + line2 + line3
        output.append(linesSum)
    except IndexError:
        print("whoopsies")

biggerNums = 0
pastNum = 10000
for Sum in output:
    newNum = Sum
    if newNum > pastNum:
        biggerNums += 1
    pastNum = Sum

print(biggerNums)
