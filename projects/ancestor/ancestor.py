# Nodes will be people
# Edges will be child-parent relationship
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    # Add nodes and edges.
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(parent, child)

    earliest_ancestor = None

    longest_path = 1

    for vertex in graph.vertices:
        # Using depth first search.
        path = graph.dfs(vertex, starting_node)

        # Check if continue search.
        if path:
            # If we have a longer path, redefine earliest ancestor
            # (and make it our new longest path)
            if len(path) > longest_path:
                longest_path = len(path)
                earliest_ancestor = vertex

        # If no match has been found, return -1.
        elif not path and longest_path == 1:
            earliest_ancestor = -1

    return earliest_ancestor