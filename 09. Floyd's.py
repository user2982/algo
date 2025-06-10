PROCEDURE: 
The Floyd-Warshall algorithm works by considering all possible intermediate vertices in the paths between 
two vertices and gradually updates the shortest paths. 
 
1. Initialize the distance matrix with the direct edges and set the distances to infinity where there is no 
direct edge. 
2. For each intermediate vertex, update the distance matrix if a shorter path is found through that vertex.
-----------------------------------------------------------------------------------------------------------
PROGRAM:
INF = float('inf') 
def floyd_warshall(graph): 
    num_vertices = len(graph) 
    distance_matrix = [[0 if i == j else graph[i][j] if graph[i][j] != 0 else INF for j in range(num_vertices)] for i 
    in range(num_vertices)] 
    for k in range(num_vertices): 
        for i in range(num_vertices): 
            for j in range(num_vertices): 
                if distance_matrix[i][k] + distance_matrix[k][j] < distance_matrix[i][j]: 
                    distance_matrix[i][j] = distance_matrix[i][k] + distance_matrix[k][j] 
    return distance_matrix 

graph = [ 
[0, 3, INF, 5], 
[2, 0, INF, 4], 
[INF, 1, 0, INF], 
[INF, INF, 2, 0] 
] 
result = floyd_warshall(graph) 
for row in result: 
    print(row)
