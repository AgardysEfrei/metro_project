from Class import *
from various_functions import*
from Parsing import*
import sys

def parcours_largeur():
    pass

def connexite(matrix, vertex):
    res = []
    p = []
    p.append(vertex)
    while(len(p) > 0):
        v = p.pop()
        if not v in res:
            res.append(v)
            print(matrix[v])
            for x in range(len(matrix[v])):
                if matrix[v][x] != None and not x in res:
                    p.append(x)
    return len(res) == len(matrix)
    

def Bellman_ford(vertexes, edges, s):
    dist = [sys.maxsize]*len(vertexes)
    pred = [None]*len(vertexes)
    stations = stations_list(vertexes)
    dist[s] = 0
    
    for k in range(1, len(vertexes) - 1):
        print("HERE RANGE")
        for edge in edges:
            u = stations.index(get_station_by_vertex_nb(vertexes, edge.stations[0]).identifier)
            v = stations.index(get_station_by_vertex_nb(vertexes, edge.stations[1]).identifier)
            print(u)
            print(v)
            if (dist[u] + int(edge.time)) < dist[v]:
                print("HERE")
                dist[v] = dist[u] + int(edge.time)
                pred[v] = u

    return (dist, pred) 


def Prim():
    pass

matrix = return_adjacency_matrix()

print(len(matrix))

print(connexite(matrix, 0))

vertexes = return_stations()
edges = return_edges()

print(Bellman_ford(vertexes, edges, 100))