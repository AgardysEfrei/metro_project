from various_functions import *
from Parsing import *
import sys

while(True):
	stations = return_stations()

	affichage_graphique_all(stations, return_edges(), return_positions(stations))

	start = input("Entrez un nom de station de départ: ")
	finish = input("Entrez un nomde station d'arrivée: ")

	station_start = [station for station in stations if station.identifier == start]
	station_finish = [station for station in stations if station.identifier == finish]

	print(station_start[0].identifier)
	print(station_finish[0].identifier)
