import common

f = common.readFile('indata')

prioSum = 0
for line in f:
    middle = (len(line) // 2)
    aLine = line[0:middle]
    bLine = line[middle:]
    for char in aLine:
        if char in bLine:
            if char.isupper():
                prioSum += ord(char) - 38
                break
            else:
                prioSum += ord(char) - 96
                break

print(prioSum)

prioSum = 0
fThird = f[0::3]
for line in f:
    if line in fThird:
        fIndex = f.index(line)
        for char in line:
            if char in f[fIndex+1]:
                if char in f[fIndex+2]:
                    if char.isupper():
                        prioSum += ord(char) - 38
                        break
                    else:
                        prioSum += ord(char) - 96
                        break
    else:
        continue

print(prioSum)
