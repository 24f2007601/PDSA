"""
Connection level explanation:
This program finds the shortest connection level between two people in a graph.
It uses BFS (Breadth-First Search), where each step moves one connection away from the starting person.

Think of it like a social network:
- Each person is a node in the graph
- Connections between people are edges
- "Connection level" is how many steps (friends of friends) away someone is

If the target is found, it returns the number of steps needed.
If no connection exists, it returns 0.
"""


def findConnectionLevel(n, Gmat, Px, Py):
    """
    Find the shortest connection level between two people in a graph.
    
    Args:
        n: Number of people (nodes) in the graph
        Gmat: An n x n adjacency matrix where Gmat[i][j] = 1 means 
              person i is directly connected to person j
        Px: The starting person (source node)
        Py: The target person (destination node)
        
    Returns:
        The minimum number of connections needed to go from Px to Py,
        or 0 if no path exists
    """
    # If the persons are the same, no connections are needed (level is 0).
    if Px == Py:
        return 0

    # Queue for BFS: stores tuples of (current_person, current_connection_level)
    # We start from Px at level 0
    queue = [(Px, 0)]
    
    # Keep track of visited people to avoid processing the same person twice
    visited = {Px}

    # Explore the graph level by level
    while queue:
        # Get the next person to explore (FIFO - first in, first out)
        current_person, level = queue.pop(0)

        # Check all possible connections for the current person
        # In the adjacency matrix, row 'current_person' shows who they are connected to
        for neighbor in range(n):
            # Check if current_person is connected to this neighbor
            if Gmat[current_person][neighbor] == 1:
                # If this neighbor is our target, we've found the answer!
                if neighbor == Py:
                    return level + 1

                # If we haven't visited this neighbor yet, add them to the queue
                if neighbor not in visited:
                    visited.add(neighbor)
                    # This neighbor is one level further from the start
                    queue.append((neighbor, level + 1))

    # If we've checked everyone and didn't find Py, they're not connected
    return 0
