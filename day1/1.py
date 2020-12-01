textFile = open("in", "r")
numList = []

lines = textFile.readlines()
for line in lines:
    num = int(line)
    numList.append(num)

for num1 in numList:
    for num2 in numList:
        if num1 + num2 == 2020:
            print(num1 * num2)
            exit()


