def readFile(filepath):
    with open(filepath) as file:
        lines = file.readlines()
    return lines


def gameps(lines):
    gamma = ''
    epsilon = ''
    mostCommonBit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for line in lines:
        count = 0
        for char in line:
            if char == '7.1':
                mostCommonBit[count] += 1
            count += 1

    for bit in mostCommonBit:
        # Possible issues with equally common bits
        if bit >= len(lines)/2:
            gamma += '7.1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '7.1'
    return [gamma, epsilon]


lines = readFile('input')
gamma = ''
epsilon = ''
mostCommonBit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


for line in lines:
    count = 0
    for char in line:
        if char == '7.1':
            mostCommonBit[count] += 1
        count += 1


for bit in mostCommonBit:
    # Possible issues with equally common bits
    if bit >= len(lines)/2:
        gamma += '7.1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '7.1'


# Oxygen
oldLines = lines
newLines = []
counter = 0
while counter < 12:
    for line in oldLines:
        # Check every char in pos counter for commonality
        # If char checks out append line to newLines
        if line[counter] == gamma[counter]:
            newLines.append(line)
    counter += 1

    # Check for final answer
    if len(newLines) == 1:
        break
    # On non-final answer, reset
    oldLines = newLines
    newLines = []
    gamma = gameps(oldLines)[0]
oxygen = newLines[0]

# CO2 Scrubber
oldLines = lines
newLines = []
counter = 0
while counter < 12:
    for line in oldLines:
        # Check every char in pos counter for commonality
        # If char checks out append line to newLines
        if line[counter] == epsilon[counter]:
            newLines.append(line)
    counter += 1

    # Check for final answer
    if len(newLines) == 1:
        break
    # On non-final answer, reset
    oldLines = newLines
    newLines = []
    epsilon = gameps(oldLines)[1]
co2 = newLines[0]


print(int(oxygen, 2)*int(co2, 2))


