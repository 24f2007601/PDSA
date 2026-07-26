import heapq

def dijkstra(WList, start):
    distances = {node: float('inf') for node in WList}
    parent = {node: None for node in WList}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue 
      
        for neighbour, weight in WList[current_node]:
            distance = current_distance + weight 
            
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                parent[neighbour] = current_node
                heapq.heappush(priority_queue, (distance, neighbour))
    return distances, parent 
    
def reconstruct_path(parent, target):
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = parent[current]
    return path[::-1]
    
def min_cost_walk(WList, S, D, V):
    dist_from_S, parent_from_S = dijkstra(WList, S)
    dist_from_V, parent_from_V = dijkstra(WList, V)
    total_cost = dist_from_S[V] + dist_from_V[D]
    
    path_S_to_V = reconstruct_path(parent_from_S, V)
    path_V_to_D = reconstruct_path(parent_from_V, D)
    
    full_path = path_S_to_V + path_V_to_D[1:]
    
    return (total_cost, full_path)






size = int(input())
edges = eval(input())
S= int(input())
D=int(input())
V=int(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges: #for create list for undirected graph
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(min_cost_walk(WL,S, D, V))