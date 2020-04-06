import heapq
import time

numbaz = []

with open("Median.txt") as file:
    for number in file.read().splitlines():
        numbaz.append(int(number))

class Heap(object):
    def __init__(self, minormax):
        self._data = []
        self.minormax = minormax
        
    def push(self, num):
        if self.minormax == "max":
            heapq.heappush(self._data, -num)
        if self.minormax == "min":
            heapq.heappush(self._data, num)
    def pop(self):
        return heapq.heappop(self._data)

    def root(self):
        return self._data[0]
    
    def __str__(self):
        stringy = ""
        for i in self._data:
            stringy += str(i) + ","
        return stringy

    def __len__(self):
        return len(self._data)

# testheap = Heap("max")
# testheap.push(1)

# print(testheap.root())

class twoheaps:
    def __init__(self):
        self.bottomheap = Heap("max")
        self.topheap = Heap("min")

    def get_median(self):
        if len(self.topheap) == 0:
            return (-self.bottomheap.root())
        if (len(self.topheap) + len(self.bottomheap)) % 2 == 0:
            return (-self.bottomheap.root())
        else:
            if len(self.topheap)-len(self.bottomheap) == 1:
                return self.topheap.root()
            if len(self.topheap)-len(self.bottomheap) == -1:
                return -self.bottomheap.root()

    def _add_number(self, num):
        if len(self.bottomheap) == 0:
            self.bottomheap.push(num)
            return
        if num <= -self.bottomheap.root():
            self.bottomheap.push(num)
        else:
            self.topheap.push(num)
        if len(self.bottomheap) - len(self.topheap) > 1:
            self.topheap.push(-self.bottomheap.pop())
        elif len(self.bottomheap) - len(self.topheap) < -1:
            self.bottomheap.push(self.topheap.pop())

TH = twoheaps()

# for i in [1,2,3]:
#     TH._add_number(i)
# print(TH.bottomheap,TH.bottomheap.root(),TH.topheap,TH.topheap.root())
# print(TH.get_median())
MEDIANS = []
for i in numbaz:
    TH._add_number(i)
    MEDIANS.append(TH.get_median())
    # print("bottomheap:(" , TH.bottomheap, ")", "topheap:(", TH.topheap, ")")
    # print(TH.get_median())
    # time.sleep(1)
print(sum(MEDIANS)%10000)