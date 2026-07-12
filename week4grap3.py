"""
Longest journey explanation:
This program finds the longest route in a directed graph using a topological-style traversal.
It builds a path from each city to its neighbors and keeps the longest path seen so far.

This is useful for problems where you want the longest valid sequence of connected cities.
"""


def longJourney(AList):
    # Normalize names so different cases are treated the same.
    name_map = {city.lower(): city for city in AList}

    # Rebuild the adjacency list with consistent exact names.
    graph = {}
    for city in AList:
        graph[city] = []
        for neighbor in AList[city]:
            actual_neighbor = name_map.get(neighbor.lower(), neighbor)
            graph[city].append(actual_neighbor)
            if actual_neighbor not in graph:
                graph[actual_neighbor] = []

    # Calculate in-degrees for all cities.
    in_degree = {city: 0 for city in graph}
    for city in graph:
        for neighbor in graph[city]:
            in_degree[neighbor] += 1

    # Find all starting cities with in-degree 0.
    queue = [city for city in graph if in_degree[city] == 0]

    # Keep the longest path found so far for each city.
    paths = {city: [city] for city in graph}

    # Process the graph in topological order.
    while queue:
        current = queue.pop(0)

        for neighbor in graph[current]:
            if len(paths[current]) + 1 > len(paths[neighbor]):
                paths[neighbor] = paths[current] + [neighbor]

            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Choose the longest path among all cities.
    max_route = []
    for city in paths:
        if len(paths[city]) > len(max_route):
            max_route = paths[city]

    return max_route