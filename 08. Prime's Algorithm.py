ALGORITHM: 
1. Start with an arbitrary node as the initial vertex. 
2. Create a priority queue to store edges with their weights. 
3. Mark the chosen initial vertex as visited. 
4. Add all edges connected to the initial vertex to the priority queue. 
5. While the priority queue is not empty: 
o Dequeue the edge with the minimum weight. 
o If the destination vertex of the edge is not visited: 
▪ Mark the destination vertex as visited. 
▪ Add the edge to the minimum spanning tree. 
▪ Add all edges connected to the destination vertex that are not visited to the priority 
queue. 
6. Repeat step 5 until all vertices are visited.
--------------------------------------------------------------------------------------------
PROGRAM:
import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight): 
        self.graph[u].append((v, weight)) 
        self.graph[v].append((u, weight)) 

    def prim_mst(self):
        min_spanning_tree = []
        visited = [False] * self.vertices
        priority_queue = []

        heapq.heappush(priority_queue, (0, 0))

        while(priority_queue):
            weight, current_vertex = heapq.heappop(priority_queue)

            if not visited[current_vertex]:
                visited[current_vertex] = True
                min_spanning_tree.append((current_vertex, weight))

                for neighbor, edge_weight in self.graph[current_vertex]:
                    if not visited[neighbor]:
                        heapq.heappush(priority_queue, (edge_weight, neighbor))
        
        return min_spanning_tree
    
g = Graph(5) 
g.add_edge(0, 1, 2) 
g.add_edge(0, 3, 8) 
g.add_edge(1, 2, 3) 
g.add_edge(1, 3, 6) 
g.add_edge(2, 4, 1) 
g.add_edge(3, 4, 5)

result = g.prim_mst()
print("Minimum Spanning Tree:\n")
for vertex, weight in result:
    print(f"Vertex: {vertex}, Weight from parent: {weight}")
