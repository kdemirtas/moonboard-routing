class Node:
    """Node class for the raw moonboard network.
    """
    def __init__(self, node_id: str) -> None:
        """Initializes a Node instance.

        Args:
            node_id (str): Unique identifier of the node given in string (i.e., A1, B2, C5) Letter represents the column, number represents the row woth respect to the moonboard
        """
        self.node_id = node_id


class HyperNode:
    """HyperNode class for the Hypernetwork constructed after network transformation.
    Each HyperNode instance has a unique string identifier `hypernode_id` and a list (actually a quadruple)
    representing the position of the body components given in the order of (LH, RH, LF, RF)
    where LH, RH, LF, RF represent left-hand, right-hand, left-foot, right-foot positions given
    by the corresponding Node objects from the raw network.
    """
    def __init__(self, hypernode_id: str, quadruple: list) -> None:
        """Initializes a HyperNode instance.

        Args:
            hypernode_id (str): Unique identifier of the hypernode given in string
            quadruple (list): _List of Node instances_
        """
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