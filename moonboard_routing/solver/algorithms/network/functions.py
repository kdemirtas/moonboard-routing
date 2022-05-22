from moonboard_routing.solver.classes.graph import *
from moonboard_routing.solver.classes.exceptions import MoveInfeasibleError

def extract_moves(hypernode1:HyperNode, hypernode2:HyperNode) -> list:
    """Extracts the individual body component movements for a move from
    hypernode1 to hypernode2 in the Hypernetwork.

    Args:
        hypernode1 (HyperNode): Origin node of the move in Hypernetwork
        hypernode2 (HyperNode): Destination node of the move in the Hypernetwork_

    Returns:
        list: List of strings representing the movement for each body component in ther order of
        LH, RH, LF, RF, where they stand for left-hand, right-hand, left-foot, right-foot, respectively.
        e.g. [-, A2->A3, -, -] represents right-hand movement from node A2 to node A3, where the
        other body components stay still, which is represented by -.
    """
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
    """Extracts the individual body component movement.

    Args:
        move_component (str): Body component performing the movement. Can be one of
        `left-hand`, `right-hand`, `left-foot`, or `right-foot`.
        from_node (str): Origin node of the corresponding move component in the raw network
        to_node (str): _Destination node of the corresponding move component in the raw network_
        test (bool, optional): Boolean variable to indicate if the function is used for test methods. Defaults to False.
        test_check (bool, optional): Boolean variable to be used in test checks. Defaults to True.

    Returns:
        movement (str): _String description of the movement. (e.g. A1->A2)
    """
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
    """Checks whether a move from `from_node` to `to_node` is feasible in the raw network
    for the given `move_component`. 

    Args:
        move_component (str): _description_
        from_node (str): _description_
        to_node (str): _description_
        test (bool, optional): _Boolean variable to indicate if the function is used for test methods. Defaults to False.
        test_check (bool, optional): Boolean variable to be used in test checks. Defaults to True.

    Returns:
        bool: True if move is feasible, False, otherwise.
    """
    # TODO check for feasibility of the move. Will probably need a predefined table indicating feasible and infeasible moves.
    if test:
        return test_check

    return True