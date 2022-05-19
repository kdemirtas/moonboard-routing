class Node:
    def __init__(self, node_id:str) -> None:
        self.node_id = node_id


class HyperNode:
    def __init__(self, hypernode_id:str, quadruple:list) -> None:
        self.hypernode_id = hypernode_id
        self.quadruple = quadruple