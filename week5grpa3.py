"""
Negative weight cycle detection explanation:
This program checks if a weighted directed graph contains a negative weight cycle.
A negative weight cycle is a cycle where the sum of all edge weights is negative.

The Bellman-Ford algorithm is used:
1. Initialize all distances from a source vertex to infinity (a very large number)
2. Relax all edges (V-1) times where V is the number of vertices
3. Check for negative cycles by trying to relax edges one more time
   If any distance can still be improved, a negative cycle exists!

This is useful for:
- Detecting price arbitrage opportunities in currency exchange
- Finding if there are any impossible situations in routing (like negative costs)
"""


def IsNegativeWeightCyclePresent(WList):
    """
    Check if the graph contains a negative weight cycle.
    
    Uses the Bellman-Ford algorithm to detect negative cycles.
    
    Args:
        WList: A dictionary representing a weighted directed graph
               Keys are node indices, values are lists of (neighbor, weight) tuples
               
    Returns:
        True if a negative weight cycle exists, False otherwise
    """
    # Get list of all vertices in the graph
    vertices = list(WList.keys())
    
    # Pick a starting vertex (using the first vertex)
    start_vertex = 0
    
    # Step 1: Calculate infinity (a number larger than any possible path)
    # This is the maximum weight times number of vertices, plus 1
    infinity = 1 + len(vertices) * max([d for u in vertices for (v, d) in WList[u]])
    
    # Step 2: Initialize all distances to infinity, except the start vertex
    distance = {}
    for v in vertices:
        distance[v] = infinity
    distance[start_vertex] = 0  # Distance to start is 0
    
    # Step 3: Relax all edges (V-1) times
    # After this, all shortest paths should be found (if no negative cycles)
    for i in range(len(vertices) - 1):
        for u in vertices:
            for (v, d) in WList[u]:
                # If going through u gives a shorter path to v, update v's distance
                if distance[u] + d < distance[v]:
                    distance[v] = distance[u] + d
    
    # Step 4: Check for negative cycles
    # Try to relax one more time - if we can still improve, there's a negative cycle!
    for u in vertices:
        for (v, d) in WList[u]:
            # If we can still find a shorter path, there's a negative cycle
            if distance[u] + d < distance[v]:
                return True
    
    # No negative cycle found
    return False


# Input: number of vertices
size = int(input())

# Input: list of edges as (from, to, weight)
edges = eval(input())

# Build the weighted directed graph
WL = {}
for i in range(size):
    WL[i] = []

for ed in edges:
    # ed[0] is from vertex, ed[1] is to vertex, ed[2] is weight
    WL[ed[0]].append((ed[1], ed[2]))
    
# Check and print whether a negative weight cycle exists
print(IsNegativeWeightCyclePresent(WL))