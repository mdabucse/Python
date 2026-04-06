class Edge:
    def __init__(self, src, dst, label, properties):
        self.src = src          # source node id
        self.dst = dst          # destination node id
        self.label = label      # relationship type
        self.properties = properties

    def __repr__(self):
        return f"{self.src} -[{self.label}]-> {self.dst} {self.properties}"