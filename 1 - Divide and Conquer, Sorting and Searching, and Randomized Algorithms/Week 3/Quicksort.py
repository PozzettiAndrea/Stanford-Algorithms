import numpy

File = open("QuickSort.txt","r")
Ints = File.readlines()

for i in range(len(Ints)):
    Ints[i] = int(Ints[i])

def CP1(arr):
    return arr[0]

def CP2(arr):
    return arr[-1]

def CP3(arr):
    return arr[0]

cs = 0
def Quicksort(arr,pivot):
    global cs
    if len(arr) <= 1:
        return arr
    else:
        if pivot == 0:
            i = 1
        else:
            i = 0
        for j in range(len(arr)):
            if j == pivot:
                pass
            else:
                cs += 1
                if arr[j] < arr[pivot]:
                    arr[j], arr[i] = arr[i], arr[j]
                    i += 1
        arr[pivot], arr[i-1] = arr[i-1], arr[pivot]
        print(arr)
        first_part = Quicksort(arr[:i-1],pivot)
        second_part = Quicksort(arr[i:],pivot)
        first_part.append(arr[i-1])
        return first_part + second_part


def Quicksort2(arr):
    global cs
    if len(arr) <= 1:
        return arr
    else:
        i = 0
        for j in range(len(arr)-1):
            cs += 1
            if arr[j] < arr[-1]:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1
        arr[-1], arr[i] = arr[i], arr[-1]
        print(arr)
        first_part = Quicksort2(arr[:i])
        second_part = Quicksort2(arr[i+1:])
        first_part.append(arr[i])
        return first_part + second_part


    
def Quicksort3(arr):
    global cs
    meh = len(arr)
    if meh <= 1:
        return arr
    else:
        alarm = 0
        i = 0
        pivot = numpy.median([arr[(meh//2)+(meh%2)-1],arr[0],arr[-1]])
        if pivot == arr[(meh//2)+(meh%2)-1]:
            pindex = (meh//2)+(meh%2)-1
        if pivot == arr[0]:
            pindex = 0
            i = 1
            alarm = 1
        if pivot == arr[-1]:
            pindex = -1
        print(pindex)
        for j in range(meh):
            if arr[j] == pivot:
                pass
            else:
                cs += 1
                if arr[j] < pivot:
                    arr[j], arr[i] = arr[i], arr[j]
                    i += 1
        if alarm == 1:
            i -= 1
        arr[pindex], arr[i] = arr[i], arr[pindex]
        print(arr)
        first_part = Quicksort3(arr[:i])
        second_part = Quicksort3(arr[i+1:])
        first_part.append(arr[i])
        return first_part + second_part

alist = [54,26,93,17,77,31,44,55,20]
print(Quicksort(Ints,0),cs)