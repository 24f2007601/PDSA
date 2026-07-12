"""
Connection level explanation:
This program finds the shortest connection level between two people in a graph.
It uses BFS, where each step moves one connection away from the starting person.

If the target is found, it returns the number of steps needed.
If no connection exists, it returns 0.
"""


def findConnectionLevel(n, Gmat, Px, Py):
    # If the persons are the same, the level is 0.
    if Px == Py:
        return 0

    # Queue for BFS: stores (current_person, current_level).
    queue = [(Px, 0)]
    visited = {Px}

    while queue:
        current_person, level = queue.pop(0)

        # Check all possible connections for the current person.
        for neighbor in range(n):
            if Gmat[current_person][neighbor] == 1:
                if neighbor == Py:
                    return level + 1

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))

    # If no path is found, return 0.
    return 0
