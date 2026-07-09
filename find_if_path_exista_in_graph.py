from collections import deque


class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        """Check whether a path exists from source to destination in an undirected graph."""

        # Step 1: If the source and destination are the same, a path already exists.
        if source == destination:
            return True

        # Step 2: Build an adjacency list so each node can quickly access its neighbors.
        # This is better than checking every pair of nodes every time.
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Step 3: Use BFS (Breadth-First Search) to explore nodes level by level.
        # Start from the source and keep track of visited nodes.
        queue = deque([source])
        visited = [False] * n
        visited[source] = True

        # Step 4: Continue until the queue is empty.
        while queue:
            # Take the next node to process from the front of the queue.
            node = queue.popleft()

            # Step 5: If we reach the destination, a valid path exists.
            if node == destination:
                return True

            # Step 6: Visit all unvisited neighbors of the current node.
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        # Step 7: If BFS finishes without finding the destination, no path exists.
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
