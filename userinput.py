def plrChoose(grid, whichOne):
    if whichOne == True:
        usr = input("P1: Choose an empty spot: ")
        x = int(usr[0])
        y = int(usr[1])
        if grid[x][y] == " ":
            grid[x][y] = "x"
            return False
        else:
            print("That spot is already taken!")
    else:
        usr = input("P2: Choose an empty spot: ")
        x = int(usr[0])
        y = int(usr[1])
        if grid[x][y] == " ":
            grid[x][y] = "o"
            return True
        else:
            print("That spot is already taken!")

def checkGrid(grid):
    spots = len(grid) * len(grid[0])
    emptySpots = 0
    xs = 0
    os = 0
    for i in grid:
        for j in i:
            if j == " ":
                emptySpots += 1
            elif j == "x":
                xs += 1
            elif j == "o":
                os += 1
    if emptySpots == 0:
        return True
    