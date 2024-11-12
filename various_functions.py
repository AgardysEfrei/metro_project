import unicodedata as uni


def remove_accents(text):
    text=text.encode('latin',errors='replace')
    text=text.decode('utf-8',errors='replace')
    text_without_accent=uni.normalize('NFD', text)
    result=''.join(char for char in text_without_accent if uni.category(char) != 'Mn')
    if "�?" in result:
        result = result.replace("�?",'E')
    return result


def get_next_stations(station_list, station, segments_list):
    next_stations_list = []
    for segment in segments_list:
        for vertex in station.vertex:
            station0 = get_station_by_vertex_nb(station_list, segment.stations[0])
            station1 = get_station_by_vertex_nb(station_list, segment.stations[1])
            if vertex[1] == segment.stations[0] and station1 not in next_stations_list and station1.identifier != station.identifier:
                next_stations_list.append(get_station_by_vertex_nb(station_list, segment.stations[1]))
            elif vertex[1] == segment.stations[1] and station0 not in next_stations_list and station0.identifier != station.identifier:
                next_stations_list.append(get_station_by_vertex_nb(station_list, segment.stations[0]))
    return next_stations_list



def get_station_by_vertex_nb(stations_list, vertex_nb): # example 0002 or 0034
    for station in stations_list:
        for vertex in station.vertex:
            if vertex_nb == vertex[1]:
                return station
    return None