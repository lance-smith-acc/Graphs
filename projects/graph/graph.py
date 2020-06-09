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
        self.vertices[vertex_id] = set() # set of eges from this vert

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)

        # Create a set for visited neighbors
        visited = set()

        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()

            # if the vertex hasn't been visited
            if v not in visited:
                # Visit it
                print(v)

                # mark it as visted
                visited.add(v)

                # Add all its neighbors to the queue
                for nextV in self.get_neighbors(v):
                    q.enqueue(nextV)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)

        # Create a set for visited neighbors
        visited = set()

        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()

            # if the vertex hasn't been visited
            if v not in visited:
                # Visit it
                print(v)

                # mark it as visted
                visited.add(v)

                # Add all its neighbors to the stack
                for nextV in self.get_neighbors(v):
                    s.push(nextV)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Add the current vertex to visited
        visited.add(starting_vertex)
        # Visit it
        print(starting_vertex)
        
        # For each neighbor, recur
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor in visited:
                return
            else:
                self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])

        visited = set()

        while q.size() > 0:
            # Set the path
            path = q.dequeue()
            # Note the last visited in our path
            last_vert = path[-1]
            # If we haven't visited our last vertex in the path
            if last_vert not in visited:
                # If the last vert is our target, we're done
                if last_vert == destination_vertex:
                    return path

                # Otherwise, visit the last vert
                else:
                    visited.add(last_vert)
                    # Start visitng neighbors
                    for n in self.get_neighbors(last_vert):
                        path_copy = list(path)
                        path_copy.append(n)
                        q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])

        visited = set()

        while s.size() > 0:

            path = s.pop()
            last_vert = path[-1]

            if last_vert not in visited:

                if last_vert == destination_vertex:
                    return path

                else:
                    visited.add(last_vert)

                    for n in self.get_neighbors(last_vert):
                        path_copy = list(path)
                        path_copy.append(n)
                        s.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Create a set of the current path
        cur_path = path.copy()
        # Add the current vert to the path
        cur_path.append(starting_vertex)
        
        if starting_vertex not in visited:
            # Visit the current vert
            visited.add(starting_vertex)
            # If we found it, we're done
            if starting_vertex == destination_vertex:
                return cur_path
            # Otherwise, start visiting neighbors
            else:
                for neighbor in self.get_neighbors(starting_vertex):
                    # Update the path and neighbors and recur
                    next_path = self.dfs_recursive(neighbor, destination_vertex, visited, cur_path)
                    # Keep going until we run out of verts
                    if next_path is not None:
                        return next_path

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
