from Class import *
import various_functions
import copy
import Parsing
import sys


def get_edges(edges_list):
    vertices = Parsing.return_stations()
    stations = various_functions.stations_list(vertices)
    res = []
    for edge in edges_list:
        u = stations.index(various_functions.get_station_by_vertex_nb(vertices, edge.stations[0]).identifier)
        v = stations.index(various_functions.get_station_by_vertex_nb(vertices, edge.stations[1]).identifier)
        time = edge.time
        res.append([u,v,int(time)])
        res.append([v,u,int(time)])
    return res

def parcours_largeur():
    pass

def connexite(matrix):
    res = []
    p = []
    p.append(0)
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
    stations = various_functions.stations_list(vertices)
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


def Prim(Starting_Vertex,Adjency_matrix,station_list):
    new_tree=[[None]*len(Adjency_matrix) for _ in range(len(Adjency_matrix))]
    CC = []
    CC.append(station_list.index(Starting_Vertex))
    M = []
    for i in station_list:
        M.append(station_list.index(i))
    M.remove(CC[0])
    while len(M) != 0:
        value = 0
        for i in CC:
            for j in M:
                current_value = Adjency_matrix[i][j]
                if current_value != None and current_value != 0:
                    if value == 0:
                        value = current_value
                        station_depart=i
                        station_to_append=j
                    if current_value < value:
                        station_depart=i
                        value = current_value
                        station_to_append = j
        CC.append(station_to_append)
        new_tree[station_depart][station_to_append] = value
        M.remove(station_to_append)
    return new_tree