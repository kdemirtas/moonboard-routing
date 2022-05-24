import unittest

from moonboard_routing.solver.algorithms.network import functions as nf
from moonboard_routing.solver.classes.graph import HyperNode, HyperpathNode
from moonboard_routing.solver.classes.exceptions import MoveInfeasibleError


class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_hyperpathnode_inheritance(self):
        node = HyperpathNode("1", ["A3", "B4", "A1", "B1"])
        self.assertEqual(node.hypernode_id, "1")
        self.assertIsNone(node.next)
        