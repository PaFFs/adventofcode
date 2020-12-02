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
    letterNum = 0
    for char in password:
        if char == keysLetter[key]:
            letterNum += 1
    if int(keysLow[key]) <= letterNum <= int(keysHigh[key]):
        correctPasswords += 1
    key += 1

print(correctPasswords)