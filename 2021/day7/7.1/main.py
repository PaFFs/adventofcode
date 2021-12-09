def readFile(filepath):
    with open(filepath) as file:
        lines = file.readlines()
    return lines


nums = readFile('input')
nums = nums[0].split(',')
nums = [int(numstring) for numstring in nums]

highest = nums[0]
lowest = nums[0]

for num in nums:
    if num > highest:
        highest = num
    elif num < lowest:
        lowest = num

fuelList = []

for i in range(lowest, highest):
    fuel = 0
    for num in nums:
        fuel += abs(num-i)
    fuelList.append([i, fuel])

lowestPos = 100000000
fuel = 0

for pos in fuelList:
    if pos[1] < lowestPos:
        lowestPos = pos[1]
        fuel = pos[0]

print(lowestPos, fuel)
