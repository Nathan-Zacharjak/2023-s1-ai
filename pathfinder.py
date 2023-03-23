import numpy as np

# Emulating an input from console
inpSearch = "bfs"
inpStart = (1,1)
inpEnd = (10,10)
inpSize = (10,10)
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

def GeneratePath(map, closed, start, end):
    loopCount = 0
    currentNode = end

    while loopCount < 10000:
        loopCount += 1

        # Current node stuff
        row = currentNode[0]
        col = currentNode[1]
        map[row][col] = "*"
        if (row == start[0]) and (col == start[1]):
            return map

        # Parent node stuff
        parentNode = closed[(row, col)]
        parentRow = parentNode[0]
        parentCol = parentNode[1]
        currentNode = (parentRow, parentCol)

    if loopCount == 10000:
        return "Generate path loop count limit reached!"
    
    return map

# Returns true if the current node is the end node and
# sets off the generation of the path
def CheckIfEndNode(consideredNode, start, end, map, closed):
    rowPos = consideredNode[0]
    colPos = consideredNode[1]
    print("is consideredNode end:", consideredNode, end, rowPos == end[0], colPos == end[1])

    if (rowPos == end[0]) and (colPos == end[1]):
        outMap = GeneratePath(map, closed, start, end)

        return outMap, True
    else:
        return None, False

# Takes a node and finds all nodes connected to it,
# that can be added to the fringe,
# and returns the extended fringe
def ExpandFringe(closed, size, map, fringe, consideredNode):
    row = consideredNode[0]
    col = consideredNode[1]
    consideredNodeDepth = consideredNode[3]

    up = (row-1,col,(row,col),consideredNodeDepth + 1, "up")
    down = (row+1,col,(row,col),consideredNodeDepth + 1, "down")
    left = (row,col-1,(row,col),consideredNodeDepth + 1, "left")
    right = (row,col+1,(row,col),consideredNodeDepth + 1, "right")
    potentialExpand = [up,down,left,right]

    print("Considered node:", consideredNode)
    print("Potential expand:", potentialExpand)
    for node in potentialExpand:
        rowPos = node[0]
        colPos = node[1]

        if rowPos < 0 or rowPos > size[0] - 1:
            continue
        if colPos < 0 or colPos > size[0] - 1:
            continue
        if map[rowPos][colPos] == "X":
            continue
        if (rowPos, colPos) in closed:
            continue

        foundDupeNode = False
        for fringeNode in fringe:
            if (fringeNode[0] == rowPos) and (fringeNode[1] == colPos):
                foundDupeNode = True
                break
        if foundDupeNode:
            continue

        fringe.add(node)

    print("Fringe:", fringe)
    return fringe

# Returns the next node to expand based on the fringe
# and the type of search we are using
def ChooseNextConsideredNode(fringe):
    # Take the first fringe node's depth to start with
    minDepth = 10000
    nextNodes = set()
    for node in fringe:
        minDepth = node[3]
        break
    
    # Now find the smallest depth out of all the nodes
    for node in fringe:
        depth = node[3]
        if depth < minDepth:
            minDepth = depth

    # Now find all nodes that have this depth
    for node in fringe:
        depth = node[3]
        if depth == minDepth:
            nextNodes.add(node)
    print("optimal nodes:", nextNodes)
    # Now from all these equally optimal nodes,
    # apply the "up, down, left right" priority to resolve a tie,
    # if there is more than 1 node in the potential nextNodes[]

    upNodes = set()
    downNodes = set()
    leftNodes = set()
    rightNodes = set()
    for node in nextNodes:
        if node[4] == "up":
            upNodes.add(node)
        elif node[4] == "down":
            downNodes.add(node)
        elif node[4] == "left":
            leftNodes.add(node)
        elif node[4] == "right":
            rightNodes.add(node)
        
    if len(upNodes) > 0:
        nextNodes = upNodes
    elif len(downNodes) > 0:
        nextNodes = downNodes
    elif len(leftNodes) > 0:
        nextNodes = leftNodes
    elif len(rightNodes) > 0:
        nextNodes = rightNodes

    print("Next considered node:", nextNodes)
    if len(nextNodes) == 0:
        return "nextNodes set is empty!"
    else:
        return nextNodes.pop()


# Takes a search type, a grid to search, and a start and end
# and returns a path through the grid from the start
# to the goal by making "*"s along the path it found.
# Returns a string if it couldn't find a path
def GraphSearch(search, size, start, end, map):
    # (row, col, Parent, Depth)
    start = (start[0] - 1, start[1] - 1, "start", 0, "start")
    end = (end[0] - 1, end[1] - 1)
    closed = {}
    fringe = {start}
    nodesConsidered = 1
    consideredNode = start

    while nodesConsidered <= 10000:
        print("Nodes considered:", nodesConsidered)
        closed[(consideredNode[0], consideredNode[1])] = consideredNode[2]
        fringe.remove(consideredNode)

        outMap, isEnd = CheckIfEndNode(consideredNode, start, end, map, closed)
        if isEnd:
            return outMap

        fringe = ExpandFringe(closed, size, map, fringe, consideredNode)

        if len(fringe) == 0:
            return "Fringe empty"
        
        consideredNode = ChooseNextConsideredNode(fringe)
        if type(consideredNode) == str:
            return consideredNode
        print("===================")
        nodesConsidered += 1

    return "Loop limit reached!"

# Prints the result
result = GraphSearch(inpSearch, inpSize, inpStart, inpEnd, inpMap)
print("Result:")
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