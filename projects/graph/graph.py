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
        # Use a set to add vertex.
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Adds the edges to graph
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # Returns edges of graph based upon vertex ID.
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # For our vertices already visited.
        already = set()
        # Use queue
        queue = Queue()
        # Enqueue our starting vertex.
        queue.enqueue(starting_vertex)
        # Ensure queue size, and dequeue vertex.
        while queue.size() > 0:
            vertex = queue.dequeue()
            # If that vertex isn't in our vertices
            # already visited...
            if vertex not in already:
                # Add and print it.
                already.add(vertex)
                print(vertex)
            # Check if the edge is already in our
            # set, and queue if not.
            for edge in self.vertices[vertex]:
                if edge not in already:
                    queue.enqueue(edge)
        return already

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # For vertices already visited.
        already = set()
        # Use a stack, push our starting vertex.
        stack = Stack()
        stack.push(starting_vertex)
        # Ensure size, do same thing as in BFT.
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in already:
                print(vertex)
                already.add(vertex)
            for edge in self.vertices[vertex]:
                if edge not in already:
                    stack.push(edge)
        return already
            
    def dft_recursive(self, starting_vertex, cache=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Use a set for the cache (should only run first time)
        if cache is None:
            cache = set()
        print(starting_vertex)
        cache.add(starting_vertex)
        # For every neighbor, check if in cache, recursion.
        for i in self.get_neighbors(starting_vertex):
            if i not in cache:
                self.dft_recursive(starting_vertex=i, cache=cache)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # For our already visited vertices.
        already = {}
        # Use a queue.
        queue = Queue()
        queue.enqueue([starting_vertex, None])
        # Ensure queue size, and dequeue (vertex, prev)
        while queue.size() > 0:
            (vertex, prev) = queue.dequeue()
            # Check if in our dict of already visited vertices.
            # If we haven't...
            if vertex not in already:
                # Set our dict at the vertex to = `prev`
                already[vertex] = prev
                # If the vertex is our destination...
                if vertex == destination_vertex:
                    # Use our vertex as the step, and make an empty
                    # array to populate
                    step = vertex
                    path = []
                    # While `step` exists...
                    while step is not None:
                        # Append step to path, redefine
                        # step.
                        path.append(step)
                        step = already[step]
                    return path[::-1]
            # Traverse through edges related to vertex.
            for edge in self.vertices[vertex]:
                if edge not in already:
                    queue.enqueue((edge, vertex))

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Dict for storing already visited
        already = {}
        # Use a stack
        stack = Stack()
        stack.push([starting_vertex, None])
        # Ensure stack size; same thing as BFS, but with
        # a stack, not a queue.
        while stack.size() > 0:
            (vertex, prev) = stack.pop()
            if vertex not in already:
                already[vertex] = prev
                if vertex == destination_vertex:
                    step = vertex
                    path = []
                    while step is not None:
                        path.append(step)
                        step = already[step]

                    return path[::-1]

            for edge in self.vertices[vertex]:
                if edge not in already:
                    stack.push((edge, vertex))



    def dfs_recursive(self, starting_vertex, destination_vertex, path=None,
                      already=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Check our cache status of our already visited (should run only once)
        if already is None:
            already = set()
        # Again, should run only once.
        if path is None:
            path = []
        # Start with our starting vertex - add it to our cache.
        already.add(starting_vertex)

        # Redefine our path.
        path = path + [starting_vertex]

        # Check if we're at the proper vertex; return path if so.
        if starting_vertex == destination_vertex:
            return path

        # Recursively iterate through available neighbors.
        for i in self.get_neighbors(starting_vertex):
            if i not in already:
                new_path = self.dfs_recursive(
                    starting_vertex=i,
                    destination_vertex=destination_vertex,
                    path=path,
                    already=already,
                )

                # If there's a new path, return it.
                if new_path:
                    return new_path

        return None



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
