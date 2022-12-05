import common

f = common.readFile('indata')

points = 0
for line in f:
    if line[2] == 'X':
        points += 1
        if line[0] == 'A':
            points += 3
        elif line[0] == 'B':
            pass
        else:
            points += 6
    elif line[2] == 'Y':
        points += 2
        if line[0] == 'A':
            points += 6
        elif line[0] == 'B':
            points += 3
        else:
            pass
    else:
        points += 3
        if line[0] == 'A':
            pass
        elif line[0] == 'B':
            points += 6
        else:
            points += 3

print(points)

games = []
for line in f:
    if line[0] == 'A':
        win = 'Y'
        draw = 'X'
        loss = 'Z'
    elif line[0] == 'B':
        win = 'Z'
        draw = 'Y'
        loss = 'X'
    else:
        win = 'X'
        draw = 'Z'
        loss = 'Y'

    if line[2] == 'X':
        play = loss
    elif line[2] == 'Y':
        play = draw
    else:
        play = win
    games.append(line[0] + ' ' + play)

points = 0
for line in games:
    if line[2] == 'X':
        points += 1
        if line[0] == 'A':
            points += 3
        elif line[0] == 'B':
            pass
        else:
            points += 6
    elif line[2] == 'Y':
        points += 2
        if line[0] == 'A':
            points += 6
        elif line[0] == 'B':
            points += 3
        else:
            pass
    else:
        points += 3
        if line[0] == 'A':
            pass
        elif line[0] == 'B':
            points += 6
        else:
            points += 3

print(points)