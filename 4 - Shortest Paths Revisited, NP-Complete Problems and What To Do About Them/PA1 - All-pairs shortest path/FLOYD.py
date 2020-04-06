from tqdm import tqdm
import numpy as np
import threading
import copy
from numba import jit, int64


class Edge:
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

def load(name):
    file = open(name,"r")
    data = file.readlines()
    
    n = int(data[0].split()[0])
    m = int(data[0].split()[1])
    
    A = np.zeros((n,n,n+1), dtype= "int64")
    inf = 9999
    
    for i in range(n):
        for j in range(n):
            if i==j:
                A[i,j,0] = 0
            else:
                A[i,j,0] = inf
    for index, line in enumerate(data[1:]):
        item = line.split()
        A[int(item[0]) -1 ,int(item[1])-1,0] = int(item[2])
        
    return A

@jit(nopython = True, parallel = True)
def floyd(A):
    n = A.shape[0]
    for k in range(1, n+1):
        if k % 10 == 0:
            print(k//10, "%")
        for i in range(n):
            for j in range(n):
                A[i,j,k] = min(A[i,j,k-1], A[i,k-1,k-1]+A[k-1,j,k-1])

    for i in range(n):
        if A[i,i,n] <0:
            #negative cycle
            return None
    mpath = np.min(A[:,:,n])
    
    return mpath
    
    
def main():
    A = load("g1.txt")
    mpath1 = floyd(A)
    print(mpath)
    
    A = load("g2.txt")
    mpath2 = floyd(A)
    print(mpath)
    
    A = load("g3.txt")
    mpath3 = floyd(A)
    print(mpath)

if __name__ == "__main__":
    threading.stack_size(67108864*2)
    thread = threading.Thread(target=main)
    thread.start()