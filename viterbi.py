import numpy as np
import sys

# Getting the path to the input file and opening the file
args = sys.argv[1:]
file = open(args[0])
lineCount = 0

# Variables the input file gives
mapRows = 0
mapCols = 0
robotMap = []
noOfObservations = 0
observations = []
errorRate = 0

# Reading the variables from the input file
for line in file:
    lineCount += 1
    line = line.rstrip()
    line = line.split(" ")
    obsArray = []

    if lineCount == 1:
        mapRows = int(line[0])
        mapCols = int(line[1])
    elif lineCount > 1 and lineCount < 2 + mapRows:
        robotMap.append(line)
    elif lineCount == 2 + mapRows:
        noOfObservations = int(line[0])
    elif lineCount > 2 + mapRows and lineCount < 3 + mapRows + noOfObservations:
        for char in line[0]:
            if char == '1':
                char = 'X'

            obsArray.append(char)

        observations.append(obsArray)
    elif lineCount == 3 + mapRows + noOfObservations:
        errorRate = float(line[0])
        
file.close()

# Preparing the variables needed for the viterbi program
robotMap = np.array(robotMap, dtype=str)
observations = np.array(observations, dtype=str)

# 1. Build Tm (Transition/Probability of position change matrix)
# Getting an array of valid positions
validPositions = []
rowNum = 0
colNum = 0
for row in robotMap:
    for col in row:
        if col == "0":
            validPositions.append((rowNum, colNum))

        colNum += 1
    colNum = 0
    rowNum += 1

# Finds and returns the values of adjacent positions on the robot map
def FindAdjacentValues(rowNum, colNum):
    adjValues = {"north": "null",
                 "south": "null",
                 "west": "null",
                 "east": "null"}
    
    if rowNum <= 0:
        adjValues["north"] = "X"
    if rowNum >= mapRows - 1:
        adjValues["south"] = "X"
    if colNum <= 0:
        adjValues["west"] = "X"
    if colNum >= mapCols - 1:
        adjValues["east"] = "X"

    for key, value in adjValues.items():
        if value == "null":
            if key == "north":
                adjValues[key] = robotMap[rowNum - 1][colNum]
            elif key == "south":
                adjValues[key] = robotMap[rowNum + 1][colNum]
            elif key == "west":
                adjValues[key] = robotMap[rowNum][colNum - 1]
            elif key == "east":
                adjValues[key] = robotMap[rowNum][colNum + 1]

    return adjValues

# Building the Tm matrix
Tm = []
rowNum = 0
colNum = 0

for fromPos in validPositions:
    xFrom = fromPos[0]
    yFrom = fromPos[1]

    # Creating an array of a position's neighbouring positions
    neighbours = {}
    for toPos in validPositions:
        xTo = toPos[0]
        yTo = toPos[1]
        toValue = robotMap[xTo, yTo]

        if toValue == "X":
            continue
        elif abs(xTo - xFrom) == 1 and abs(yTo - yFrom) == 0:
            neighbours[toPos] = True
        elif abs(xTo - xFrom) == 0 and abs(yTo - yFrom) == 1:
            neighbours[toPos] = True
    
    # Putting the probabilities of travelling from this point into the transition matrix
    row = []
    prob = 1/len(neighbours)
    for pos in validPositions:
        if neighbours.get(pos):
            row.append(prob)
        else:
            row.append(0)

    Tm.append(row)

print("Transition matrix:")
for row in Tm:
    print(row)

# 2. Build Em (Emission/Probability of observation error matrix) (NSWE)
# For every valid position, find the number of incorrect detections for each observation
Em = []
for pos in validPositions:
    posRow = []
    adjValues = FindAdjacentValues(pos[0], pos[1])

    for obs in observations:
        incorrectCount = 0

        if adjValues.get("north") != obs[0]:
            incorrectCount += 1
        if adjValues.get("south") != obs[1]:
            incorrectCount += 1
        if adjValues.get("west") != obs[2]:
            incorrectCount += 1
        if adjValues.get("east") != obs[3]:
            incorrectCount += 1

        # Use the incorrect count to now calculate the value
        # that goes in the emission matrix
        prob = pow(1 - errorRate, 4 - incorrectCount) * pow(errorRate, incorrectCount)

        posRow.append(prob)
    
    Em.append(posRow)

print("Emission matrix:")
for row in Em:
    print(row)

# 3. Create the array of initial probabilities (Robot is equally likely to be at any position, 1/N probability)
#    trellis[i,1] ← πi * Emiy1

# 4. Add the first entry to the trellis matrix, by implementing the first for loop in the pseudoscope
#    using the array of initial probabilities and the emission matrix
trellis = []

# 5. Do the gigachad 2nd for loop in the pesudocode
#   a. Find the set of most likely prior positions at the previous j-1 timestep, and put this into variable K
#   b. Calculate a temporary set of probabilities "KTemp" using trellis[i,j] ← trellis[k, j - 1] * Tm_ki ∗ Em_ij
#      for each most likely prior position(s) in K, where k is one of the most likely prior positions
#      (more than 1 if multiple positions have the same highest value!)
#   c. Find the maximum probability calculated from "KTemp", and put that into the position i, and timestep j in the trellis matrix
#   d. Repeat for the next position until all positions are done for that timestep
#   e. Repeat for every timestep

# 6. Reformat the arrays of probabilities (the "trellis" array) into proper trellis matrices,
#    as formatted by gradescope by adding 0's at each of the X positions of the robot map
#    and put them into an array called "output"
output = []

# 6. Print and export the output array using print() and np.savez()
np.savez("output.npz", *Em)
