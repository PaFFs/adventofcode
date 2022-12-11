import common

f = common.readFile('indata')

cycle = 1
X = 1
signalStrengths = 0
for line in f:
    if line[0:4] == 'noop':
        cycle += 1
    else:
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            print('Signal strength at cycle' + str(cycle) + ': ' + str(cycle * X))
            signalStrengths += cycle*X
        X += int(line[5:])
        cycle += 1
    if cycle in [20, 60, 100, 140, 180, 220]:
        print('Signal strength at cycle' + str(cycle) + ': ' + str(cycle * X))
        signalStrengths += cycle * X
print(signalStrengths)
