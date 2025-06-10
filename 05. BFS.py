ALGORITHM: 
1. Start with a queue and enqueue the starting node. 
2. Mark the starting node as visited. 
3. While the queue is not empty: a. Dequeue a node from the queue. b. Process the dequeued node. c. 
Enqueue all adjacent nodes of the dequeued node that are not yet visited. d. Mark each visited adjacent 
node. 
4. Repeat steps 3 until the queue is empty.

-----------------------------------------------------------
class Graph:
    def __init__(self):
        self.graph = {}

    def add(self,node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def bfs(self, start):
        visited = set()
        queue = [start]
        result = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                result.append(node)
                queue.extend(self.graph.get(node, []))
        return result

if __name__ == "__main__":
    g = Graph()

    for i in range(int(input("Enter no.of nodes:"))):
        li = input("Enter node and neighbor separated by a space: ").split()
        g.add(li[0], li[1])

    print(g.bfs("A"))
