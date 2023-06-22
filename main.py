from graph import Graph,UndirectedGraph, DirectedGraph


graph = DirectedGraph()

graph.addVertex("1",10)
graph.addVertex("2",10)
graph.addVertex("3",10)
graph.addVertex("4",10)

graph.addEdge("1","2",1)
graph.addEdge("2","4",1)
graph.addEdge("4","3",1)
graph.addEdge("3","2",1)

list = graph.topologicalOrder()
print(list)

graph.visualGraph()
