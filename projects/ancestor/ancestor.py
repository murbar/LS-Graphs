# unweighted, directed, acyclic graph

# depth first traversal (stack)
# traversing backwards
# traverse up until no parents
# keep track of paths
# return last element of longest path

# need get_parents function


def get_parents(vertex, graph):
    # for larger graphs it may be better to rebuild the graph up-front with vertex-parent relationships
    parents = []
    for v, children in graph.items():
        if vertex in children:
            parents.append(v)
    return parents


def earliest_ancestor(graph, vertex):
    """Returns the ancestor with the farthest distance and lowest
       numeric ID from the supplied vertex. If none is found, returns -1."""

    visited = set()
    paths_stack = []
    paths_stack.append([vertex])
    terminating_paths = []

    while paths_stack:
        candidate_path = paths_stack.pop()
        vertex = candidate_path[-1]
        if vertex not in visited:
            visited.add(vertex)
            parents = get_parents(vertex, graph)
            if not parents and len(candidate_path) > 1:
                terminating_paths.append(candidate_path)
            for p in parents:
                next_path = candidate_path.copy()
                next_path.append(p)
                paths_stack.append(next_path)

    if not terminating_paths:
        return -1

    longest_path_len = max([len(p) for p in terminating_paths])
    earliest_ancestors = [p[-1]
                          for p in terminating_paths if len(p) == longest_path_len]
    return min(earliest_ancestors)
