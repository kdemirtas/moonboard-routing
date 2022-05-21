import unittest

from moonboard_routing.solver.algorithms.network import functions as nf
from moonboard_routing.solver.classes.graph import HyperNode, HyperEdge
from moonboard_routing.solver.classes.exceptions import MoveInfeasibleError


class TestNetworkFunctions(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_extract_moves_returns_empty_list_for_no_move(self):
        hn1 = HyperNode("Hypernode1", ["A3", "B4", "A1", "B1"])
        hn2 = HyperNode("Hypernode2", ["A3", "B4", "A1", "B1"])

        moves = nf.extract_moves(hn1, hn2)
        self.assertEqual(moves, [])

    def test_extract_movement_returns_dash_for_no_move(self):
        move_component = "left-hand"
        from_node = "A1"
        to_node = "A1"

        movement = nf._extract_movement(move_component, from_node, to_node)
        self.assertEqual(movement, "-")

    def test_extract_movement_returns_movement_for_feasible_move(self):
        move_component = "left-hand"
        from_node = "A1"
        to_node = "A2"

        movement = nf._extract_movement(move_component, from_node, to_node)
        self.assertEqual(movement, "A1->A2")

    def test_extract_raises_moveinfeasible_error_for_infeasible_move(self):
        move_component = "left-hand"
        from_node = "A1"
        to_node = "A2"

        with self.assertRaises(MoveInfeasibleError):
            movement = nf._extract_movement(move_component, from_node, to_node, test=True, test_check=False)