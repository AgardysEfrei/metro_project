class Stations:
    def __init__(self,vertex,lines,is_terminal,fork):
        self.vertex=vertex
        self.nbr_line=lines
        self.is_terminal=is_terminal
        self.fork=fork