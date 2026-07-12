def findConnectionLevel(n, Gmat, Px, Py):
    # If the persons are the same, the level is 0
    if Px == Py:
        return 0
    
    # Queue for BFS: stores (current_person, current_level)
    queue = [(Px, 0)]
    # Set to keep track of visited persons
    visited = {Px}
    
    while queue:
        current_person, level = queue.pop(0)
        
        # Check all possible connections for the current person
        for neighbor in range(n):
            # If there is an edge and the neighbor hasn't been visited
            if Gmat[current_person][neighbor] == 1:
                if neighbor == Py:
                    return level + 1
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))
    
    # If no path is found, return 0 as per instructions
    return 0
