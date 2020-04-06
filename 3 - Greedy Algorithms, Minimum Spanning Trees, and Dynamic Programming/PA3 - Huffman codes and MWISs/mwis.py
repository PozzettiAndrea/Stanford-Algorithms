file = open("mwis.txt", "r")
PG = []
for line in file:
    PG.append(int(line.strip()))

n = 1000

def MWIS(PG):
    S = []
    W = [0] * (n + 1)
    W[1] = PG[0]
    for i in range(2, n + 1):
        W[i] = max(W[i - 1], W[i - 2] + PG[i - 1])

    
    i = n
    while i > 0:
        if W[i] > W[i - 2] + PG[i - 1]:
            i -= 1
        else:
            S.append(i)
            i -= 2
    return S


S = MWIS(PG)
tocheck = [1, 2, 3, 4, 17, 117, 517, 997]

for i in tocheck:
    if i in S:
        print(1, end = "")
    else:
        print(0,end = "")