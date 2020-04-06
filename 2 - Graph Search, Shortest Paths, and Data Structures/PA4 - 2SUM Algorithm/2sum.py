import bisect

file = open("2sum.txt", "r")
for line in file:
    data = [int(line.rstrip()) for line in f]

data.sort()

s = set([])
for x in data:    
    t = bisect.bisect_right(data, 10000 - x)
    b = bisect.bisect_left(data, -10000 - x)
    for y in data[b:t]:
        s.add(x + y)

print(len(s))
