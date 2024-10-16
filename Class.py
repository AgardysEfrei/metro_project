class Stations:
    def __init__(self,identifier,lines,vertex,is_terminal,fork):
        #identifier str
        #lines list int
        #vertex list tuple int syntax: (line, vertex_identifier)
        #is_terminal list tuple boolean syntax: (line, is_terminal)
        #fork list tuple int syntax : (line, fork)
        self.lines = [lines]
        self.identifier = identifier
        self.vertex=[(lines,vertex)]
        self.is_terminal=[(lines,is_terminal)]
        self.fork=[(lines,fork)]