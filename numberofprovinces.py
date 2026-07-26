"""
Province counting explanation:
This program counts how many connected groups of cities exist in a country.
A province is a group of cities that are connected directly or indirectly.

The program uses DFS (Depth-First Search) to explore one connected component at a time.
Think of it like finding islands on a map:
- Two cities are in the same province if there's a path between them
- DFS explores all reachable cities from one starting point
- Every time we find an unvisited city, it's a new province!
"""

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Find the number of connected provinces in a country.
        
        Args:
            isConnected: An adjacency matrix where isConnected[i][j] = 1 means
                        city i is directly connected to city j
            
        Returns:
            The number of connected provinces (groups of cities)
        """
        # Number of cities in the adjacency matrix
        n = len(isConnected)

        # Track whether each city has already been visited during DFS
        visited = [False] * n

        def dfs(city):
            """
            Explore all cities reachable from the given city using DFS.
            
            Args:
                city: The current city we're exploring from
            """
            # Mark the current city as visited so we don't process it again
            visited[city] = True

            # Explore all possible neighboring cities connected to this city
            for neighbour in range(n):
                # If there's a direct connection AND we haven't visited this neighbour
                if (isConnected[city][neighbour] == 1) and (not visited[neighbour]):
                    # Recursively explore from the neighbour
                    dfs(neighbour)

        # Count of connected components (provinces)
        provinces = 0

        # Start a DFS from every unvisited city
        # Each DFS traversal marks all cities in the same province as visited
        for city in range(n):
            # If we find a city we haven't visited yet, it's a new province!
            if not visited[city]:
                provinces += 1  # Found a new province
                dfs(city)  # Explore all cities in this province

        return provinces