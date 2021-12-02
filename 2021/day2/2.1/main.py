def readFile(filepath):
    with open(filepath) as file:
        lines = file.readlines()
    return lines


lines = readFile('input')
forward = 0
depth = 0

for line in lines:
    line = line.split()
    if line[0] == 'forward':
        forward += int(line[1])
    elif line[0] == 'down':
        depth += int(line[1])
    else:
        depth -= int(line[1])

print(forward)
print(depth)
print(forward*depth)
