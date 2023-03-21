import numpy as np

def GraphSearch(problem, fringe):
    closed = {}
    fringe = Insert(MakeNode(initialState[problem]), fringe)
    loopCount = 0
    
    while loopCount < 10000:
        loopCount += 1
        if len(fringe) == 0:
            return False
        
        node = RemoveFront(fringe)

        if GoalTest(problem, state[node]):
            return node
        
        if not (state[node] in closed):
            closed.add(state[node])
            fringe = InsertAll(Expand(node, problem), fringe)

# GraphSearch()