from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, node):
        visited, queue = [False] * (max(self.graph) + 1), []

        queue.append(node)
        visited[node] = True

        while queue:
            node = queue.pop()
            print(node, end = " ")

            for i in self.graph[node]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.BFS(2)


    