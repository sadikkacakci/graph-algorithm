# vertexId, weight, nextEdge

class Edge:
    def __init__(self,vertexId,weight):
        self.vertexId = vertexId
        self.weight = weight
        self.nextEdge = None

    def __str__(self):
        return f"vertexId: {self.vertexId}, weight: {self.weight}"