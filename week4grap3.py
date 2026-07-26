"""
Longest journey explanation:
This program finds the longest route in a directed graph using a topological-style traversal.
It builds a path from each city to its neighbors and keeps the longest path seen so far.

This is useful for problems where you want the longest valid sequence of connected cities.

Key concept: Topological Sort
- In a directed graph, topological order ensures we process nodes in a valid sequence
- A node with in-degree 0 has no prerequisites (no incoming edges)
- We can only reach a city after we've processed all cities that point to it
"""


def longJourney(AList):
    """
    Find the longest path in a directed graph.
    
    This uses dynamic programming combined with topological sorting:
    1. First, we find nodes with no incoming edges (starting points)
    2. Process nodes in topological order
    3. Keep track of the longest path to each node
    
    Args:
        AList: A dictionary representing a directed graph
               Keys are city names, values are lists of cities they can reach
        
    Returns:
        A list representing the longest route (path) through the graph
    """
    # Normalize names so different cases are treated the same
    # (e.g., "CityA" and "citya" should be treated as the same city)
    name_map = {city.lower(): city for city in AList}

    # Rebuild the adjacency list with consistent exact names
    graph = {}
    for city in AList:
        graph[city] = []
        for neighbor in AList[city]:
            actual_neighbor = name_map.get(neighbor.lower(), neighbor)
            graph[city].append(actual_neighbor)
            if actual_neighbor not in graph:
                graph[actual_neighbor] = []

    # Calculate in-degrees for all cities
    # In-degree = number of cities that can reach this city
    in_degree = {city: 0 for city in graph}
    for city in graph:
        for neighbor in graph[city]:
            in_degree[neighbor] += 1

    # Find all starting cities with in-degree 0
    # These are cities with no incoming connections (starting points)
    queue = [city for city in graph if in_degree[city] == 0]

    # Keep track of the longest path found so far for each city
    # Initialize with just the city itself (path of length 1)
    paths = {city: [city] for city in graph}

    # Process the graph in topological order
    # We process nodes that have no remaining prerequisites
    while queue:
        # Get the next city to process (FIFO)
        current = queue.pop(0)

        # Update paths to all neighbors of the current city
        for neighbor in graph[current]:
            # If going through current city gives a longer path to neighbor,
            # update the neighbor's path
            if len(paths[current]) + 1 > len(paths[neighbor]):
                paths[neighbor] = paths[current] + [neighbor]

            # Reduce the in-degree (remove the edge we just processed)
            in_degree[neighbor] -= 1
            # If this neighbor now has no prerequisites, add it to the queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Find the longest path among all cities
    max_route = []
    for city in paths:
        if len(paths[city]) > len(max_route):
            max_route = paths[city]

    return max_route