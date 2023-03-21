import numpy as np
search = "bfs"
size = [10,10]
start = [1,1]
end = [10,10]
inpMap = np.array([1, 1, 1, 1, 1, 1, 4, 7, 8, "X"],
                  [1, 1, 1, 1, 1, 1, 1, 5, 8, 8],
                  [1, 1, 1, 1, 1, 1, 1, 4, 6, 7],
                  [1, 1, 1, 1, 1, "X", 1, 1, 1, 6],
                  [1, 1, 1, 1, 1, "X", 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [6, 1, 1, 1, 1, "X", 1, 1, 1, 1],
                  [7, 7, 1, "X", "X", "X", 1, 1, 1, 1],
                  [8, 8, 1, 1, 1, 1, 1, 1, 1, 1],
                  ["X", 8, 7, 1, 1, 1, 1, 1, 1, 1])
def CreateFringe(search, node, closed, inpMap):
    fringe = []
    if node in closed:
        return fringe
    x = node[0]
    y = node[1]

    up = inpMap[x,y-1]
    down = inpMap[x,y+1]
    left = inpMap[x-1,y]
    right = inpMap[x+1,y]
    potentialFringe = [up,down,left,right]
    print(potentialFringe)
    return fringe

def GraphSearch(search, size, start, end, inpMap):
    outMap = inpMap
    closed = {}
    fringe = CreateFringe(search, start, closed, inpMap)
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
if not result:
    print("null")
else:
    print(result)