from edge import Edge
from vertex import Vertex
from exception import checkId,checkWeight
from myQueue import Queue
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.head = None
        self.vertecies = []
        self.edges = []

    def findVertex(self,id):
        if(checkId(id) == False):
            return
        iterator = self.head
        while(iterator != None):
            if(iterator.id == id):
                return iterator
            iterator = iterator.nextVertex
        return None
    
    def findVertexOfNeighbors(self,id):
        if(checkId(id) == False):
            return        
        current = self.findVertex(id)
        if(current == None):
            print("This vertex does not exist.")
        else:
            iterator = current.EdgeLink
            if(iterator == None):
                print("This vertex has no edge.")
            while(iterator != None):
                print(f"{id} -> {iterator.vertexId}")
                iterator = iterator.nextEdge
        
    def addVertex(self, id, value):
        if(checkId(id) == False):
            return        
        if(self.findVertex(id) == None):
            vertex = Vertex(id,value)
            self.vertecies.append(vertex)
            if(self.head == None):
                self.head = vertex
                self.vertecies.append(vertex)
            else:
                iterator = self.head
                while(iterator.nextVertex != None):
                    iterator = iterator.nextVertex
                iterator.nextVertex = vertex
                self.vertecies.append(vertex)
        else:
            print(f"The vertex has {id} id number is exist.")
            
    def getVertexList(self):
        return self.vertecies

    def addEdge(self, idStart, idEnd, weight): 
        if(checkId(idStart) != True or checkId(idEnd) != True or checkWeight(weight) != True):
            return
        current = self.findVertex(idStart)
        if( current != None or self.findVertex(idEnd) != None ): 
            iterator = current.EdgeLink 
            if(iterator == None):
                current.EdgeLink = Edge(idEnd,weight)
                self.edges.append([idStart,idEnd,weight])
            else: 
                while(iterator.nextEdge != None): 
                    iterator = iterator.nextEdge
                iterator.nextEdge = Edge(idEnd,weight)
                self.edges.append([idStart,idEnd,weight])
        else:
            print(f"This edge can not exist. The id's: {idStart} or {idEnd} does not exist.")

    def getEdgeList(self):
        return self.edges
    
    def displayVertex(self):
        iterator = self.head
        while(iterator != None):
            print(iterator.value)
            iterator = iterator.nextVertex
    
    def breathFirstSearch(self):
        def checkList(id, list):
            if not id in list:
                list.append(id)
            return list        
        bfs_list = []
        iterator = self.head
        while(iterator != None):
            bfs_list = checkList(iterator.id,bfs_list)
            iterator_edge = iterator.EdgeLink
            while(iterator_edge != None):
                bfs_list = checkList(iterator_edge.vertexId,bfs_list)
                iterator_edge = iterator_edge.nextEdge
            iterator = iterator.nextVertex        
        return bfs_list
    

    def depthFirstSearch(self):
        def checkList(id, list):
            if not id in list: 
                list.append(id)
            return list             
        dfs_list = []
        iterator = self.head
        while(iterator != None):
            dfs_list = checkList(iterator.id,dfs_list)
            iterator_edge = iterator.EdgeLink
            while(iterator_edge != None):
                dfs_list = checkList(iterator_edge.vertexId,dfs_list)
                iterator_edge_v2 = self.findVertex(iterator_edge.vertexId).EdgeLink
                while(iterator_edge_v2 != None):
                    dfs_list = checkList(iterator_edge_v2.vertexId,dfs_list)
                    iterator_edge_v2 = iterator_edge_v2.nextEdge
                iterator_edge = iterator_edge.nextEdge
            iterator = iterator.nextVertex
        return dfs_list
    
class UndirectedGraph(Graph):

    def __init__(self):
        super().__init__()

    def findVertex(self, id):
        return super().findVertex(id)

    def findVertexOfNeighbors(self,id):
        return super().findVertexOfNeighbors(id)
        
    def addVertex(self,id,value):
        super().addVertex(id,value)  

    def getVertexList(self):
        return super().getVertexList()
    
    def getEdgeList(self):
        return super().getEdgeList()
    
    def addEdge(self, idStart, idEnd, weight): 
        super().addEdge(idStart, idEnd, weight)

    def displayVertex(self):
        super().displayVertex()

    def breathFirstSearch(self):
        return super().breathFirstSearch()

    def depthFirstSearch(self):
        return super().depthFirstSearch()
    
    def visualGraph(self):
        graph = nx.MultiGraph()
        vertecies = self.getVertexList()
        for vertex in vertecies:
            graph.add_node(vertex.id)
        for edge in self.getEdgeList():
            graph.add_edge(edge[0],edge[1],weight = edge[2]) #idstart, idend, weight
        pos = nx.spring_layout(graph)
        edge_labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw(graph, pos, with_labels=True, node_color='c', node_size=500, edge_color='gray')
        for (u, v, keys, data) in graph.edges(keys=True, data=True):
            label = edge_labels[(u, v, keys)]
            x = pos[u][0] + (pos[v][0] - pos[u][0]) * 0.45  # weight coordinates of x 
            y = pos[u][1] + (pos[v][1] - pos[u][1]) * 0.45  # weight coordinates of y 
            plt.text(x, y, label, verticalalignment='center', horizontalalignment='center', color='red')
        plt.show()

class DirectedGraph(Graph):

    def __init__(self):
        super().__init__()

    def findVertex(self, id):
        return super().findVertex(id)

    def findVertexOfNeighbors(self,id):
        return super().findVertexOfNeighbors(id)
        
    def addVertex(self,id,value):
        super().addVertex(id,value)  

    def getVertexList(self):
        return super().getVertexList()
    
    def getEdgeList(self):
        return super().getEdgeList()
    
    def addEdge(self, idStart, idEnd, weight): 
        super().addEdge(idStart, idEnd, weight)

    def displayVertex(self):
        super().displayVertex()

    def breathFirstSearch(self):
        return super().breathFirstSearch()

    def depthFirstSearch(self):
        return super().depthFirstSearch()
    
    def inDegree(self,id):
        if(self.findVertex(id) == None):
            print("This vertex does not exist.")
            return
        iterator = self.head
        inDegreeCounter = 0
        while(iterator != None):
            iterator_edge = iterator.EdgeLink
            while(iterator_edge != None):
                if(iterator_edge.vertexId == id):
                    inDegreeCounter += 1
                iterator_edge = iterator_edge.nextEdge
            iterator = iterator.nextVertex
        return inDegreeCounter


    def outDegree(self,id):
        outDegreeCounter = 0
        iterator = self.findVertex(id)
        while(iterator.EdgeLink != None):
            print(f"{id} -> {iterator.EdgeLink.vertexId}")
            outDegreeCounter += 1
            iterator.EdgeLink = iterator.EdgeLink.nextEdge
        return outDegreeCounter


    def topologicalOrder(self):
        def getVertexWhichIndegree0():
            iterator = self.head
            while(iterator != None):
                indegree_value = self.inDegree(iterator.id)
                if(indegree_value == 0):
                    return iterator
                iterator = iterator.nextVertex
            return None
        
        def getIndegreeArray():
            inDegreeDict = {}
            iterator = self.head
            while(iterator != None):
                inDegreeDict.update({iterator.id:self.inDegree(iterator.id)})
                iterator = iterator.nextVertex 
            return inDegreeDict        
        
        queue = Queue()
        order = []
        inDegreeDict = getIndegreeArray()
        starting_vertex = getVertexWhichIndegree0()
        if starting_vertex == None:
            print("There is no vertex which has indegree 0. This must be a cycle graph.")
            return None
        queue.enqueue(starting_vertex)
        iterators = []
        while( not queue.isEmpty()):
            iterator = queue.dequeue()
            iterators.append(iterator.id)
            order.append(iterator.id)
            iterator_edge = iterator.EdgeLink
            while(iterator_edge != None):
                inDegreeDict.update({iterator_edge.vertexId : inDegreeDict.get(iterator_edge.vertexId) - 1})
                if(inDegreeDict.get(iterator_edge.vertexId) == 0):
                    queue.enqueue(self.findVertex(iterator_edge.vertexId))
                iterator_edge = iterator_edge.nextEdge

            if(queue.isEmpty()):
                keys = inDegreeDict.keys()
                for key in keys:
                    value = inDegreeDict.get(key)
                    if(value == 0 and  (not key in iterators)):
                        queue.enqueue(self.findVertex(key))
                        break
            dict_values = inDegreeDict.values()
            if all(value == 0 for value in dict_values):
                for i in range(queue.size()):
                    order.append(queue.dequeue().id)
                return order
        print("Cycle Graph!")
        return None           
        
    def isCycle(self):
        value = self.topologicalOrder()
        if value == None:
            return True
        else:
            return False
    
    def visualGraph(self):
        graph = nx.MultiDiGraph()
        vertecies = self.getVertexList()
        for vertex in vertecies:
            graph.add_node(vertex.id)
        for edge in self.getEdgeList():
            graph.add_edge(edge[0],edge[1],weight = edge[2]) #idstart, idend, weight
        pos = nx.spring_layout(graph)
        nx.draw(graph, pos, with_labels = True, node_color = "c", node_size = 350, edge_color = "gray")
        weight_labels = nx.get_edge_attributes(graph, 'weight')
        for (u, v, keys, data) in graph.edges(keys=True, data=True):
            label = weight_labels[(u, v, keys)]
            x = pos[u][0] + (pos[v][0] - pos[u][0]) * 0.45
            y = pos[u][1] + (pos[v][1] - pos[u][1]) * 0.45  
            plt.text(x, y, label, verticalalignment='center', horizontalalignment='center', color='red')
        plt.show()