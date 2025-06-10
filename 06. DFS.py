ALGORITHM: 
1. Create a stack to keep track of vertices. 
2. Push the starting vertex onto the stack. 
3. While the stack is not empty: 
    o Pop a vertex from the stack. 
    o If the vertex is not visited: 
        ▪ Mark it as visited. 
        ▪ Process the vertex (print or store it). 
        ▪ Push all unvisited neighbors of the vertex onto the stack. 

----------------------------------------------------------------
class Graph:
    def __init__(self):
        self.graph = {}

    def addnode(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)
    
    def dfs(self, start):
        visited = set()
        stack = [start]
        result = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                stack.extend(neighbor for neighbor in self.graph[node] if neighbor not in visited)
        return result

if __name__ == "__main__":
    g = Graph()

    for i in range(int(input("Enter no. of nodes: "))):
        li = input("Enter node and neighbor separated by space: ").split()
        g.addnode(li[0], li[1])

    print(g.dfs("D"))
