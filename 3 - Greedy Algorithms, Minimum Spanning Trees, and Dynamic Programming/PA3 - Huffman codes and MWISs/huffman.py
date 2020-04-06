import heapq

alpha = {}
with open("huffman.txt") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        alpha[i] = [int(line.split()[0]),0,0]

def huffman(alpha):
    #print(alpha.items())
    freqs = [[f[0], f[1], f[2]] for letter, f in alpha.items()]
    heapq.heapify(freqs)
    #print(freqs)
    while len(freqs) > 1:
        #print(freqs)
        a, b = heapq.heappop(freqs), heapq.heappop(freqs)
        heapq.heappush(freqs, [a[0] + b[0], 1 + min(a[1], b[1]), 1 + max(a[2], b[2])])
    return freqs[0][1], freqs[0][2]

print("Min and max lengths for a codeword are:", huffman(alpha))