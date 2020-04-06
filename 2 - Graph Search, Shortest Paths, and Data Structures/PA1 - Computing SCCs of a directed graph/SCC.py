import sys
import threading

#n = 875714
n = 10
E = {}
Erev = {}

for i in range(1,n+1):
    Erev[i] = []
    E[i] = []

file = open('scc_test_1.txt', "r")

for i in file:
    if i != None:
        v,w = i.split()
        E[int(v)].append(int(w))
        Erev[int(w)].append(int(v))

def SCC(graph):
	global leader

	if firstpass:
		for node in range(1, n + 1):
			if not explored[-1 * node]:
				DFS(graph, node)
	else:
		for node in reversed(finisht):
			if not explored[-1 * node]:
				leader = node
				DFS(graph, node)

def DFS(graph, start):
	explored[-1*start] = True

	if not firstpass:
		if leader not in SCCLIST:
			SCCLIST[leader] = [start]
		else:
			SCCLIST[leader].append(start)

	if start in graph:
		for v in graph[start]:
			if not explored[-1 * v]:
				DFS(graph, v)

	if firstpass:
		finisht.append(start)

explored, finisht, firstpass = [False] * 10, [], True
leader, SCCLIST = None, {}
SCC(Erev)
firstpass, explored = not firstpass, [False] * 10
SCC(E)

print(SCCLIST)