from core.node import Node
from core.edge import Edge
from storage.wal import WAL


class GraphDB:
    def __init__(self):
        self.nodes = {}      # id  Node
        self.edges = []      # list of Edge
        self.node_id = 1     # auto increment
        self.wal = WAL()


    # CREATE NODE
    def create_node(self, label, properties):
        node = Node(self.node_id, label, properties)
        self.nodes[self.node_id] = node

        # WAL LOG
        self.wal.log({
            "action": "create_node",
            "id": self.node_id,
            "label": label,
            "properties": properties
        })

        self.node_id += 1
        return node

    # CREATE EDGE

    def create_edge(self, src_id, dst_id, label, properties):
        if src_id not in self.nodes or dst_id not in self.nodes:
            raise ValueError("Invalid node id")

        edge = Edge(src_id, dst_id, label, properties)
        self.edges.append(edge)

        # WAL LOG
        self.wal.log({
            "action": "create_edge",
            "src": src_id,
            "dst": dst_id,
            "label": label,
            "properties": properties
        })

        return edge


    # GET NEIGHBORS

    def get_neighbors(self, node_id, edge_label=None):
        neighbors = []

        for edge in self.edges:
            if edge.src == node_id:
                if edge_label is None or edge.label == edge_label:
                    neighbors.append(edge.dst)

        return neighbors


    # DEBUG PRINT

    def show(self):
        print("\nNodes:")
        for node in self.nodes.values():
            print(node)

        print("\nEdges:")
        for edge in self.edges:
            print(edge)


if __name__ == "__main__":
    db = GraphDB()

    # create nodes
    alice = db.create_node("Person", {"name": "Alice"})
    bob = db.create_node("Person", {"name": "Bob"})

    # create edge
    db.create_edge(alice.id, bob.id, "FRIENDS_WITH", {"since": 2021})

    # show data
    db.show()

    # neighbors
    print("\nNeighbors of Alice:", db.get_neighbors(alice.id))