import math
import sys

# Getting and formatting command line arguments
# into a format GraphSearch() can read
args = sys.argv[1:]
inpSearch = args[1]
inpHeuristic = ""
inpSize = []
inpStart = []
inpEnd = []
inpMap = []

if len(args) > 2:
    inpHeuristic = args[2]

# Getting the input file's contents into the right format
f = open(args[0])
lineNumber = 1
for line in f:
    # Turning each line into an array of numbers and "X" strings
    line = line.rstrip()
    line = line.split(" ")
    mapRow = []
    for number in line:
        if number != "X":
            number = int(number)

        if lineNumber == 1:
            inpSize.append(number)
        elif lineNumber == 2:
            inpStart.append(number)
        elif lineNumber == 3:
            inpEnd.append(number)
        else:
            mapRow.append(number)
    if mapRow != []:
        inpMap.append(mapRow)

    lineNumber += 1
f.close()

def GeneratePath(map, start, consideredNode, maxLoops):
    currentNode = consideredNode
    loopCount = 0

    while loopCount < maxLoops:
        loopCount += 1

        # Staring the current node on the map
        row = currentNode[0]
        col = currentNode[1]
        map[row][col] = "*"
        if (row == start[0]) and (col == start[1]):
            return map

        # Getting the parent node of the current node
        currentNode = currentNode[2]

    if loopCount == maxLoops:
        return "Generate path loop count limit reached!"
    
    return map

# Returns true if the current node is the end node and
# sets off the generation of the path
def CheckIfEndNode(consideredNode, start, end, map, maxLoops):
    rowPos = consideredNode[0]
    colPos = consideredNode[1]

    if (rowPos == end[0]) and (colPos == end[1]):
        outMap = GeneratePath(map, start, consideredNode, maxLoops)

        return outMap, True
    else:
        return None, False

# Takes a node and finds all nodes connected to it,
# that can be added to the fringe,
# and returns the extended fringe
def ExpandFringe(closed, size, map, fringe, consideredNode, fringeIndex, heuristic, end):
    row = consideredNode[0]
    col = consideredNode[1]
    consideredNodeDepth = consideredNode[3]
    consideredNodeCost = consideredNode[6]
    consideredNodeValue = map[row][col]
    expandOrder = ["up", "down", "left", "right"]

    # Creating nodes and putting them in potentialExpand[]
    for dir in expandOrder:
        expRow = -1
        expCol = -1
        if dir == "up":
            expRow = row-1
            expCol = col
        elif dir == "down":
            expRow = row+1
            expCol = col
        elif dir == "left":
            expRow = row
            expCol = col-1
        elif dir == "right":
            expRow = row
            expCol = col+1
        
        # print((expRow, expCol), "Size[0]:")
        # Only adding expanded nodes to the fringe if they are valid and not closed
        if (expRow < 0) or (expRow > size[0] - 1):
            continue
        if (expCol < 0) or (expCol > size[1] - 1):
            continue
        expValue = map[expRow][expCol]
        if expValue == "X":
            continue
        if (expRow,expCol) in closed:
            continue
        
        # Need to ensure the cost and heuristic is calculated correctly!
        # Take the point in which the paths diverged, make a smaller test case, and calculate the cost + heuristic by hand!
        cost = consideredNodeCost + max(expValue - consideredNodeValue + 1, 1)
        # print((expRow,expCol),"cost:", cost)
        # If we're doing A* search and we've got a heuristic,
        # calculate it and add it to the cost
        if heuristic == "manhattan":
            rowDist = abs(expRow - end[0])
            # print("row:", expRow, "end:", end[0])
            colDist = abs(expCol - end[1])
            # print("col:", expCol, "end:", end[1])
            heuristicCost = rowDist + colDist
            cost = cost + heuristicCost
        if heuristic == "euclidean":
            rowDist = expRow - end[0]
            colDist = expCol - end[1]
            heuristicCost = math.sqrt(rowDist*rowDist + colDist*colDist)
            cost = cost + heuristicCost
        
        # print((expRow,expCol),"heuristicCost:", heuristicCost)
        node = (expRow, expCol, consideredNode, consideredNodeDepth + 1, dir, fringeIndex, cost)
        fringe.append(node)
        fringeIndex += 1

    return fringe, fringeIndex

# Returns the next node to expand based on the fringe
# and the type of search we are using
def ChooseNextConsideredNode(fringe, search):
    nextNodes = fringe

    if search != "bfs":
        # Take the first fringe node's cost to start with
        minCost = -1
        nextNodes = []
        for node in fringe:
            minCost = node[6]
            break
        
        # Now find the smallest cost out of all the nodes
        for node in fringe:
            cost = node[6]
            if cost < minCost:
                minCost = cost

        # Now find all nodes that have this cost
        for node in fringe:
            cost = node[6]
            if cost == minCost:
                nextNodes.append(node)

        # print("optimal nodes:", nextNodes)
        if len(nextNodes) == 0:
            return "No optimal nodes!"

    # Now from all these equally optimal nodes,
    # apply the "up, down, left right" priority to resolve a tie,
    # if there is more than 1 optimal cost node in nextNodes

    # Always pick the node with the lowest index as the indexes are always put in order
    # of the up, down, left, right
    lowestIndex = None
    nextNode = None

    # Put the first optimal node and its index as the initial lowest index
    for node in nextNodes:
        lowestIndex = node[5]
        nextNode = node
        break

    # Find the node with the lowest index
    for node in nextNodes:
        if node[5] < lowestIndex:
            lowestIndex = node[5]
            nextNode = node
        
    return nextNode

# Takes a search type, a grid to search, and a start and end
# and returns a path through the grid from the start
# to the goal by making "*"s along the path it found.
# Returns a string if it couldn't find a path
def GraphSearch(search, size, start, end, map, heuristic):
    # (row, col, parent, depth, direction, index, cost)
    start = (start[0] - 1, start[1] - 1, "startParent", 0, "startDir", -1, 0)
    end = (end[0] - 1, end[1] - 1)
    closed = set()
    fringe = [start]
    nodesConsidered = 1
    consideredNode = start
    fringeIndex = 0
    maxLoops = 50000

    while nodesConsidered <= maxLoops:
        print("Nodes considered:", nodesConsidered)
        # Remove the node from the fringe and consider if it is the end node
        fringe.remove(consideredNode)
 
        print("is consideredNode end:", consideredNode, end, consideredNode[0] == end[0] and consideredNode[1] == end[1])
        outMap, isEnd = CheckIfEndNode(consideredNode, start, end, map, maxLoops)
        if isEnd:
            return outMap
        
        # Close a node as it is searched
        closed.add((consideredNode[0], consideredNode[1]))

        # If it isn't the end, add its neighbors to the fringe
        fringe, fringeIndex = ExpandFringe(closed, size, map, fringe, consideredNode, fringeIndex, heuristic, end)

        # If there is no fringe, there is no valid path
        if len(fringe) == 0:
            return "Fringe empty"
        
        # If there is a fringe, choose the next node to check if its the end
        consideredNode = ChooseNextConsideredNode(fringe, search)
        # (And if something went wrong with that function return an error string)
        if type(consideredNode) == str:
            return consideredNode
        
        print("===================")
        nodesConsidered += 1

    return "Loop limit reached!"

# Runs the program and prints the result
result = GraphSearch(inpSearch, inpSize, inpStart, inpEnd, inpMap, inpHeuristic)
if type(result) == str:
    print(result)
    # print("null")
else:
    for row in result:
        printRow = ""
        for col in row:
            stringCol = str(col)
            printRow = printRow + " " + stringCol
        # Removing the first unneeded space in each row
        print(printRow[1:])