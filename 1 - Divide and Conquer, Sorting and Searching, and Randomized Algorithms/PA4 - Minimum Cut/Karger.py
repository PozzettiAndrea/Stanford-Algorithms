import numpy
import copy

file = open('kargerMinCut.txt')

graph = []
for line in file:
    elems = line.split()
    if elems != None:
        a = [int(x) for x in elems]
        graph.append(a)

def find_remnodes(graph):
    nodes = []
    for i in range(len(graph)):
        nodes.append(graph[i][0])
    return nodes

def replace(nodes,graph,index,v1):
    for i in graph[index][1:]:
        index_index = nodes.index(i)
        for position,value in enumerate(graph[index_index]):
            if value == graph[index][0]:
                graph[index_index][position] = graph[v1][0]
    return graph

def contractedge(graph):
    v1 = numpy.random.randint(0,len(graph))
    v2 = numpy.random.randint(1,len(graph[v1]))
    nodes = find_remnodes(graph)
    index = nodes.index(graph[v1][v2])
    graph[v1].extend(graph[index][1:])
    graph = replace(nodes,graph,index,v1)
    graph[v1][1:] = [a for a in graph[v1][1:] if a!=graph[v1][0]]
    graph.remove(graph[index])
    return graph

def Karger(graph):
    graph = copy.deepcopy(graph)
    while len(graph) >2:
        graph = contractedge(graph)
        #print data
    num = len(graph[0][1:])
    return num

niters = 1000
Bah = 0
for i in range(niters):
    x = Karger(graph)
    if x < Bah or Bah == 0:
        Bah = x
    print(Bah)