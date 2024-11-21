from Class import *  # Importation des classes nécessaires
from various_functions import *  # Importation des fonctions utilitaires

def there_is_name(name, stationList):
    # Vérifie si une station avec le nom spécifié existe déjà dans la liste 'stationList'
    if len(stationList) == 0:
        # Si la liste est vide, retourne False et un indice -1
        return False, -1
    else:
        # Parcours la liste des stations et vérifie si le nom de la station correspond
        for i in range(len(stationList)):
            if stationList[i].get_name() == name:
                # Si le nom correspond, retourne True et l'indice de la station
                return True, i
        # Si aucune station ne correspond, retourne False et -1
        return False, -1


def return_stations():
    # Fonction qui retourne une liste d'objets Stations à partir du fichier source
    vertex_list = []  # Liste des stations
    identifier = 0  # Initialisation de l'identifiant de la station
    with open("Source/Sources projet métro/metro", "r") as vertex:
        # Ouverture du fichier contenant les données des stations
        for station in vertex:
            if station[0] == "V":  # Si la ligne correspond à une station (commence par "V")
                station = station.split(";")  # Sépare les valeurs par ';'
                station[-1] = station[-1][:-1]  # Enlève le saut de ligne à la fin de la dernière valeur
                station_id = int(station[1])  # Récupère l'identifiant de la station
                station_name = remove_accents(station[2])  # Enlève les accents du nom de la station
                if "bis" in station[3]:
                    station_line = int(station[3][0]) * 10  # Si "bis" est dans le nom de ligne, on multiplie par 10
                else:
                    station_line = int(station[3])  # Sinon, on prend la ligne telle quelle
                station_is_terminal = bool(station[4])  # Récupère si la station est terminale
                station_fork = int(station[5])  # Récupère l'information sur la fourche
                if there_is_name(station_name, vertex_list)[0]:
                    # Si une station avec ce nom existe déjà, on ajoute les informations à cette station
                    hint = there_is_name(station_name, vertex_list)[1]
                    vertex_list[hint].add_lines(station_line, station_id, station_is_terminal, station_fork)
                else:
                    # Sinon, on crée une nouvelle station et on l'ajoute à la liste
                    stop = Stations(station_name, station_line, station_id, station_is_terminal, station_fork)
                    vertex_list.append(stop)
        return vertex_list  # Retourne la liste des stations

def return_edges():
    # Fonction qui retourne une liste des segments (arêtes) à partir du fichier source
    edges_list = []  # Liste des segments
    with open("Source/Sources projet métro/metro", "r") as edges:
        # Ouverture du fichier contenant les données des segments
        for segment in edges:
            if segment[0] == "E":  # Si la ligne correspond à un segment (commence par "E")
                segment = segment.split(";")  # Sépare les valeurs par ';'
                segment_stations = (int(segment[1]), int(segment[2]))  # Récupère les stations de départ et d'arrivée
                segment_time = segment[3].replace('\n', "")  # Récupère le temps et enlève le saut de ligne
                edge = Segment(segment_stations, segment_time)  # Crée un objet Segment
                edges_list.append(edge)  # Ajoute le segment à la liste des arêtes
        return edges_list  # Retourne la liste des segments

def return_adjacency_matrix():
    # Fonction qui retourne la matrice d'adjacence des stations à partir des segments
    vertex = return_stations()  # Récupère la liste des stations
    segment = return_edges()  # Récupère la liste des segments
    stations = stations_list(vertex)  # Récupère la liste des stations sous une forme spécifique
    adjacency_matrix = [[None]*len(vertex) for _ in range(len(vertex))]
    # Crée une matrice d'adjacence initiale avec des valeurs 'None'
    for i in range(len(segment)):
        # Parcourt tous les segments
        depart = get_station_by_vertex_nb(vertex, segment[i].stations[0])  # Récupère la station de départ du segment
        index_depart = stations.index(depart.identifier)  # Trouve l'indice de la station de départ
        arrive = get_station_by_vertex_nb(vertex, segment[i].stations[1])  # Récupère la station d'arrivée du segment
        index_arrive = stations.index(arrive.identifier)  # Trouve l'indice de la station d'arrivée
        value = segment[i].time  # Récupère le temps de transit pour ce segment
        adjacency_matrix[index_depart][index_arrive] = value  # Remplie la matrice d'adjacence pour le départ -> arrivée
        adjacency_matrix[index_arrive][index_depart] = value  # Remplie la matrice d'adjacence pour l'arrivée -> départ
        adjacency_matrix[index_depart][index_depart] = 0
        adjacency_matrix[index_arrive][index_arrive] = 0
    return adjacency_matrix  # Retourne la matrice d'adjacence
