

"""

1. Translate the problem into graph terminology:
vertex = Individual
edges = relationship from one individual to another individual, in this case one directional and = parent. 
weights = None needed

2. build your graph: child: {parent pairs}
{   
    11: {}
    10 : {},
    9 : {8},
    8 : {4,11},
    7 :{5},
    6: {3,5},
    5: {4},
    4: {},
    3: {1,2},
    2: {},
    1: {10}
}

3. Traverse your graph:
BFT will work.   Can start from any vertex.
 -return the earliest known ancestor
 - If there is more than one ancestor tied to “earliest”, return the one with the lowest 
 numeric ID. +++ i am using BFT - so the last ancestor found is always the earliest+++
 -If the input individual has no parents, the function should return -1.

"""

from collections import deque

def createGraph(ancestors):
    graph = {}
    for edge in ancestors:
        child, parent = edge[1], edge[0]
    
        if child in graph:
            graph[child].add(parent)
        else:
            graph[child] = {parent}
    return graph
    

def earliest_ancestor(ancestors, starting_node):
    if len(ancestors) == 0:
        return ''
    graph = createGraph(ancestors) 
    #make a queue
    queue = deque()
    #starting node (we can start anywhere)
    queue.append(starting_node)
    #make a set to track this
    visited = set()
    
    #return -1 if starting node does not have any parents
    if starting_node not in graph:
        return -1
    #while our queue is not empty
    while len(queue) > 0:
        #pop whatever is at the front of our line, this is our current node
        curr = queue.popleft()
        #if we haven't visited this node yet
        if curr not in visited:
            #mark as visited
            visited.add(curr)
            print(curr)

            #for each of the neighbors
            for neighbor in graph[curr]:
                if neighbor in graph:
                    queue.append(neighbor)
    
                        
    return neighbor




            
if __name__ == '__main__':
    ancestors = [(1,3),(2,3),(3, 6),(5 ,6),(5 ,7),(4, 5), (4 ,8),(8, 9), (11, 8), (10 ,1)]
    print(earliest_ancestor(ancestors,10))