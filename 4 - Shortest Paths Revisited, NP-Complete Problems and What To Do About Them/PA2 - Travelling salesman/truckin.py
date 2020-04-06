import numpy as np
from tqdm import tqdm
from math import sqrt

with open("tsp.txt") as file:
        num_cities = int(file.readline().strip('\n'))
        graph = {}
        for line in file.readlines():
            temp_list = list(map(float, line.strip('\n').split(' ')))
            graph[int(temp_list[0])] = (temp_list[1], temp_list[2])

def dist(x, y):
    distance = sqrt(pow(x[0] - y[0], 2) + pow(x[1] - y[1], 2))
    return distance

def Shortest(source, destination_cites, graph):
    dist_array = []
    for city in destination_cites:
        dist_array.append([city, dist(graph[source], graph[city])])
    dist_array = sorted(dist_array, key=lambda x: (x[1], x[0]))

    return dist_array[0]

def find_next(start_city, graph, visited2, set, tour):
    destination_cites = set - visited2
    (next, s_dist) = \
            Shortest(start_city, destination_cites, graph)
    visited2.add(next)
    tour += s_dist

    return  next, visited2, tour


def tsp(num_cities, graph):
    visited2 = set([1])
    set = set([i for i in range(1, num_cities + 1)])
    tour = 0
    next, visited2, tour_length = \
        find_next(1, graph, visited2, set, tour_length)
    while len(visited2) != num_cities:
        if (len(visited2) -1) % 1000 == 0:
            print("Been trucking through %d cities'%len(visited2))
        next, visited2, tour_length = \
            find_next(next, graph, visited2, set, tour_length)
    last_hop = dist(graph[next], graph[1])
    tour_length += last_hop

    return tour_length

tour_length = tsp(num_cities, graph)
print(tour)