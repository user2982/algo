ALGORITHM:

1. Dijkstra's algorithm is a greedy algorithm that finds the shortest path between two nodes in a weighted 

graph.

2. The algorithm maintains a set of vertices whose shortest distance from the source is known.

3. At each step, it selects the vertex with the smallest known distance, explores its neighbors, and updates 

their distances if a shorter path is found.
------------------------------------------------------------------------------------------------------------------
PROGRAM:
import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]  

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if distances[current_node] < current_distance:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

graph = Graph()
n = int(input())
for i in range(n):
    input_data = input().split()
    graph.add_edge(input_data[0], input_data[1], int(input_data[2]))

distances = graph.dijkstra('A')

print("Shortest distances from node A:")
for node, distance in distances.items():
    print(f"Distance from A to {node}: {distance}")
