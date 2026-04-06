class Node:
    def __init__(self, id, label, properties):
        self.id = id
        self.label = label
        self.properties = properties

    def __repr__(self):
        return f"{self.label}#{self.id} {self.properties}"