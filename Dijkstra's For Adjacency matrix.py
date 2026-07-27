def dijkstra(WMat,s):
    #Initialization
    (rows,cols,x) = WMat.shape
    infinity = np.max(WMat)*rows+1
    (visited,distance) = ({},{})
    for v in range(rows):
        (visited[v],distance[v]) = (False,infinity)        
    distance[s] = 0
    
    # Computing shortest distance for each vertex from source
    for u in range(rows):
        # Find minimum distance value on vertices which are not visited
        min_dist = min([distance[v] for v in range(rows) if not visited[v]])
        
        # Find vertices which have minimum distance value min_dist
        nextv_list = [v for v in range(rows)if (not visited[v]) and distance[v] == min_dist]
        
        # Select minimum level vertex which have minimum distance value min_dist and mark visited
        nextv = min(nextv_list)
        visited[nextv] = True
        
        # Check for each adjacent of nextv vertex which is not visited
        for v in range(cols):            
            if WMat[nextv,v,0] == 1 and (not visited[v]):
                #If distance of v through nextv is smaller than the current distance on v, then update
                if distance[nextv] + WMat[nextv,v,1] < distance[v]:
                    distance[v] = distance[nextv] + WMat[nextv,v,1]
    return(distance)



dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]
size = 7
import numpy as np
W = np.zeros(shape=(size,size,2))
for (i,j,w) in dedges:
    W[i,j,0] = 1
    W[i,j,1] = w
print(dijkstra(W,0))
Output

{0: 0, 1: 10.0, 2: 16.0, 3: 86.0, 4: 30.0, 5: 80.0, 6: 35.0}
Complexity


 

