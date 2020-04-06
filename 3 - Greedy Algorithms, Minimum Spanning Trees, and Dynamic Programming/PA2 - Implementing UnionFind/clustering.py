class unionfind:    
    def __init__(self,n):
        self.num = n
        self.rank = [0]*n
        self.root = list(range(n))
        
    def get_root(self):
        return self.root
    def get_rank(self):
        return self.rank
    def get_num(self):
        return self.num

    def find(self, x):
        listy = self.root
        if listy[x] != x:
            listy[x] = self.find(listy[x])
        return listy[x]
    
    def count(self):
        return self.num
        
    def union(self, x,y):
        s = self.root
        ranks = self.rank
        
        s1 = self.find(x)
        s2 = self.find(y)
        
        if s1 == s2:
            return
        
        self.num -= 1
        if ranks[s1] == ranks[s2]:
            ranks[s1] +=1
            s[s2] = s1
        elif ranks[s1]>ranks[s2]:
            s[s2] = s1
        else:
            s[s1] = s2
            
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Edge:
    def __init__(self, v, w, cost):
        self.v = v
        self.w = w
        self.cost = cost
    
    def get_cost(self):
        return self.cost

def clustering(edges, k):
    edges = sorted(edges, key = lambda x: x.get_cost())
    
    UF = unionfind(500)
    

    for edge in edges:
        if not UF.connected(edge.v,edge.w) and UF.count()!= k:
            UF.union(edge.v,edge.w)
        
        if not UF.connected(edge.v,edge.w) and UF.count()== k:
            return edge.cost

edges = []
file = open("clustering1.txt")
for i in file:
    item = i.split()
    edges.append(Edge(int(item[0]) -1 , int(item[1]) -1 , int(item[2])))

print(clustering(edges, 4))