def readFile(filepath):
    with open(filepath) as file:
        lines = file.readlines()
    return lines


days = 0
state = []

oldState = [0,0,0,0,0,0,0,0,0]

lines = readFile('input')
for line in lines:
    line = line.split(',')

for entry in line:
    state.append(int(entry))

for fish in state:
    oldState[fish] += 1

for i in range(80):
    newState = [0,0,0,0,0,0,0,0,0]
    newState[0] = oldState[1]
    newState[1] = oldState[2]
    newState[2] = oldState[3]
    newState[3] = oldState[4]
    newState[4] = oldState[5]
    newState[5] = oldState[6]
    newState[6] = oldState[0] + oldState[7]
    newState[7] = oldState[8]
    newState[8] = oldState[0]
    oldState = newState
    fishSum = 0
    for fish in oldState:
        fishSum += fish
    print('Day ' + str(i+1) + ': ' + str(fishSum))
