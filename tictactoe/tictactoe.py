import gridgen
import userinput

# Imported modules are selfmade files with definitions of functions 
# that are running the game

# Setup:
# gameOver is a boolean telling the program when to end the game;
# player is a boolean that represents which player should move now: True is P1 and False is P2
# (by deafaut P1 starts)
# size is value of the side of the grid
# time is a variable that keeps track of used moves
# the game is caled a draw, when all the possible moves are done

gameOver = False
player = True
size = 3
time = size**2

newGrid = gridgen.getGrid(int(size))
gridgen.printGrid(newGrid)
while not gameOver and not time == 0:
    player = userinput.plrChoose(newGrid, player)
    gridgen.printGrid(newGrid)
    gameOver = userinput.checkGrid(newGrid)
    time -= 1
    
if time == 0:
    print("Draw!")
print("G A M E  O V E R")