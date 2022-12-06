import common

f = common.readFile('indata')
message = f[0]

# task 1
for i in range(3, len(message)):
    chars = list(message[i-3:i+1])
    if common.checkDuplicates(chars):
        continue
    else:
        print(i+1)
        break
# task 2
for i in range(13, len(message)):
    chars = list(message[i-13:i+1])
    if common.checkDuplicates(chars):
        continue
    else:
        print(i+1)
        break
