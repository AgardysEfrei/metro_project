import unicodedata as uni  # Importation du module unicodedata pour manipuler les caractères Unicode.
import networkx as nx  # Importation du module NetworkX pour la manipulation de graphes.
from matplotlib import pyplot as plt
import Algos
import Parsing
from Class import *

# Fonction pour supprimer les accents d'un texte
def remove_accents(text):
    # Encodage du texte en 'latin', et gestion des erreurs d'encodage en remplaçant les caractères invalides.
    text = text.encode('latin', errors='replace')

    # Décodage du texte en UTF-8 en remplaçant les erreurs par des caractères de remplacement.
    text = text.decode('utf-8', errors='replace')

    # Normalisation NFD (Normalization Form Decomposed) pour décomposer les caractères accentués en caractères de base + accents.
    text_without_accent = uni.normalize('NFD', text)

    # Création du résultat en filtrant les caractères ayant la catégorie 'Mn' (les marques diacritiques, i.e. accents).
    result = ''.join(char for char in text_without_accent if uni.category(char) != 'Mn')

    # Si des caractères de remplacement (�? ou d'autres erreurs) sont présents dans le texte, on les remplace par 'E'.
    if "�?" in result:
        result = result.replace("�?", 'E')

    # Retourner le texte sans accents.
    return result


# Fonction pour obtenir les stations suivantes à partir de la liste des segments
def get_next_stations(station_list, station, segments_list):
    # Liste pour stocker les stations suivantes
    next_stations_list = []

    # Parcourir tous les segments dans la liste des segments
    for segment in segments_list:
        # Parcourir tous les vertices associés à la station
        for vertex in station.vertex:
            # Récupérer les stations de début et de fin du segment
            station0 = get_station_by_vertex_nb(station_list, segment.stations[0])
            station1 = get_station_by_vertex_nb(station_list, segment.stations[1])

            # Si le vertex correspond à la station de départ du segment, et que la station1 n'est pas déjà dans la liste des stations suivantes,
            # et que l'identifiant de la station1 n'est pas celui de la station actuelle, on l'ajoute à la liste.
            if vertex[1] == segment.stations[0] and station1 not in next_stations_list and station1.identifier != station.identifier:
                next_stations_list.append(get_station_by_vertex_nb(station_list, segment.stations[1]))

            # Si le vertex correspond à la station de fin du segment, et que la station0 n'est pas déjà dans la liste des stations suivantes,
            # et que l'identifiant de la station0 n'est pas celui de la station actuelle, on l'ajoute à la liste.
            elif vertex[1] == segment.stations[1] and station0 not in next_stations_list and station0.identifier != station.identifier:
                next_stations_list.append(get_station_by_vertex_nb(station_list, segment.stations[0]))

    # Retourner la liste des stations suivantes.
    return next_stations_list


# Fonction pour récupérer une station par son numéro de vertex
def get_station_by_vertex_nb(stations_list, vertex_nb):  # Par exemple 0002 ou 0034
    # Parcourir chaque station dans la liste des stations
    for station in stations_list:
        # Vérifier si le numéro du vertex correspond à celui de la station
        for vertex in station.vertex:
            if vertex_nb == vertex[1]:
                return station  # Retourner la station si on trouve une correspondance.

    # Retourner None si la station n'a pas été trouvée.
    return None

# Fonction pour obtenir une liste des identifiants de toutes les stations
def stations_list(station_list):
    st_list = []  # Liste vide pour stocker les identifiants des stations
    for station in station_list:
        st_list.append(station.identifier)  # Ajouter l'identifiant de chaque station à la liste
    return st_list  # Retourner la liste des identifiants des stations

def affichage_graphique(vertex_list,adjancy_matrix):
    graph=nx.Graph()
    edges_tuple=[]
    for edge in range(len(adjancy_matrix)):
        for sub_edge in range(len(adjancy_matrix[edge])):
            if adjancy_matrix[edge][sub_edge] != None and adjancy_matrix[edge][sub_edge]!=0:
                edges_tuple.append((vertex_list[edge],vertex_list[sub_edge]))
    graph.add_nodes_from(vertex_list)
    graph.add_edges_from(edges_tuple)
    nx.draw(graph,nx.spring_layout(graph,k=0.8,scale=10),with_labels=True,node_color='lightblue')
    plt.title("Graphique")
    plt.figure(figsize=(50,50))
    plt.show()
def plus_court_chemin(depart,arrive,listofstation):
    print("Vous etes a",depart)
    station_arrive=arrive
    chemin=[]
    edges= Parsing.return_edges()
    index_arrive=listofstation.index(arrive)
    BellmanOutput=Algos.Bellman_ford(Parsing.return_stations(),Algos.get_edges(edges),listofstation.index(depart))
    temps=BellmanOutput[0][listofstation.index(arrive)]
    while(BellmanOutput[1][index_arrive]!=None):
        chemin.append(arrive)
        arrive=BellmanOutput[1][index_arrive]
        index_arrive = arrive
    del chemin[0]
    Sta=Parsing.return_stations()
    Ed=Parsing.return_edges()
    ligne=Sta[listofstation.index(depart)].lines[0]
    chemin=chemin[::-1]
    for i in range(len(chemin)-1):
        if ligne not in Sta[chemin[i+1]].lines:
            next_sta=get_next_stations(Sta, Sta[chemin[i]],Ed)
            for y in next_sta:
                if y.identifier == Sta[chemin[i+1]].identifier:
                        for z in y.lines:
                            if z in Sta[chemin[i+1]].lines:
                                ligne=z
            print("A ",listofstation[chemin[i]],"changez et prenez la ligne",ligne)
    print("Vous devriez arriver a",station_arrive,"dans environ",int(temps/60),"minutes")