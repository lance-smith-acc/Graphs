from graph import Graph

def earliest_ancestor(ancestors, starting_node):
# Take in a list of pairs(parent, child)
# Each pair is assigned a unique identifier(int)
# Given the dataset and an ID,
# Return an id that is the furthest from the given ID
# If there is a tie, return the lowest numeric id
# If there are no parents, the function should return -1

    # Create a list of our vertices to traverse through
    vertices = list(set([y for x in ancestors for y in x]))
    # Create a graph to search
    graph = Graph()

    # Add the parents/children to the graph
    for pair in ancestors:
        graph.add_vertex(pair[1])
        graph.add_vertex(pair[0])
    # Direct the parents to the children
    for pair in ancestors:
        graph.add_edge(pair[1], pair[0])

    # Track our paths
    paths = []
    # For each vertice, search for the farthest away and add the search path to paths
    for v in vertices:
        if v != starting_node and graph.dfs(starting_node, v):
            paths.append(graph.dfs(starting_node, v))

    # If no paths were found for the starting node
    if len(paths) < 1:
        return -1
    else:
        # Returns the last value on the longest list of paths, the earliest ancestor
        return max(paths, key=len)[-1]

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 4))