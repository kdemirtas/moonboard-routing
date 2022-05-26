import unittest

from moonboard_routing.solver.algorithms.network import functions as nf
from moonboard_routing.solver.classes.graph import HyperNode, HyperpathNode
from moonboard_routing.solver.classes.solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        node1 = HyperpathNode("1", ["A3", "B4", "A1", "B1"])
        node2 = HyperpathNode("2", ["A3", "C5", "A1", "B1"], pred=node1)
        node1.next = node2
        node3 = HyperpathNode("3", ["A3", "C5", "A1", "C2"], pred=node2)
        node2.next = node3
        node4 = HyperpathNode("4", ["B5", "C5", "A1", "C2"], pred=node3)
        node3.next = node4
        node5 = HyperpathNode("5", ["B5", "C5", "B2", "C2"], pred=node4)
        node4.next = node5
        hyperpath_root = node1
        self.solution = Solution(hyperpath_root=hyperpath_root)

    def tearDown(self) -> None:
        pass

    def test_solution_decode_path(self):
        decoded_path = self.solution.decoded_path
        self.assertListEqual(decoded_path, [['-', 'B4->C5', '-', '-'], ['-', '-', '-', 'B1->C2'], ['A3->B5', '-', '-', '-'], ['-', '-', 'A1->B2', '-']])
