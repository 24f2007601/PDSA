def dijkstralist(WList,s):
    #Initialization
    infinity = 1 + len(WList.keys())*max([d for u in WList.keys() for (v,d) in WList[u]])
    (visited,distance) = ({},{})
    for v in WList.keys():
        (visited[v],distance[v]) = (False,infinity)        
    distance[s] = 0
    
    # Computing shortest distance for each vertex from source
    for u in WList.keys():
        # Find minimum distance value on vertices which are not visited
        min_dist = min([distance[v] for v in WList.keys() if not visited[v]])
        
        # Find vertices which have minimum distance value min_dist
        nextv_list = [v for v in WList.keys() if (not visited[v]) and distance[v] == min_dist]

        # Select minimum level vertex which have minimum distance value min_dist and mark visited
        nextv = min(nextv_list)
        visited[nextv] = True
        
        # Check for each adjacent of nextv vertex which is not visited
        for (v,d) in WList[nextv]:
            if not visited[v]:
                # If distance of v through nextv is smaller than the current distance of v, then update
                if distance[nextv]+d < distance[v]:
                    distance[v] = distance[nextv]+d
    return(distance)



dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]
size = 7
WL = {}
for i in range(size):
    WL[i] = []
for (i,j,d) in dedges:
    WL[i].append((j,d))
print(dijkstralist(WL,0))

