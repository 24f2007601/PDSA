"""
Graph path-checking explanation:
This program checks whether a path exists between two nodes in an undirected graph.
It uses BFS (Breadth-First Search), which explores nearby nodes first before moving farther away.

This is helpful when you need to answer questions like:
- Can I reach this city from this city?
- Is there a connection between two people in a network?
"""

from collections import deque


class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        """Check whether a path exists from source to destination in an undirected graph."""

        # If the start and end are the same, a path already exists.
        if source == destination:
            return True

        # Build an adjacency list so each node knows its neighbors.
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Use a queue to explore nodes level by level.
        queue = deque([source])
        visited = [False] * n
        visited[source] = True

        while queue:
            node = queue.popleft()

            # If we reach the destination, a valid path exists.
            if node == destination:
                return True

            # Visit all unvisited neighbors of the current node.
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        # If the search finishes without reaching the destination, no path exists.
        return False

    def validPathOptimized(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        """A slightly more compact BFS version using a set for visited nodes."""

        if source == destination:
            return True

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque([source])
        visited = {source}

        while queue:
            node = queue.popleft()
            if node == destination:
                return True

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False
