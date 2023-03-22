import numpy as np

# Emulating an input from console
search = "bfs"
inpStart = (1,1)
inpEnd = (10,10)
size = (10,10)
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

start = (inpStart[0] - 1, inpStart[1] - 1)
end = (inpEnd[0] - 1, inpEnd[1] - 1)

# Takes a node and returns all nodes connected to it
# that aren't closed
def ConsideredNode(closed, node, size, inpMap, fringe, consideredNodes):
    nodes = []
    x = node[0]
    y = node[1]

    up = (x,y-1)
    down = (x,y+1)
    left = (x-1,y)
    right = (x+1,y)
    potentialExpand = [up,down,left,right]

    for pos in potentialExpand:
        xPos = pos[0]
        yPos = pos[1]

        if xPos < 0 or xPos > size[0] - 1:
            continue
        if yPos < 0 or yPos > size[0] - 1:
            continue
        if pos in closed:
            continue
        if inpMap[xPos][yPos] == "X":
            continue
        if pos in fringe:
            continue
        if pos in consideredNodes:
            continue

        nodes.append(pos)

    return nodes

# Returns the expanded fringe from the current one,
# one iteration of depth deeper
def ExpandFringe(search, closed, size, inpMap, fringe):
    consideredNodes = []
    for node in fringe:
        consideredNodes.update(ConsideredNode(closed, node, size, inpMap, fringe, consideredNodes))

    fringe.extend(consideredNodes)

    return fringe

def GeneratePath(inpMap, close, start, end):
    outMap = []
    # Need to make convert the closed set into a tree,
    # and add nodes to the tree as you close them
    # Then in this function, traverse the tree
    # from the end node to the start,
    # making sure you are always going up a depth level
    return outMap

# Returns true if the current node is the end node and
# sets off the generation of the path
def CheckIfEndNode(currNode, start, end, inpMap, closed):
    isEnd = False

    if currNode == end:
        isEnd = True
        closed.add(currNode)
        outMap = GeneratePath(inpMap, closed, start, end)

        return outMap, isEnd
    else:
        return None, isEnd

# Takes a search type, a grid to search, and a start and end
# and returns a path through the grid from the start
# to the goal by making "*"s along the path it found.
# Returns a string if it couldn't find a path
def GraphSearch(search, size, start, end, inpMap):
    closed = set()
    fringe = [start]
    nodesConsidered = 1
    consideredNode = start

    while nodesConsidered < 10000:
        isEnd, outMap = CheckIfEndNode(consideredNode, start, end, inpMap, closed)
        if isEnd:
            return outMap
        
        closed.add(consideredNode)

        fringe = ExpandFringe(closed, size, inpMap, fringe, consideredNode)

        if len(fringe) == 0:
            return "Fringe empty"
        
        consideredNode = ChooseNextConsideredNode(search, fringe)
        nodesConsidered += 1

    return "Loop limit reached!"

# Prints the result
result = GraphSearch(search, size, start, end, inpMap)
print("Result:")
if type(result) == str:
    print(result)
else:
    for row in result:
        print(row)