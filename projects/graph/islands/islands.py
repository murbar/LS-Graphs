"""
Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands)  # returns 4
"""
# graph problem?
# problem statement uses the word "connected"
# islands look like connected components
# 1.  translate input into graph terminology
# 2. build graph
# 3. traverse graph

# create visited matrix
# walk through each element in matrix
# if element not in visited
# when element == 1
# do DFT and mark each as visited
# increment counter by 1
# return island count

# need DFT function
# need get_neighbors function
