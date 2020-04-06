with open("knapsack1.txt") as file:
        lines = file.readlines()
        w = int(lines[0].split()[0])
        n = int(lines[0].split()[1])
        values = [int(line.split()[0]) for line in lines[1:]]
        weights = [int(line.split()[1]) for line in lines[1:]]

v = {}

def knapsack(values, weights, w, v):
    if w <= 0:
        return 0
    if len(values) == 1:
        if weights[0] <= w:
            return values[0]
        else:
            return 0
    v1 = v.get((len(values[:-1]), w))
    if not v1:
        v1 = knapsack(values[:-1], weights[:-1], w, v)
        v[(len(values[:-1]), w)] = v1
    v2 = v.get((len(values[:-1]), w - weights[-1]))
    if not v2:
        v2 = knapsack(values[:-1], weights[:-1], w - weights[-1], v)
        v[(len(values[:-1]), w - weights[-1])] = v2
    if weights[-1] <= w:
        v2 = v2 + values[-1]
    else:
        v2 = 0
    return max(v1, v2)

print(knapsack(values, weights, w, v))