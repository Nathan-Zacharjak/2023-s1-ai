import numpy as np

# Emulating an input from console
inpSearch = "bfs"
inpStart = (1,1)
inpEnd = (10,10)
inpSize = (10,10)
# inpEnd = (3,3)
# inpSize = (3,3)
# inpMap = [[1, 1, "X"],
#         [4, "X", 1],
#         [7, 6, 1]]
inpMap = [[1, 1, 1, 1, 1, 1, 4, 7, 8, "X"],
        [1, 1, 1, 1, 1, 1, 1, 5, 8, 8],
        [1, 1, 1, 1, 1, 1, 1, 4, 6, 7],
        [1, 1, 1, 1, 1, "X", 1, 1, 1, 6],
        [1, 1, 1, 1, 1, "X", 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [6, 1, 1, 1, 1, "X", 1, 1, 1, 1],
        [7, 7, 1, "X", "X", "X", 1, 1, 1, 1],
        [8, 8, 1, 1, 1, 1, 1, 1, 1, 1],
        ["X", 8, 7, 1, 1, 1, 1, 1, 1, 1]]

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
    print("is consideredNode end:", consideredNode, end, rowPos == end[0] and colPos == end[1])

    if (rowPos == end[0]) and (colPos == end[1]):
        outMap = GeneratePath(map, start, consideredNode, maxLoops)

        return outMap, True
    else:
        return None, False

# Takes a node and finds all nodes connected to it,
# that can be added to the fringe,
# and returns the extended fringe
def ExpandFringe(closed, size, map, fringe, consideredNode, fringeIndex):
    row = consideredNode[0]
    col = consideredNode[1]
    consideredNodeDepth = consideredNode[3]
        
    up = (row-1,col,consideredNode,consideredNodeDepth + 1, "up", fringeIndex)
    fringeIndex += 1
    down = (row+1,col,consideredNode,consideredNodeDepth + 1, "down", fringeIndex)
    fringeIndex += 1
    left = (row,col-1,consideredNode,consideredNodeDepth + 1, "left", fringeIndex)
    fringeIndex += 1
    right = (row,col+1,consideredNode,consideredNodeDepth + 1, "right", fringeIndex)
    fringeIndex += 1
    potentialExpand = [up,down,left,right]

    # print("Considered node:", consideredNode)
    # print("Potential expand:", potentialExpand)
    for node in potentialExpand:
        rowPos = node[0]
        colPos = node[1]

        if (rowPos < 0) or (rowPos > size[0] - 1):
            continue
        if (colPos < 0) or (colPos > size[0] - 1):
            continue
        if map[rowPos][colPos] == "X":
            continue
        if (rowPos,colPos) in closed:
            continue

        # foundDupeNode = False
        # for fringeNode in fringe:
        #     if (fringeNode[0] == rowPos) and (fringeNode[1] == colPos) and (fringeNode[2] == (row, col)):
        #         foundDupeNode = True
        #         break
        # if foundDupeNode:
        #     continue

        fringe.append(node)

    return fringe, fringeIndex

# Returns the next node to expand based on the fringe
# and the type of search we are using
def ChooseNextConsideredNode(fringe, map, maxLoops, search):
    nextNodes = fringe

    if search == "ucs":
        # Take the first fringe node's cost to start with
        minCost = maxLoops
        nextNodes = []
        for node in fringe:
            minCost = map[node[0]][node[1]]
            break
        
        # Now find the smallest cost out of all the nodes
        for node in fringe:
            cost = map[node[0]][node[1]]
            if cost < minCost:
                minCost = cost

        # Now find all nodes that have this cost
        for node in fringe:
            cost = map[node[0]][node[1]]
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
def GraphSearch(search, size, start, end, map):
    # (row, col, parent, depth, direction, index)
    start = (start[0] - 1, start[1] - 1, "startParent", 0, "startDir", -1)
    end = (end[0] - 1, end[1] - 1)
    closed = set()
    fringe = [start]
    nodesConsidered = 1
    consideredNode = start
    fringeIndex = 0
    maxLoops = 50000

    while nodesConsidered <= maxLoops:
        print("Nodes considered:", nodesConsidered)
        fringe.remove(consideredNode)
 
        outMap, isEnd = CheckIfEndNode(consideredNode, start, end, map, maxLoops)
        if isEnd:
            return outMap
        
        # Close a node as it is searched
        closed.add((consideredNode[0], consideredNode[1]))

        fringe, fringeIndex = ExpandFringe(closed, size, map, fringe, consideredNode, fringeIndex)

        if len(fringe) == 0:
            return "Fringe empty"
        
        consideredNode = ChooseNextConsideredNode(fringe, map, maxLoops, search)
        if type(consideredNode) == str:
            return consideredNode
        print("===================")
        nodesConsidered += 1

    return "Loop limit reached!"

# Prints the result
result = GraphSearch(inpSearch, inpSize, inpStart, inpEnd, inpMap)
# print("Result:")
if type(result) == str:
    print(result)
else:
    for row in result:
        printRow = ""
        for col in row:
            stringCol = str(col)
            printRow = printRow + " " + stringCol
        # Removing the first unneeded space in each row
        print(printRow[1:])