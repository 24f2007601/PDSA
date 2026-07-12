"""
Province counting explanation:
This program counts how many connected groups of cities exist in a country.
A province is a group of cities that are connected directly or indirectly.

The program uses DFS (Depth-First Search) to explore one connected component at a time.
"""

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Number of cities in the adjacency matrix.
        n = len(isConnected)

        # Track whether each city has already been visited during DFS.
        visited = [False] * n

        def dfs(city):
            # Mark the current city as visited.
            visited[city] = True

            # Explore all possible neighboring cities connected to this city.
            for neighbour in range(n):
                if (isConnected[city][neighbour] == 1) and (not visited[neighbour]):
                    dfs(neighbour)

        # Count of connected components (provinces).
        provinces = 0

        # Start a DFS from every unvisited city.
        # Each DFS traversal marks all cities in the same province as visited.
        for city in range(n):
            if not visited[city]:
                provinces += 1
                dfs(city)

        return provinces