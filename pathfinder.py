import numpy as np

# Emulating an input from console
inpSearch = "bfs"
inpStart = (1,1)
inpEnd = (10,10)
inpSize = (10,10)
inpMap = [[1, 2, 1, 1, 1, 1, 4, 7, 8, "X"],
        [3, 4, 1, 1, 1, 1, 1, 5, 8, 8],
        [1, 1, 1, 1, 1, 1, 1, 4, 6, 7],
        [1, 1, 1, 1, 1, "X", 1, 1, 1, 6],
        [1, 1, 1, 1, 1, "X", 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [6, 1, 1, 1, 1, "X", 1, 1, 1, 1],
        [7, 7, 1, "X", "X", "X", 1, 1, 1, 1],
        [8, 8, 1, 1, 1, 1, 1, 1, 1, 1],
        ["X", 8, 7, 1, 1, 1, 1, 1, 1, 1]]

def GeneratePath(map, close, start, end):
    outMap = []
    # Use closed set as dicionary, index by end, get its parent, index parent, etc. until start is reached and star along the way
    return outMap

# Returns true if the current node is the end node and
# sets off the generation of the path
def CheckIfEndNode(currNode, start, end, map, closed):
    isEnd = False

    if currNode == end:
        isEnd = True
        closed.add(currNode)
        outMap = GeneratePath(map, closed, start, end)

        return outMap, isEnd
    else:
        return None, isEnd

# Takes a node and finds all nodes connected to it,
# that can be added to the fringe,
# and returns the extended fringe
def ExpandFringe(closed, size, map, fringe, consideredNode):
    x = consideredNode[0]
    y = consideredNode[1]
    consideredNodeDepth = consideredNode[3]

    up = (x,y-1,(x,y),consideredNodeDepth + 1, "up")
    down = (x,y+1,(x,y),consideredNodeDepth + 1, "down")
    left = (x-1,y,(x,y),consideredNodeDepth + 1, "left")
    right = (x+1,y,(x,y),consideredNodeDepth + 1, "right")
    potentialExpand = [up,down,left,right]

    for node in potentialExpand:
        xPos = node[0]
        yPos = node[1]

        if xPos < 0 or xPos > size[0] - 1:
            continue
        if yPos < 0 or yPos > size[0] - 1:
            continue
        if map[xPos][yPos] == "X":
            continue
        if (xPos, yPos) in closed:
            continue

        foundDupeNode = False
        for fringeNode in fringe:
            if (fringeNode[0] == xPos) and (fringeNode[1] == yPos):
                foundDupeNode = True
                break
        if foundDupeNode:
            continue

        fringe.add(node)

    return fringe

# Returns the next node to expand based on the fringe
# and the type of search we are using
def ChooseNextConsideredNode(search, fringe, consideredNode):
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
    
    # Now from all these equally optimal nodes,
    # apply the "up, down, left right" priority to resolve a tie,
    # if there is more than 1 node in the potential nextNodes[]
    while len(nextNodes) > 1:
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

    if len(nextNodes) == 0:
        return "nextNodes set is empty!"
    else:
        return nextNodes.pop()


# Takes a search type, a grid to search, and a start and end
# and returns a path through the grid from the start
# to the goal by making "*"s along the path it found.
# Returns a string if it couldn't find a path
def GraphSearch(search, size, start, end, map):
    # (X, Y, Parent, Depth)
    start = (start[0] - 1, start[1] - 1, "start", 0, "start")
    end = (end[0] - 1, end[1] - 1)
    closed = {}
    fringe = {start}
    nodesConsidered = 1
    consideredNode = start

    while nodesConsidered < 10000:
        closed[(consideredNode[0], consideredNode[1])] = consideredNode[2]
        fringe.remove(consideredNode)

        isEnd, outMap = CheckIfEndNode(consideredNode, start, end, map, closed)
        if isEnd:
            return outMap

        fringe = ExpandFringe(closed, size, map, fringe, consideredNode)

        if len(fringe) == 0:
            return "Fringe empty"
        
        consideredNode = ChooseNextConsideredNode(search, fringe, consideredNode)
        if type(consideredNode) == str:
            return consideredNode
        
        nodesConsidered += 1

    return "Loop limit reached!"

# Prints the result
result = GraphSearch(inpSearch, inpSize, inpStart, inpEnd, inpMap)
print("Result:")
if type(result) == str:
    print(result)
else:
    for row in result:
        print(row)