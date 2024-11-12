import unicodedata as uni
from Parsing import*
import re
def remove_accents(text):
    text=text.encode('latin',errors='replace')
    text=text.decode('utf-8',errors='replace')
    text_without_accent=uni.normalize('NFD', text)
    result=''.join(char for char in text_without_accent if uni.category(char) != 'Mn')
    if "�?" in result:
        result = result.replace("�?",'E')
    return result

def get_next_stations():
    pass

def get_station_by_vertex_nb(): # example 0002 or 0034
    pass