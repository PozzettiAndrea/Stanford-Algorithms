import numpy as np
from numba import jit
import threading

f = open("nn.txt", "r")
ls = f.readlines()[1:]
graph = [list(map(float, i.split(' ')))[1:] for i in ls]
graph = {i: graph[i] for i in range(len(graph))}

N = len(graph)


def dis(i, j):
    return (graph[i][0]-graph[j][0])**2+(graph[i][1]-graph[j][1])**2

def main():
    tour = [0]
    travel = 0
    g = graph.copy()
    g.pop(0)
    
    
    while len(g) > 0:
        plan = 1e9
        for c in g:
            d = dis(tour[-1], c)
            if d < plan:
                plan = d
                city = c
        travel += np.sqrt(plan)
        tour += [city]
        g.pop(city)
        if len(g) % 10 == 0:
            print("Travel %i, %i cities remaining" % (city, len(g)))
    
    travel += np.sqrt(dis(0, tour[-1]))
    print(travel)

if __name__ == "__main__":
    threading.stack_size(67108864*2)
    thread = threading.Thread(target=main)
    thread.start()