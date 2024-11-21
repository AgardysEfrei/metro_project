from Parsing import *
from Algos import *
import unicodedata as uni
from various_functions import *
adjency_matrix = return_adjacency_matrix()
stationslist = return_stations()
listofstation = stations_list(stationslist)
plus_court_chemin(listofstation[4],"Villejuif, P. Vaillant Couturier",listofstation)