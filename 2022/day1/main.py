import common

f = common.readFile('indata')

elf = 0
elves = []
for line in f:
    if line != '\n':
        elf += int(line)
    else:
        elves.append(elf)
        elf = 0

elves.sort()
print(elves[-1]+elves[-2]+elves[-3])
