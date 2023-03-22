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
def ExpandNode(closed, node, size, inpMap):
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

        nodes.append(pos)

    return nodes

# Returns the fringe from a specified depth
def GetFringe(search, closed, size, start, inpMap, fringe):
    

    return fringe

# Marks off a node as explored by changing it to a "*"
# Returns true if the current node is the goal node
def GoalTest(currNode, outMap, end):
    isGoalNode = False
    if currNode == end:
        isGoalNode = True

    outMap[currNode[0]][currNode[1]] = "*"

    return outMap, isGoalNode

def SelectNextNode(fringe, search):

            
    return nextNode

# Takes a search type, a grid to search, and a start and end
# and returns a path through the grid from the start
# to the goal by making "*"s along the path it found.
# Returns a string if it couldn't find a path
def GraphSearch(search, size, start, end, inpMap):
    outMap = inpMap
    closed = set()
    depth = 0
    fringe = []
    fringe = GetFringe(search, closed, size, start, inpMap, depth, fringe)

    while depth < 10000:
        depth += 1

        if type(fringe) == str:
            return fringe
        elif len(fringe) == 0:
            return "Fringe empty"
        
        # Remove the current node from the fringe,
        # and test if it is the end node
        currNode = fringe.pop(0)

        outMap, goalReached = GoalTest(currNode, outMap, end)
        if goalReached:
            return outMap
        
        closed.add(currNode)
        currNode = SelectNextNode(fringe, search)
        fringe = GetFringe(closed, size, start, inpMap)

    return "Loop limit reached!"

# Prints the result
result = GraphSearch(search, size, start, end, inpMap)
print("Result:")
if type(result) == str:
    print(result)
else:
    for row in result:
        print(row)