def return_vertex_from_file():
    max = return_max()
    matrix=[[0 for i in range(max+1)] for i in range(max+1)]
    with open("Source/Sources projet métro/metro","r") as vertex:
        for lines in vertex.readlines():
            if lines[0]=="E" and lines[2] != "n": #On évite d'ajouter la ligne 10 : E num_sommet1 num_sommet2 temps_en_secondes
                cache=lines;
                cache=cache.split(" ")
                cache[-1]=cache[-1][:-1] #On supprime les '\n'
                if cache[-1]=="":
                    cache.remove(cache[-1]) #Parfois, les lignes se terminent par un espace, on fait cette ligne pour supprimer les " " des listes
                line = int(cache[1])
                column = int(cache[2])
                value = int(cache[3])
                matrix[line][column]=value
        return matrix

def return_max():
    max=0
    with open("Source/Sources projet métro/metro","r") as vertex:
        for lines in vertex.readlines():
            if lines[0]=="E" and lines[2] != "n": #On évite d'ajouter la ligne 10 : E num_sommet1 num_sommet2 temps_en_secondes
                cache=lines;
                cache=cache.split(" ")
                cache[-1]=cache[-1][:-1] #On supprime les '\n'
                if cache[-1]=="":
                    cache.remove(cache[-1]) #Parfois, les lignes se terminent par un espace, on fait cette ligne pour supprimer les " " des listes
                line = int(cache[1])
                column = int(cache[2])
                if line>max:
                    max=line
                if column>max:
                    max=column
        return max
