def readfile(path):
    textfile = open(path, "r")

    lines = textfile.readlines()

    return lines


def seat(seatstr):
    seatrow = seatstr[:7]
    seatrow = seatrow.replace("F", "0")
    seatrow = seatrow.replace("B", "1")
    seatrow = int(seatrow,2)

    seatcol = seatstr[7:]
    seatcol = seatcol.replace("R", "1")
    seatcol = seatcol.replace("L", "0")
    seatcol = int(seatcol,2)

    seatid = seatrow * 8 + seatcol

    return seatrow, seatcol, seatid


def highestid(seatlines):
    highest = 0
    for seatline in seatlines:
        if seat(seatline)[2] > highest:
            highest = seat(seatline)[2]
    return highest


def sortids(seatlines):
    seatids = []
    for seatline in seatlines:
        seatids.append(seat(seatline)[2])
    seatids.sort()
    return seatids


def findmissingid(seats):
    lowestid = seats[0]
    for seat in seats:
        if seat == lowestid:
            lowestid += 1
            continue
        return seat - 1

print(highestid(readfile("5.in")))
print(findmissingid(sortids(readfile("5.in"))))
