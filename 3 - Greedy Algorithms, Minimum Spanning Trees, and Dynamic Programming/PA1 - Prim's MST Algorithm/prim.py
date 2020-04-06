def ff(x):
    return x[2]

file = open("edges.txt", "r")
costs = {}
graph = {}

for i in range(1,501):
    graph[i] = []

for i in file:
    #print(i.strip().split(' '))
    edge = i.strip().split(' ')
    v1 = int(edge[0])
    v2 = int(edge[1])
    costs[(v1, v2)] = int(edge[2])
    costs[(v2, v1)] = int(edge[2])
    graph[v1].append(v2)
    graph[v2].append(v1)

def prim(graph, costs):
    Totalcost = 0
    X = [1]
    T = []
    while len(T)<499:
        print(len(T))
        edgesncosts = []
        for leader in X:
            for v in graph[leader]:
                if v not in X:
                    edgesncosts.append([leader,v,costs[leader,v]])
        edgesncosts.sort(key = lambda x: x[2])
        luckyedge = edgesncosts[0]
        T.append(luckyedge)
        X.append(luckyedge[1])
        Totalcost += luckyedge[2]
    return Totalcost

print(prim(graph,costs))