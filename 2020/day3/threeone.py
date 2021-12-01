def toboggan (down, side):
    textFile = open("3.in", "r")
    rows = []

    lines = textFile.readlines()
    for line in lines:
        rows.append(line)
    trees = 0
    jumps = 0

    width = 30
    hor = 0

    for line in lines:
        # Check if line is supposed to be read
        row = lines.index(line)
        if row % down != 0:
            continue

        # Check if tree
        if line[hor] == "#":
            # tree
            trees += 1

        # Prepare the next jump
        jumps += 1  # Increase the counter for no of jumps
        hor = hor + side  # Increase the horizontal position

        # If the next jump goes to far to the right, adjust
        if hor > width:
            hor = hor - width - 1



    # How many trees?
    print("Trees: " + str(trees))
    print("Jumps: " + str(jumps))
    return trees
