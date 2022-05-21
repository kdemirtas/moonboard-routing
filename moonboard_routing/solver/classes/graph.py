class Node:
    def __init__(self, node_id: str) -> None:
        self.node_id = node_id


class HyperNode:
    def __init__(self, hypernode_id: str, quadruple: list) -> None:
        self.hypernode_id = hypernode_id
        self.quadruple = quadruple


class Edge:
    def __init__(self, edge_id: str, from_node: Node, to_node: Node) -> None:
        self.edge_id = edge_id
        self.from_node = from_node
        self.to_node = to_node


class HyperEdge:
    def __init__(self, hyperedge_id: str, from_hypernode: HyperNode, to_hypernode: HyperNode) -> None:
        self.hyperedge_id = hyperedge_id
        self.from_hypernode = from_hypernode
        self.to_hypernode = to_hypernode