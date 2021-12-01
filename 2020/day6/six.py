def readfile(path):
    textfile = open(path, "r")

    lines = textfile.readlines()
    group = ""
    groups = []

    for line in lines:
        if line == "\n":
            group.replace("\n", "")
            group = "".join(dict.fromkeys(group))
            groups.append(group)
            group = ""
        else:
            group = group + line
            group.replace("\n", "")

    group = "".join(dict.fromkeys(group))
    groups.append(group)
    return groups


def countgroups(groups):
    import string
    val = string.ascii_lowercase[0:26]
    counts = []

    for group in groups:
        count = 0
        for char in group:
            if char in val:
                count += 1
        counts.append(count)
    return counts


def readfiletooelectricbogaloo(path):
    textfile = open(path, "r")

    lines = textfile.readlines()
    group = []
    groups = []

    for line in lines:
        if line == "\n":
            group.append(line)
            groups.append(group)
            group = []
        else:
            group.append(line)

    groups.append(group)
    return groups


def checkifallagree(groups):
    import string
    val = string.ascii_lowercase[0:26]
    counts = []

    for group in groups:
        count = 0
        for char in val:
            charcheck = []
            for person in group:
                if person == "\n":
                    continue
                if char in person:
                    charcheck.append(True)
                else:
                    charcheck.append(False)
            if all(charcheck):
                count += 1
        counts.append(count)
    return sum(counts)


filepath = "6.in"
print(sum(countgroups(readfile(filepath))))
print(checkifallagree(readfiletooelectricbogaloo(filepath)))
