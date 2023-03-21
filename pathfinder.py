import numpy as np
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

def GetFringe(search, closed, size, currNode):
    fringe = []
    if currNode in closed:
        return "Tried to create fringe with currNode in closed!"
    else:
        fringe.append(currNode)

    x = currNode[0]
    y = currNode[1]

    up = (x,y-1)
    down = (x,y+1)
    left = (x-1,y)
    right = (x+1,y)
    potentialFringe = [up,down,left,right]

    for pos in potentialFringe:
        xPos = pos[0]
        yPos = pos[1]
        if xPos < 0 or xPos > size[0] - 1:
            continue
        if yPos < 0 or yPos > size[0] - 1:
            continue
        if pos in closed:
            continue
        fringe.append(pos)

    return fringe

def GoalTest(search, currNode, inpMap):
    
    return False

def GraphSearch(search, size, start, end, inpMap):
    outMap = inpMap
    closed = {}
    fringe = GetFringe(search, closed, size, start)
    loopCount = 0

    while loopCount < 10000:
        loopCount += 1

        if type(fringe) == "str":
            return fringe
        elif len(fringe) == 0:
            return "Fringe empty"
        
        # Remove the current node from the fringe,
        # and test if it is the end node
        currNode = fringe.pop(0)

        if GoalTest(search, currNode, inpMap):
            return outMap
        
        # if not (state[currNode] in closed):
        #     closed.add(state[currNode])
        #     fringe = InsertAll(Expand(currNode, problem), fringe)

    return "Loop limit reached!"

result = GraphSearch(search, size, start, end, inpMap)
print("Result:")
print(result)