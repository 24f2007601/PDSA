"""
Dijkstra's Algorithm explanation:
This program finds the shortest path between nodes in a weighted graph.

Dijkstra's algorithm works like this:
1. Start from the source node with distance 0
2. All other nodes start with distance infinity
3. Visit the unvisited node with the smallest known distance
4. Update distances to its neighbors if a shorter path is found
5. Repeat until we reach the destination

The algorithm uses a min-heap (priority queue) to always process the nearest node first.
This is like using a GPS:
- It finds the fastest route, not necessarily the fewest turns
- It considers the weight (distance/cost) of each road
"""

import heapq

def dijkstra(WList, start):
    """
    Find the shortest paths from a starting node to all other nodes.
    
    Uses Dijkstra's algorithm with a min-heap for efficiency.
    
    Args:
        WList: A dictionary representing a weighted graph
               Keys are node indices, values are lists of (neighbor, weight) tuples
        start: The starting node for all shortest paths
        
    Returns:
        A tuple (distances, parent) where:
        - distances: A dictionary of shortest distance from start to each node
        - parent: A dictionary tracking the previous node in the shortest path
    """
    # Initialize all distances to infinity (we don't know the shortest path yet)
    distances = {node: float('inf') for node in WList}
    
    # Keep track of the parent node for path reconstruction
    parent = {node: None for node in WList}
    
    # The distance to the start node is 0
    distances[start] = 0
    
    # Priority queue: (distance, node)
    # We always process the node with the smallest known distance
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Skip if we've already found a shorter path to this node
        if current_distance > distances[current_node]:
            continue 
      
        # Check all neighbors of the current node
        for neighbour, weight in WList[current_node]:
            # Calculate the distance through the current node
            distance = current_distance + weight 
            
            # If this path is shorter than what we knew before, update it
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                parent[neighbour] = current_node
                heapq.heappush(priority_queue, (distance, neighbour))
    
    return distances, parent 
    
def reconstruct_path(parent, target):
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = parent[current]
    return path[::-1]
    
def min_cost_walk(WList, S, D, V):
    dist_from_S, parent_from_S = dijkstra(WList, S)
    dist_from_V, parent_from_V = dijkstra(WList, V)
    total_cost = dist_from_S[V] + dist_from_V[D]
    
    path_S_to_V = reconstruct_path(parent_from_S, V)
    path_V_to_D = reconstruct_path(parent_from_V, D)
    
    full_path = path_S_to_V + path_V_to_D[1:]
    
    return (total_cost, full_path)






size = int(input())
edges = eval(input())
S= int(input())
D=int(input())
V=int(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges: #for create list for undirected graph
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(min_cost_walk(WL,S, D, V))