from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Number of cities in the adjacency matrix
        n = len(isConnected)

        # Track whether each city has already been visited during DFS
        visited = [False] * n

        def dfs(city):
            # Mark the current city as visited
            visited[city] = True

            # Explore all possible neighbour cities connected to this city
            for neighbour in range(n):
                # If there is a direct connection and the neighbour is not visited,
                # continue the depth-first search from that neighbour.
                if (isConnected[city][neighbour] == 1) and (not visited[neighbour]):
                    dfs(neighbour)

        # Count of connected components (provinces)
        provinces = 0

        # Iterate over every city and start a DFS when we find an unvisited city.
        # Each DFS traversal marks all cities in the same province as visited.
        for city in range(n):
            if not visited[city]:
                provinces += 1
                dfs(city)

        # Return the total number of provinces found
        return provinces