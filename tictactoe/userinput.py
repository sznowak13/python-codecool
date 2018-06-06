import gridgen

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
    ln = len(grid)   # Variable to store the length of the grid
    rotGrid = gridgen.rotateGrid(grid) # Preparing the rotated grid, to check on the vertical lines
    for j in range(ln):
        if grid[j].count("x") == ln:  # Here, the function checks the lines, first horizontal, then the vertical, each for both players
            print("Player 1 wins!")
            return True
        if grid[j].count("o") == ln:
            print("Player 2 wins!")
            return True
        if rotGrid[j].count("x") == ln:
            print("Player 1 wins!")
            return True
        if rotGrid[j].count("o") == ln:
            print("Player 2 wins!")
            return True
    if (grid[0][0] and grid[1][1] and grid[2][2]) == 'x':
        print("Player 1 wins!")
        return True
    if (grid[2][0] and grid[1][1] and grid[0][2]) == 'x':
        print("Player 1 wins!")
        return True
    if (grid[0][0] and grid[1][1] and grid[2][2]) == 'o':
        print("Player 2 wins!")
        return True
    if (grid[2][0] and grid[1][1] and grid[0][2]) == 'o':
        print("Player 2 wins!")
        return True