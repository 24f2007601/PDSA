def longJourney(AList):
    # 1. Normalize case differences (e.g., 'varanasi' vs 'Varanasi')
    # Create a map from lowercase names to the exact keys present in AList
    name_map = {city.lower(): city for city in AList}
    
    # Rebuild the adjacency list with consistent, exact case keys
    graph = {}
    for city in AList:
        graph[city] = []
        for neighbor in AList[city]:
            actual_neighbor = name_map.get(neighbor.lower(), neighbor)
            graph[city].append(actual_neighbor)
            if actual_neighbor not in graph:
                graph[actual_neighbor] = []

    # 2. Calculate in-degrees for all cities
    in_degree = {city: 0 for city in graph}
    for city in graph:
        for neighbor in graph[city]:
            in_degree[neighbor] += 1

    # 3. Find all source cities (in-degree == 0) to start our BFS/Topological sort
    queue = [city for city in graph if in_degree[city] == 0]
    
    # 4. DP arrays: tracks the maximum path length and the actual path tracking array
    # Every city starts with a path containing just itself (length 1)
    paths = {city: [city] for city in graph}

    # 5. Process the graph topologically (Iterative loop - zero recursion)
    while queue:
        current = queue.pop(0)
        
        for neighbor in graph[current]:
            # If going through 'current' gives a longer path to 'neighbor', update it
            if len(paths[current]) + 1 > len(paths[neighbor]):
                paths[neighbor] = paths[current] + [neighbor]
            
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # 6. Find the absolute longest path calculated among all cities
    max_route = []
    for city in paths:
        if len(paths[city]) > len(max_route):
            max_route = paths[city]

    return max_route