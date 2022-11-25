def readFile(filepath):
    with open(filepath) as file:
        lines = file.readlines()
    return lines
