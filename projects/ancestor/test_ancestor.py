from ancestor import earliest_ancestor

graph = {
    1: {3},
    2: {3},
    3: {6},
    5: {6, 7},
    4: {5, 8},
    8: {9},
    11: {8},
    10: {1}
}

print(earliest_ancestor(graph, 6))  # -> 10
