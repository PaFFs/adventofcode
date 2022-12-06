import common, collections

f = common.readFile('indata')

# get number of piles
piles = 0
height = 0
for line in f:
    # stop if line contains numbers
    if line[1] == '1':
        piles = line[-2]
        height = f.index(line)
        break

# read piles height amount of times
pileDict = {}
for i in range(1, height + 1):
    line = f[i-1]
    # start at line[1], increment by 4 until line[33], or len(line)-3
    for x in range(1, (len(line) - 2), 4):
        if line[x].isupper():
            char = line[x]
            pos = x//4+1
            if pos not in pileDict.keys():
                pileDict.update({pos: char})
            else:
                pileDict[pos] = pileDict[pos] + char

# reverse chars in pileDict
for key in pileDict:
    pileDict[key] = common.reverseString(pileDict[key])

# read instructions
pileDict2 = pileDict.copy()
for i in range(height+2, len(f)):
    line = f[i].split(' from ')
    numberToMove = int(line[0].split(' ')[1])
    fromStack = int(line[1].split(' to ')[0])
    toStack = int(line[1].split(' to ')[1])
    for x in range(1, numberToMove+1):
        char = pileDict[fromStack][-1]
        pileDict[toStack] = pileDict[toStack] + char
        pileDict[fromStack] = pileDict[fromStack][:-1]


# print out the final response for task 1
response = ''
for key in sorted(pileDict):
    response += pileDict[key][-1]
print(response)

# read instructions for task 2
for i in range(height+2, len(f)):
    line = f[i].split(' from ')
    numberToMove = int(line[0].split(' ')[1])
    fromStack = int(line[1].split(' to ')[0])
    toStack = int(line[1].split(' to ')[1])
    stack = pileDict2[fromStack][-numberToMove:]
    pileDict2[toStack] += stack
    pileDict2[fromStack] = pileDict2[fromStack][:-numberToMove]

# print out the final response for task 2
response = ''
for key in sorted(pileDict2):
    response += pileDict2[key][-1]
print(response)
