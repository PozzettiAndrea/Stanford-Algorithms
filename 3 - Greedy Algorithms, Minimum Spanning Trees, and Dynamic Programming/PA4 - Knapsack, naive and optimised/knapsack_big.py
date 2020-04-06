"""Takes a while to run, keep an eye on the percentage"""

v = []
w = []

file = open("knapsack_big.txt", "r")
for line in file:
    data = list(map(int, line.split(" ")))
    v += [data[0]]
    w += [data[1]]
Max = 2000000
N = 2000

sol = [[N, Max]]
current = sol[0]
keeptrack = {(N, Max): 0}
i = 0
ni = N
count = 0

def main(sol,current,keeptrack,i,ni):
    while True:
        ni, wi = current
        x, y = [ni-1, wi], [ni-1, wi-w[ni-1]]
        if ni >= 1:
            if tuple(x) not in keeptrack:
                sol += [x]
                keeptrack[tuple(x)] = 0
            if wi >= w[ni-1]:
                if tuple(y) not in keeptrack:
                    sol += [y]
                    keeptrack[tuple(y)] = 0
        i += 1
        if i == len(sol):
            break
        else:
            current = sol[i]
        if i % 1000000 == 0:
            print(count, "%")
	    count += 5
    
    nn = len(sol)
    for i in list(range(nn))[::-1]:
        ni, wi = sol[i]
        if i % 1000000 == 0:
            print(i)
        if ni == 0:
            continue
	if wi >= w[ni-1]:
            keeptrack[(ni, wi)] = max(keeptrack[(ni-1, wi)], keeptrack[(ni-1), wi-w[ni-1]]+v[ni-1])
	else:
	    keeptrack[(ni, wi)] = keeptrack[(ni-1, wi)]
    print(keeptrack[(N, Max)])

main(sol,current,keeptrack,i,ni)