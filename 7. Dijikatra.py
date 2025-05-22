ALGORITHM:
1. Dijkstra's algorithm is a greedy algorithm that finds the shortest path between two nodes in a weighted 
graph.
2. The algorithm maintains a set of vertices whose shortest distance from the source is known.
3. At each step, it selects the vertex with the smallest known distance, explores its neighbors, and updates 
their distances if a shorter path is found.

----------------------------------------------------------------------------------------------------------------

import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        # Adding edges in both directions for undirected graph
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def dijkstra(self, start):
        # Initialize distances to infinity, except for the start node
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]  # (distance, node)

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # Skip nodes that have already been processed with a shorter distance
            if distances[current_node] < current_distance:
                continue

            # Check the neighbors of the current node
            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

                # If a shorter path to the neighbor is found
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


# Example usage

# Creating a weighted graph
graph = Graph()
n = int(input())
for i in range(n):
    input_data = input().split()
    graph.add_edge(input_data[0], input_data[1], int(input_data[2]))

# Running Dijkstra's algorithm from node 'A'
distances = graph.dijkstra('A')

# Displaying the shortest distances from node 'A'
print("Shortest distances from node A:")
for node, distance in distances.items():
    print(f"Distance from A to {node}: {distance}")
