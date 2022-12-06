def readFile(filepath):
    with open(filepath) as file:
        lines = file.readlines()
    return lines


def reverseString(string):
    return string[::-1]
