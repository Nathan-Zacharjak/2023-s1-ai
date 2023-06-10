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
            obsArray.append(char)

        observations.append(obsArray)
    elif lineCount == 3 + mapRows + noOfObservations:
        errorRate = float(line[0])
        
file.close()

# Preparing the variables needed for the viterbi program
robotMap = np.array(robotMap, dtype=str)
observations = np.array(observations, dtype=str)

# 1. Build Tm (Transition/Probability of position change matrix)
validPositions = []
rowNum = 0
colNum = 0
for row in robotMap:
    for col in row:
        if col == "0":
            validPositions.append((rowNum, colNum))

        colNum += 1

    rowNum += 1

# Finds and returns the values of adjacent positions on the robot map
def FindAdjacentValues(value, rowNum, colNum):
    adjValues = {"north": "null",
                 "south": "null",
                 "west": "null",
                 "east": "null"}

    if rowNum == 0 or rowNum == mapRows - 1:
        west = "X"

    if colNum == 0

    for 

    return adjValues

Tm = []
rowNum = 0
colNum = 0
for row in robotMap:
    TmRow = []

    for col in row:
        prob = 0
        adjValues = FindAdjacentValues(col, rowNum, colNum)

        TmRow.append(prob)

    colNum += 1

    rowNum += 1
    Tm.append(TmRow)


# 2. Build Em (Emission/Probability of observation error matrix) (NSWE)

# 3. Create the array of initial probabilities (Robot is equally likely to be at any position, 1/N probability)
#    trellis[i,1] ← πi * Emiy1

# 4. Add the first entry to the trellis matrix, by implementing the first for loop in the pseudoscope
#    using the array of initial probabilities and the emission matrix
trellis = []

# 5. Do the gigachad 2nd for loop in the pesudocode
#   a. Find the set of most likely prior positions at the previous j-1 timestep, and put this into variable K
#   b. Calculate a temporary set of probabilities "KTemp" using trellis[i,j] ← trellis[k, j - 1] * Tm_ki ∗ Em_ij for each k
#   c. Find the maximum probability calculated from "KTemp", and put that into the position i, and timestep j in the trellis matrix
#   d. Repeat for the next position for every timestep

# 6. Reformat the arrays of probabilities (the "trellis" array) into proper trellis matrices,
#    as formatted by gradescope by adding 0's at each of the X positions of the robot map
#    and put them into an array called "output"
output = []

# 6. Print and export the output array using print() and np.savez()
print(output)
np.savez("output.npz", *output)
