"""
Negative weight cycle detection explanation:
This program checks if a weighted directed graph contains a negative weight cycle.
A negative weight cycle is a cycle where the sum of all edge weights is negative.

The Bellman-Ford algorithm is used:
1. Initialize all distances from a source vertex to infinity (a very large number)
2. Relax all edges (V-1) times where V is the number of vertices
3. Check for negative cycles by trying to relax edges one more time
   If any distance can still be improved, a negative cycle exists!
"""


def IsNegativeWeightCyclePresent(WList):
    # Step 1: Create a list of all vertices
    vertices = list(WList.keys())
    
    # Step 2: Pick a starting vertex (we use vertex 0)
    start_vertex = 0
    
    # Step 3: Calculate a very large number (infinity) for initialization
    # This ensures any real distance will be smaller than this initial value
    infinity = 1 + len(vertices) * max([d for u in vertices for (v, d) in WList[u]])
    
    # Step 4: Create a distance dictionary and set all distances to infinity
    distance = {}
    for v in vertices:
        distance[v] = infinity
    # Set the distance to the starting vertex as 0
    distance[start_vertex] = 0
    
    # Step 5: Relax all edges (V-1) times
    # V is the number of vertices, so we loop (V-1) times
    for i in range(len(vertices) - 1):
        # For each vertex u in the graph
        for u in vertices:
            # For each neighbor v of vertex u with edge weight d
            for (v, d) in WList[u]:
                # If going from u to v gives a shorter path than current distance to v
                # update the distance to v
                if distance[u] + d < distance[v]:
                    distance[v] = distance[u] + d
    
    # Step 6: Check for negative weight cycles
    # Try to relax all edges one more time
    # If any distance can still be improved, there's a negative cycle!
    for u in vertices:
        for (v, d) in WList[u]:
            # If we can still make the distance to v smaller,
            # it means there's a negative weight cycle
            if distance[u] + d < distance[v]:
                return True
    
    # If no negative cycle was found, return False
    return False


# Input: Read the number of vertices
size = int(input())

# Input: Read the list of edges as (from_vertex, to_vertex, weight)
edges = eval(input())

# Build the adjacency list representation of the graph
WL = {}
for i in range(size):
    WL[i] = []

for ed in edges:
    # ed[0] is from vertex, ed[1] is to vertex, ed[2] is weight
    WL[ed[0]].append((ed[1], ed[2]))

# Call the function and print the result
print(IsNegativeWeightCyclePresent(WL))