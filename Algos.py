from Class import *
from various_functions import*
import copy
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

'''
def Prim(Starting_Vertex,Adjency_matrix,station_list):
    adj_mat=copy.deepcopy(Adjency_matrix)
    station_name = "1"#Starting_Vertex.identifier
    previous_station=[]
    new_tree = [[None] * len(station_list) for _ in range(len(station_list))]
    station_index = station_list.index(station_name)
    fin=1
    while len(previous_station) != len(station_list):
        value = None
        for i in range(len(adj_mat[station_index])):
            current_value = adj_mat[station_index][i]
            if current_value != 0 and current_value != None:
                print(current_value)
                if value == None or value ==0 and i not in previous_station:
                    value = current_value
                    nouveau_noeud=i
                if current_value < value and i not in previous_station:
                    value = current_value
                    nouveau_noeud=i
        if value==None:
            station_index = station_list[-fin]
            fin+=1
        else :
            new_tree[station_index][nouveau_noeud] = value
            previous_station.append(station_index)
            station_index=nouveau_noeud
            fin=1
        reussi=False
        print(previous_station)
        if not reussi:
            del previous_station[-1]
    return new_tree
'''