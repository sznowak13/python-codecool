import gridgen
import userinput

# Imported modules are selfmade files with definitions of functions 
# that are running the game

gameOver = False
player = True

size = 3
#size = input("What size of grid do you want?")

newGrid = gridgen.getGrid(int(size))
gridgen.printGrid(newGrid)
while not gameOver:
    player = userinput.plrChoose(newGrid, player)
    gridgen.printGrid(newGrid)
    gameOver = userinput.checkGrid(newGrid)

print("G A M E  O V E R   :<")