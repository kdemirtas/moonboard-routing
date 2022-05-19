import node

class Edge:
    def __init__(self, edge_id:str, from_node:node.Node, to_node:node.Node) -> None:
        self.edge_id = edge_id
        self.from_node = from_node
        self.to_node = to_node


class HyperEdge:
    def __init__(self, hyperedge_id:str, from_hypernode:node.HyperNode, to_hypernode:node.HyperNode) -> None:
        self.hyperedge_id = hyperedge_id
        self.from_hypernode = from_hypernode
        self.to_hypernode = to_hypernode