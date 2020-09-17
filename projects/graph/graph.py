"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from collections import deque

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        #empty dictionary
        self.vertices = {}
    #method
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        #make sure we dont add a vertex if already in graph
        if vertex_id not in self.vertices:
            #add a key and have an empty set
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        #check to make sure vertices are in graph
        if v1 in self.vertices and v2 in self.vertices:
            #add edge
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        
        return self.vertices[vertex_id] if vertex_id in self.vertices else set()

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #make a queue
        queue = deque()
        #starting node (we can start anywhere)
        queue.append(starting_vertex)
        #make a set to track this
        visited = set()

        #while our queue is not empty
        while len(queue) > 0:
            #pop whatever is at the front of our line, this is our current node
            currNode = queue.popleft()

            #if we haven't visited this node yet
            if currNode not in visited:
                #mark as visited
                visited.add(currNode)
                print(currNode)
                #for each of the neighbors
                for neighbor in self.get_neighbors(currNode):
                    #add to the queue
                    queue.append(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #make a stack
        stack = deque()
        #starting node
        stack.append(starting_vertex)
        #make a set to track this
        visited = set()
        while len(stack) > 0:
            currNode = stack.pop()
            if currNode not in visited:
                visited.add(currNode)
                print(currNode)
                for neighbor in self.get_neighbors(currNode):
                    stack.append(neighbor)

    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #if node has not been visited
        if starting_vertex not in visited:
            #mark as visited
            visited.add(starting_vertex)
            #print
            print(starting_vertex)
            #for each of node's neihgbors
            for neighbor in self.vertices[starting_vertex]:
                #recurse
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = deque()
        queue.append([starting_vertex])
        visited = set()
        while len(queue) > 0 :
            currPath = queue.popleft()
            currNode = currPath[-1]
            if currNode == destination_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neighbor in self.get_neighbors(currNode):
                    newPath = list(currPath)
                    newPath.append(neighbor)
                    queue.append(newPath)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = deque()
        stack.append([starting_vertex])
        visited = set()
        while len(stack) > 0 :
            currPath = stack.pop()
            currNode = currPath[-1]
            if currNode == destination_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neighbor in self.get_neighbors(currNode):
                    newPath = list(currPath)
                    newPath.append(neighbor)
                    stack.append(newPath)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = set(), path = []):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        #add the starting node in the visited set
        visited.add(starting_vertex)
        #add the node in path
        path = path + [starting_vertex]
        #base case
        #is the node our target?
        if starting_vertex == destination_vertex:
            #if yes, return
            return path
        #for each node's neigbhor
        for neighbor in self.get_neighbors(starting_vertex):
            #is the node visited
            if neighbor not in visited:
                #if no, recure and get the new path
                newPath = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                #is the new path None?
                if newPath is not None:
                    #if not none, return
                    return newPath

        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    print("++++++++++++++")
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)
    print("+++++++++++++")
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    
    graph.dft(1)
    print("++++++++")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
