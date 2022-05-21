from moonboard_routing.graph import node, edge


def extract_moves(hypernode1:node.HyperNode, hypernode2:node.HyperNode) -> list:
    repr1 = hypernode1.quadruple
    repr2 = hypernode2.quadruple

    if repr1 == repr2:
        # two hypernodes are identical, return an empty list
        return []

