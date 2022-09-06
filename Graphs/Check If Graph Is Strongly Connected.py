from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFSUntil(self, v, visited):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUntil(i, visited)
    
    def getTranspose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        
        return g
    
    def isSC(self):
        visited = [False]*self.V
        self.DFSUntil(0, visited)

        if any(i == False for i in visited):
            return False
        
        gr = self.getTranspose()

        visited = [False]*self.V
        gr.DFSUntil(0, visited)

        if any(i == False for i in visited):
            return False
        
        return True


g1 = Graph(5)
g1.addEdge(0, 1)
g1.addEdge(1, 2)
g1.addEdge(2, 3)
g1.addEdge(3, 0)
g1.addEdge(2, 4)
g1.addEdge(4, 2)
print ("Yes" if g1.isSC() else "No")
 
g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print ("Yes" if g2.isSC() else "No")