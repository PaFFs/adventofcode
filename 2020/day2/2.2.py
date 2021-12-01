textFile = open("2.in", "r")
passwords = []
keysLow = []
keysHigh = []
keysLetter = []

lines = textFile.readlines()
for line in lines:
    key = line.partition(":")[0]
    lowKey = key.partition("-")[0]
    keysLow.append(lowKey)

    first, *middle, last = key.split()
    letterKey = last
    keysLetter.append(letterKey)
    highKey = first.partition("-")[-1]
    keysHigh.append(highKey)

    first, *middle, last = line.split()
    passwords.append(last)

key = 0
correctPasswords = 0
for password in passwords:
    lowKey = password[int(keysLow[key]) - 1]
    highKey = password[int(keysHigh[key]) - 1]
    letter = keysLetter[key]
    if lowKey == letter:
        if highKey != letter:
            correctPasswords += 1
    if highKey == letter:
        if lowKey != letter:
            correctPasswords += 1
    key += 1
print(correctPasswords)