File = open("IntegerArray.txt","r")
Ints = File.readlines()

for i in range(len(Ints)):
    Ints[i] = int(Ints[i])

def findinversions(arr):
    x = len(arr)
    if x<=1:
        return 0, arr
    else:
        A = arr[:x//2]
        B = arr[x//2:]
        splits = 0
        i = 0
        j = 0
        sordet = []
        l, A = findinversions(A)
        r, B = findinversions(B)
        lnr = l+r
        splits = 0
        while i < len(A) and j < len(B):
            if A[i] < B[j] or A[i] == B[j]:
                sordet.append(A[i])
                i += 1
                continue
            if A[i] > B[j]:
                splits += len(A)-i
                sordet.append(B[j])
                j += 1
        if i < len(A):
            sordet.extend(A[i:])
        else:
            sordet.extend(B[j:])
        tot = lnr + splits
        return tot, sordet

print(findinversions(Ints)[0])