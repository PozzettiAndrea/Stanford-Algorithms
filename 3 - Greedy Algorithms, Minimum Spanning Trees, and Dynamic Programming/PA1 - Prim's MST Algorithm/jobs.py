import copy

file = open("jobs.txt","r")
jobs = []

for i in file:
	jobs.append([int(i.split()[0]),int(i.split()[1])])

jobs2 = copy.deepcopy(jobs)
jobs.sort(key = lambda x: (x[1]-x[0])-0.0001*x[1]) #Apexoflaziness.jpg
jobs2.sort(key = lambda x: x[1]/x[0])


def completiontimesum(jobs):
    for i in range(len(jobs)-1):
        jobs[i+1][1] += jobs[i][1]
    
    product = 0
    
    for i in jobs:
        product += i[0] * i[1]
    
    return product
    
print(completiontimesum(jobs),completiontimesum(jobs2))