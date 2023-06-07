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

robotMap = np.array(robotMap, dtype=str)
observations = np.array(observations, dtype=str)

output = [mapRows, mapCols, robotMap, noOfObservations, observations, errorRate]
print(output)
np.savez("output.npz", *output)


# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# c = np.array([7, 8, 9])
# maps = [a,b,c]

# np.savez("output.npz", *maps)
# print(maps)