from Class import *

def return_stations():
    vertex_list=[]
    identifier = 0
    with open("Source/Sources projet métro/metro","r") as vertex:
        for station in vertex:
            if station[0]=="V":
                station=station.split(";")
                station[-1] = station[-1][:-1]
                station_id=station[1]
                station_name=station[2]
                if("bis" in station[3]):
                    station_line=int(station[3][0])*10
                else:
                    station_line=int(station[3])
                station_is_terminal=bool(station[4])
                station_fork=int(station[5])
                if there_is_name(station_name,vertex_list)[0]:
                    hint=there_is_name(station_name,vertex_list)[1]
                    vertex_list[hint].add_lines(station_line,station_id,station_is_terminal,station_fork)
                else:
                    stop=Stations(station_name,station_line,station_id,station_is_terminal,station_fork)
                    vertex_list.append(stop)
        return vertex_list
def return_adjacency_matrix_from_file():
    max = return_max()
    matrix=[[None for i in range(max+1)] for i in range(max+1)]
    with open("Source/Sources projet métro/metro","r") as vertex:
        for lines in vertex.readlines():
            if lines[0]=="E":
                cache=lines
                cache=cache.split(";")
                cache[-1]=cache[-1][:-1] #On supprime les '\n'
                line = int(cache[1])
                column = int(cache[2])
                value = int(cache[3])
                matrix[line][column]=value
        return matrix

def return_max():
    max=0
    with open("Source/Sources projet métro/metro","r") as vertex:
        for lines in vertex.readlines():
            if lines[0]=="E":
                cache=lines;
                cache=cache.split(";")
                cache[-1]=cache[-1][:-1] #On supprime les '\n'
                line = int(cache[1])
                column = int(cache[2])
                if line>max:
                    max=line
                if column>max:
                    max=column
        return max

def there_is_name(name,stationList):
    if len(stationList)==0:
        return False,-1
    else :
        for i in range(len(stationList)):
            if stationList[i].get_name()==name:
                return True,i
        return False,-1
