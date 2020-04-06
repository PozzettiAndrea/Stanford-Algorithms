import time

n = 200 #Number of nodes

E = {}

for i in range(1,n+1):
    E[i] = []

with open("dijkstraData.txt", "r") as file:
    for line in file:
        edge = line.split()
        for x in range(1,len(edge)):
            E[int(edge[0])].append([int(edge[x].split(",")[0]),int(edge[x].split(",")[1])])

#print(E)


def Dijkstra(Graph,s):
    X = [s] #edges explored so far
    A = {} #shortest path dict
    A[s] = 0
    while len(X) < 200:
        #print(len(X))
        edgestoconsider = {}
        for v in X:
            for edge in E[v]:
                if edge[0] not in X:
                    try:
                        if edgestoconsider[edge[0]][0]>(A[v] + edge[1]):
                            edgestoconsider[edge[0]] = [(A[v] + edge[1]),v]
                    except:
                        edgestoconsider[edge[0]] = [(A[v] + edge[1]),v]
        #print(edgestoconsider)
        newvert = min(edgestoconsider, key = edgestoconsider.get)
        X.append(newvert)
        #print(newvert,"newvertex")
        val = 0
        for edge in E[edgestoconsider[newvert][1]]:
            #print(edge)
            if edge[0] == newvert:
                val = edge[1]
        A[newvert] = (A[edgestoconsider[newvert][1]] + val)
        #print(A)
        #time.sleep(10)
    return(A)

dist = Dijkstra(E,1)

for i in [7,37,59,82,99,115,133,165,188,197]:
    print(dist[i], end=",")