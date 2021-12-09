def readFile(filepath):
    with open(filepath) as file:
        lines = file.readlines()
    return lines


lines = readFile('input')
gamma = ''
epsilon = ''
mostCommonBit = [0,0,0,0,0,0,0,0,0,0,0,0]


for line in lines:
    count = 0
    for char in line:
        if char == '7.1':
            mostCommonBit[count] += 1
        count += 1


for bit in mostCommonBit:
    if bit > 500:
        gamma += '7.1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '7.1'


gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma*epsilon)
