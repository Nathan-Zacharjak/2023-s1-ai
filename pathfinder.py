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

def CreateFringe(search, closed, size, node):
    fringe = []
    if node in closed:
        return fringe
    x = node[0]
    y = node[1]

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

def GraphSearch(search, size, start, end, inpMap):
    outMap = inpMap
    closed = {}
    fringe = CreateFringe(search, closed, size, start)
    print("Fringe:",fringe)
    loopCount = 0

    # while loopCount < 10000:
    #     loopCount += 1
    #     if len(fringe) == 0:
    #         return False
        
        # node = RemoveFront(fringe)

        # if GoalTest(problem, state[node]):
        #     return outMap
        
        # if not (state[node] in closed):
        #     closed.add(state[node])
        #     fringe = InsertAll(Expand(node, problem), fringe)

result = GraphSearch(search, size, start, end, inpMap)
print("Result:")
if not result:
    print("null")
else:
    print(result)