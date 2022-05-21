import unittest

from moonboard_routing.solver.methods.network import functions as nf
from moonboard_routing.graph import node, edge

class TestNetworkFunctions(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_extract_moves_returns_empty_list_for_no_move(self):
        hn1 = node.HyperNode("Hypernode1", ["A3", "B4", "A1", "B1"])
        hn2 = node.HyperNode("Hypernode2", ["A3", "B4", "A1", "B1"])

        moves = nf.extract_moves(hn1, hn2)
        self.assertEqual(moves, [])