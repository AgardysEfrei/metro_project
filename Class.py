class Stations:
    def __init__(self, identifier, lines, vertex, is_terminal, fork):
        # Initialisation de l'objet Station avec les paramètres suivants:
        # identifier (str) : Identifiant de la station
        # lines (list[int]) : Liste des lignes associées à cette station
        # vertex (list[tuple[int]]) : Liste des tuples représentant les relations (ligne, identifiant du sommet) pour chaque ligne
        # is_terminal (list[tuple[bool]]) : Liste des tuples représentant si une station est terminale pour chaque ligne
        # fork (list[tuple[int]]) : Liste des tuples représentant les fourches (ligne, fourche)

        self.lines = [lines]  # Crée une liste contenant 'lines'
        self.identifier = identifier  # Assigne l'identifiant de la station
        self.vertex = [(lines, vertex)]  # Crée une liste de tuples (ligne, sommet)
        self.is_terminal = [(lines, is_terminal)]  # Crée une liste de tuples (ligne, terminal)
        self.fork = [(lines, fork)]  # Crée une liste de tuples (ligne, fourche)

    def add_lines(self, lines, vertex, is_terminal, fork):
        # Méthode pour ajouter de nouvelles lignes, sommets, informations terminales et fourches
        self.lines.append(lines)  # Ajoute une nouvelle ligne
        self.vertex.append((lines, vertex))  # Ajoute un nouveau tuple (ligne, sommet)
        self.is_terminal.append((lines, is_terminal))  # Ajoute un nouveau tuple (ligne, terminal)
        self.fork.append((lines, fork))  # Ajoute un nouveau tuple (ligne, fourche)

    def get_name(self):
        # Retourne l'identifiant de la station
        return self.identifier

    def __str__(self):
        # Redéfinit la méthode __str__ pour afficher les informations de la station
        for i in range(len(self.lines)):  # Parcourt toutes les lignes
            if self.lines[i] > 19:  # Si le numéro de ligne est supérieur à 19
                self.lines[i] = str(
                    int(self.lines[i] / 10)) + "bis"  # Modifie la ligne pour ajouter "bis" après l'unité
        # Retourne une chaîne formatée pour afficher les informations de la station
        return f"Stations:{self.identifier}\nLignes:{self.lines}\nVertex:{self.vertex}\nFork:{self.fork}\nTerminal:{self.is_terminal}"


class Segment:
    def __init__(self, stations, time):
        # Initialisation de l'objet Segment avec les paramètres suivants:
        # stations : Liste des stations dans le segment
        # time : Temps de transit entre ces stations
        self.stations = stations  # Liste des stations du segment
        self.time = time  # Temps associé à ce segment

    def get_stations(self):
        # Retourne la liste des stations du segment
        return self.stations

    def get_time(self):
        # Retourne le temps du segment
        return self.time

    def __str__(self):
        # Redéfinit la méthode __str__ pour afficher les informations du segment
        return f"Stations:{self.stations}\nTime:{self.time}"
