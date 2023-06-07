import numpy as np
import sys

# Getting the path to the input file and opening the file
args = sys.argv[1:]
file = args[0]
lineCount = 0

# Variables the input file gives
mapRows = 0
mapCols = 0
robotMap = np.array()
noOfObservations = 0
observations = np.array()
errorRate = 0

# Reading the variables from the input file
for line in file:
    lineCount += 1



a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])
maps = [a,b,c]

np.savez("output.npz", *maps)
print(maps)