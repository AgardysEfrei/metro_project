from Class import *
from various_functions import*
from Parsing import*
import sys

def get_edges(edges_list):
    vertices = return_stations()
    stations = stations_list(vertices)
    res = []
    for edge in edges_list:
        u = stations.index(get_station_by_vertex_nb(vertices, edge.stations[0]).identifier)
        v = stations.index(get_station_by_vertex_nb(vertices, edge.stations[1]).identifier)
        time = edge.time
        res.append([u,v,int(time)])
        res.append([v,u,int(time)])
    return res

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
            for x in range(len(matrix[v])):
                if matrix[v][x] != None and not x in res:
                    p.append(x)
    return len(res) == len(matrix)
    

def Bellman_ford(vertices, edges, s):
    dist = [sys.maxsize]*len(vertices)
    pred = [None]*len(vertices)
    stations = stations_list(vertices)
    dist[s] = 0
    
    for k in range(1, len(vertices) - 1):
        for edge in edges:
            u = edge[0]
            v = edge[1]
            time = edge[2]
            if (dist[u] + time) < dist[v]:
                dist[v] = dist[u] + time
                pred[v] = u

    return (dist, pred) 


def Prim(vertices):
    key[0] = [sys.maxsize]*len(vertices)
    parent = [None]*len(vertices)

    key[0] = 0
    mstSet = [False]*len(vertices)

    for _ in range(len(vertices))

matrix = return_adjacency_matrix()

print(len(matrix))

print(connexite(matrix, 0))

vertices = return_stations()
edges = get_edges(return_edges())

res = Bellman_ford(vertices, edges, 0)

print(Bellman_ford(vertices, edges, 0))

print(res[0][251])