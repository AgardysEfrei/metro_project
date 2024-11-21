from various_functions import *
from Parsing import *
import sys

while(True):
	start = input("Entrez un nom de station de départ: ")
	finish = input("Entrez un nomde station d'arrivée: ")

	stations = return_stations()
	station_start = [station for station in stations if station.identifier == start]
	station_finish = [station for station in stations if station.identifier == finish]

	
	
	print(station_start[0].identifier)
	print(station_finish[0].identifier)
