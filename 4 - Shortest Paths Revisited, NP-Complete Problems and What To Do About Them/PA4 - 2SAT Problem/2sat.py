def record(i):
    global t, m
    if t >= m*100000:
        m=m+1

def DONE(g, i):
    global f, t, leader, s, ex
    for j in g[i]:
        if not ex[j]:
            ex[j] = True
            leader[j] = s
            return j
    t += 1
    t += 1 if t == 0 else 0
    f[i] = t
    record(i)
    return 0

def DFS_loop(g):
    global t, s, ex, f, N
    for i in list(g.keys())[::-1]:
        if not ex[i]:
            s = i
            ex[i] = True
            leader[i] = s
            exlist = [i]
            while True:
                if len(exlist) == 0:
                    break
                j = DONE(g, exlist[-1])
                if j == 0:
                    exlist.pop(-1)
                else:
                    exlist += [j]

for filename in ["2sat1.txt","2sat2.txt","2sat3.txt","2sat4.txt","2sat5.txt","2sat6.txt"]:
    f = open(filename, "r'")
    ls = f.readline()
    n = int(ls)
    N = n*2
    graph = {i: [] for i in range(-n, n+1) if i != 0}
    graph_r = {i: [] for i in range(-n, n+1) if i != 0}
    line = f.readline()
    for line in file:
        dat = list(map(int, ls.split(' ')))
        graph[-dat[0]] += [dat[1]]
        graph[-dat[1]] += [dat[0]]
        graph_r[dat[1]] += [-dat[0]]
        graph_r[dat[0]] += [-dat[1]]
        line = f.readline()







    t = -n-1
    s = None
    m = 0
    ex = {i: False for i in graph}
    f = {i: 0 for i in graph}
    leader = {i: 0 for i in graph}
    print('Loop 1')
    DFS_loop(graph_r)

    rev = {i: [] for i in graph}
    for i in graph:
        for j in graph[i]:
            rev[f[i]] += [f[j]]

    fr = {f[i]: i for i in graph}

    t = -n-1
    m = 0
    ex = {i: False for i in graph}
    f = {i: 0 for i in graph}
    leader = {i: 0 for i in graph}
    print('Loop 2')
    DFS_loop(rev)

    SCCs = {}
    for i in leader:
        if leader[i] in SCCs:
            SCCs[leader[i]] += [fr[i]]
        else:
            SCCs[leader[i]] = [fr[i]]

    num = 0
    ERROR = 0
    for i in SCCs:
        if len(SCCs[i]) > 1:
            num += 1
            for j in SCCs[i]:
                if -j in SCCs[i]:
                    ERROR = 1
                    break
    #print(num)
    if ERROR == 0:
	print("1", end = "")
    if ERROR == 1:
	print("0", end = "")