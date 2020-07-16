"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue and enqueue starting vertex
        que = Queue()
        que.enqueue([starting_vertex])
        # create a set of traversed vertices
        visited = set()
        # while queue is not empty
        while que.size() > 0:
            # dequeue/pop the first vertex
            path = que.dequeue()
            if path[-1] not in visited:
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    que.enqueue(new_path)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push([starting_vertex])
        # create a set of traversed vertices
        visited = set()
        # while queue is not empty
        while stack.size() > 0:
            # dequeue/pop the first vertex
            path = stack.pop()
            if path[-1] not in visited:
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        # Track visited nodes
        visited.add(starting_vertex)
        print(starting_vertex)
        # Call the function recursively - on neighbors not visited 
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
                # if a node has no unvisited neighbors, do nothing
                # essentially a base case

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While the queue is not empty
        while q.size() > 0:
            # dequeue/pop the first vertex
            path = q.dequeue()
            # if not visited
            if path[-1] not in visited:
                # Do what you want to each one
                if path[-1] == destination_vertex:
                    return path
                # mark as visited
                visited.add(path[-1])
                # enqueue all it's neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    q.enqueue(new_path)
            # Function will return None if destination not found

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a queue and enqueue the starting vertex
        ss = Stack()
        ss.push([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While the queue is not empty
        while ss.size() > 0:
            # dequeue/pop the first vertex
            path = ss.pop()
            # if not visited
            if path[-1] not in visited:
                if path[-1] == destination_vertex:
                    return path
                # mark as visited
                visited.add(path[-1])
                # add all it's neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path) # lists pass by reference and would change all paths
                    new_path.append(next_vert)
                    ss.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
            
        if path is None:
            path = []

        if starting_vertex not in visited:
            #Track visited nodes
            visited.add(starting_vertex)
            copy = path.copy()
            copy.append(starting_vertex)
            if starting_vertex == destination_vertex:
                return copy
            for next_v in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(
                    next_v, destination_vertex, visited, copy)
                if new_path is not None:
                    return new_path

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

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
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
