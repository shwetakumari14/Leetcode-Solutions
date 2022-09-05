class Graph:
    def __init__(self, noOfVetices):
        self.adjacencyMat = [[-1]*noOfVetices for i in range(noOfVetices)]
        self.noOfVetices = noOfVetices
        self.vertices = {}
        self.verticesList = [0]*noOfVetices

    def setVertices(self, vtxNo, id):
        if 0 <= vtxNo <= self.noOfVetices:
            self.vertices[id] = vtxNo
            self.verticesList[vtxNo] = id
    
    def setEdges(self, fromEdge, toEdge, weight):
        fromEdge = self.vertices[fromEdge]
        toEdge = self.vertices[toEdge]
        self.adjacencyMat[fromEdge][toEdge] = weight
        self.adjacencyMat[toEdge][fromEdge] = weight
    
    def getVertices(self):
        return self.verticesList
    
    def getEdges(self):
        edges = []

        for i in range(self.noOfVetices):
            for j in range(self.noOfVetices):
                if self.adjacencyMat[i][j] != -1:
                    edges.append((self.verticesList[i], self.verticesList[j], self.adjacencyMat[i][j]))
        
        return edges
    
    def getAdjacencyMat(self):
        return self.adjacencyMat

G = Graph(6)
G.setVertices(0, 'a')
G.setVertices(1, 'b')
G.setVertices(2, 'c')
G.setVertices(3, 'd')
G.setVertices(4, 'e')
G.setVertices(5, 'f')
G.setEdges('a','e',10)
G.setEdges('a','c',20)
G.setEdges('c','b',30)
G.setEdges('b','e',40)
G.setEdges('e','d',50)
G.setEdges('f','e',60)
print("Set Of Vertices")
print(G.getVertices())
print("Set Of Edges")
print(G.getEdges())
print("Adjacency Matric")
print(G.getAdjacencyMat())
