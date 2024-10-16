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

    def add_lines(self,lines,vertex,is_terminal,fork):
        self.lines.append(lines)
        self.vertex.append((lines,vertex))
        self.is_terminal.append((lines,is_terminal))
        self.fork.append((lines,fork))
    def get_name(self):
        return self.identifier

    def __str__(self):
        for i in range(len(self.lines)):
            if self.lines[i]>19:
                self.lines[i]=str(int(self.lines[i]/10))+"bis"
        return f"Stations:{self.identifier}\nLignes:{self.lines}\nVertex:{self.vertex}\nFork:{self.fork}\nTerminal:{self.is_terminal}"