import common

f = common.readFile('indata')

counter = 0
bigCounter = 0
for pairs in f:
    left = pairs.split(',')[0]
    left = left.split('-')
    right = pairs.split(',')[1]
    right = right.split('-')
    pair1 = range(int(left[0]), int(left[1]) + 1)
    pair2 = range(int(right[0]), int(right[1]) + 1)
    if set(pair1).issubset(set(pair2)):
        counter += 1
    elif set(pair2).issubset(set(pair1)):
        counter += 1

    for num in pair1:
        if num in pair2:
            bigCounter += 1
            break

print(counter)
print(bigCounter)
