# NODE
# id, value, nextVertex, EdgeLink

class Vertex: 
    
    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.nextVertex = None
        self.EdgeLink = None
    
    def __str__(self):
        return f"Vertex: {self.id}"