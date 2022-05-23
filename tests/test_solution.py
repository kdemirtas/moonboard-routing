import unittest

from moonboard_routing.solver.algorithms.network import functions as nf
from moonboard_routing.solver.classes.graph import HyperNode, HyperEdge
from moonboard_routing.solver.classes.solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        hyperpath = []
        self.solution = Solution(hyperpath=hyperpath)

    def tearDown(self) -> None:
        pass

    def test_solution_decode_path(self):
        pass