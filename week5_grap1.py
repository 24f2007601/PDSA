"""
Kruskal's Algorithm explanation:
This program finds the minimum spanning tree (MST) of a weighted graph using Kruskal's algorithm.

How Kruskal's algorithm works:
1. Sort all edges by their weight (distance)
2. Start with each city as its own separate component
3. Add edges from shortest to longest
4. Skip an edge if it would create a cycle (connect two cities already in the same component)
5. Stop when all cities are connected

This is like laying fiber optic cables:
- Connect cities with the shortest possible cables first
- But don't create redundant connections (that would be a cycle)

Union-Find (Disjoint Set Union) is used to track which cities are already connected.
"""


def kruskal(WList):
    """
    Find the minimum spanning tree using Kruskal's algorithm.
    
    Args:
        WList: A dictionary representing a weighted undirected graph
               Keys are city indices, values are lists of (neighbor, distance) tuples
               
    Returns:
        A list of edges (tuples) that form the minimum spanning tree
    """
    # Step 1: Get all edges from the graph
    # Each edge is represented as (distance, from_city, to_city)
    edges = []
    component = {}  # Track which component each city belongs to
    
    for u in WList.keys():
        # Add all edges from city u
        edges.extend([(d, u, v) for (v, d) in WList[u]])
        # Initially, each city is in its own component
        component[u] = u
    
    # Step 2: Sort edges by distance (shortest first)
    edges.sort()
    
    # Step 3: Process edges in order
    TE = []  # Tree Edges - will contain our MST
    
    for (d, u, v) in edges:
        # Check if u and v are in different components
        if component[u] != component[v]:
            # Add this edge to our tree (connects two different components)
            TE.append((u, v))
            
            # Merge the two components
            # All cities in u's component now belong to v's component
            c = component[u]
            for w in WList.keys():
                if component[w] == c:
                    component[w] = component[v]
    
    return TE


def FiberLink(distance_map):
    """
    Calculate the total cost of the minimum fiber network.
    
    Args:
        distance_map: A dictionary representing the distances between cities
        
    Returns:
        The total minimum cost to connect all cities
    """
    # Get the minimum spanning tree edges
    R = kruskal(distance_map)
    
    # Calculate the total cost by summing up the distances of MST edges
    S = 0
    for e in R:
        # Find the distance for this edge
        for ed in distance_map[e[0]]:
            if ed[0] == e[1]:
                S += ed[1]
                break
    
    return S


# Input: number of cities (nodes)
size = int(input())

# Input: list of edges as (from, to, distance)
edges = eval(input())

# Build the weighted graph (undirected - roads go both ways)
WL = {}
for i in range(size):
    WL[i] = []

for ed in edges:
    WL[ed[0]].append((ed[1], ed[2]))
    WL[ed[1]].append((ed[0], ed[2]))

# Calculate and print the minimum fiber cost
print(FiberLink(WL))