from various_functions import *
from Parsing import *
from Algos import *
import sys

run = True

while(run is True):

	print("--------------Bienvenue---------------")
	print()
	print("Choisissez une option :")
	print("A - vérifier la connexité du réseau de métro.")
	print("B - Calculer le plus court chemin d'une station à une autre\n(avec l'algorithme de Bellman-Ford).")
	print("C - Calculer l'abre couvrant de poids minimum du réseau de métro\n(avec l'algorithme de Prim).")
	print("D - Affichez le plan du réseau de métro.")
	print("E - Quittez")
	option = input()

	stations = return_stations()
	match option:
		case "A":
			if connexite(return_adjacency_matrix()):
				print("Le réseau de métro est connexe !")
			else:
				print("Le réseau de métro n'est pas connexe !")
		case "B":

			listofstation = stations_list(stations)

			start = input("Entrez un nom de station de départ: ")
			finish = input("Entrez un nomde station d'arrivée: ")

			station_start = None
			station_finish = None
			for station in stations:
				if station.identifier == start:
					station_start = start
				elif station.identifier == finish:
					station_finish = finish
			if station_start is not None and station_finish is not None:
				plus_court_chemin(station_start, station_finish, listofstation)
			else:
				print("Une de ces station n'existe pas")
		case "C":
			pass
			#Prim(, return_adjacency_matrix(), stations)
		case "D":
			affichage_graphique_all(stations, return_edges(), return_positions(stations))
		case "E":
			print("Au revoir !")
			run = False
