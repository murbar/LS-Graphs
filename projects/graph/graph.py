"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Add least one specified vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        path = []
        visited = set()
        to_visit = Queue()
        to_visit.enqueue(starting_vertex)

        while to_visit.size() > 0:
            vertex = to_visit.dequeue()
            if vertex not in visited:
                visited.add(vertex)
                path.append(vertex)
                for neighbor in self.vertices[vertex]:
                    to_visit.enqueue(neighbor)

        print(path)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        path = []
        visited = set()
        to_visit = Stack()
        to_visit.push(starting_vertex)

        while to_visit.size() > 0:
            vertex = to_visit.pop()
            if vertex not in visited:
                visited.add(vertex)
                path.append(vertex)
                for neighbor in self.vertices[vertex]:
                    to_visit.push(neighbor)

        print(path)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        path = []
        visited = set()

        def traverse(vertex, visited):
            if vertex in visited:
                return
            visited.add(vertex)
            path.append(vertex)
            for neighbor in self.vertices[vertex]:
                traverse(neighbor, visited)

        traverse(starting_vertex, visited)
        print(path)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty set to store visited nodes
        # Create an empty Queue and enqueue A PATH TO the starting vertex
        # While the queue is not empty...
        # Dequeue the first PATH
        # GRAB THE VERTEX FROM THE END OF THE PATH
        # IF VERTEX = TARGET, RETURN PATH
        # If that vertex has not been visited...
        # Mark it as visited
        # Then add A PATH TO all of its neighbors to the back of the queue
        # Copy the path
        # Append neighbor to the back of the copy
        # Enqueue copy

        visited = set()
        paths = Queue()
        paths.enqueue([starting_vertex])

        while paths.size() > 0:
            path = paths.dequeue()
            last_index = len(path) - 1
            vertex = path[last_index]
            if vertex == destination_vertex:
                return path
            if vertex not in visited:
                visited.add(vertex)
                neighbors = self.vertices[vertex]
                for n in neighbors:
                    next_path = path.copy()
                    next_path.append(n)
                    paths.enqueue(next_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        path = []
        visited = set()
        to_visit = Stack()
        to_visit.push(starting_vertex)

        while to_visit.size() > 0:
            vertex = to_visit.pop()
            if vertex == destination_vertex:
                path.append(vertex)
                return path
            if vertex not in visited:
                visited.add(vertex)
                path.append(vertex)
                for neighbor in self.vertices[vertex]:
                    to_visit.push(neighbor)


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
    print('Vertices:')
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('Depth traversal:')
    graph.dft(1)

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
    print('Breadth traversal:')
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('Depth traversal, recursive:')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('Breadth search:')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('Depth search:')
    print(graph.dfs(1, 6))
