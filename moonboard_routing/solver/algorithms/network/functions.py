from moonboard_routing.solver.classes.graph import *
from moonboard_routing.solver.classes.exceptions import MoveInfeasibleError

def extract_moves(hypernode1:HyperNode, hypernode2:HyperNode) -> list:
    repr1 = hypernode1.quadruple
    repr2 = hypernode2.quadruple

    moves = []
    if repr1 == repr2:
        # two hypernodes are identical, return an empty list
        return moves
    
    for i in range(len(repr1)):
        move_components = ["left-hand", "right-hand", "left-foot", "right-foot"]
        moves.append(move_components[i],_extract_movement(repr1[i]), repr2[i])

    return moves
    
def _extract_movement(move_component:str, from_node:str, to_node:str, test=False, test_check=True):
    if from_node == to_node:
        return "-"
    else:
        if _is_move_feasible(move_component, from_node, to_node, test=test, test_check=test_check):
            movement = f"{from_node}->{to_node}"
            return movement
        else:
            movement = f"{from_node}->{to_node}"
            message = f"{move_component} movement {movement} is infeasible."
            errors = []
            raise(MoveInfeasibleError(message, errors))

def _is_move_feasible(move_component:str, from_node:str, to_node:str, test=False, test_check=True):
    # TODO check for feasibility of the move
    if test:
        return test_check

    return True