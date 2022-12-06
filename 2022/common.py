def readFile(filepath):
    with open(filepath) as file:
        lines = file.readlines()
    return lines


def reverseString(string):
    return string[::-1]


def checkDuplicates(listToCheck):
    if len(listToCheck) == len(set(listToCheck)):
        return False
    else:
        return True
