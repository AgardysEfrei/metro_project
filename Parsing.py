def return_vertex_from_file():
    matrix=[]
    with open("Source/source_projet_metro/metro","r") as vertex:
        for line in vertex:
            print(vertex.readline())
