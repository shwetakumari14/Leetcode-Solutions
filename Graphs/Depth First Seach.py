from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFSUntil(self, v, visited):

        visited.add(v)
        print(v, end = " ")

        for i in self.graph[v]:
            if i not in visited:
                self.DFSUntil(i, visited)
    
    def DFS(self, v):
        visited = set()

        self.DFSUntil(v, visited)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.DFS(2)