from moonboard_routing.solver.classes.graph import HyperpathNode
from moonboard_routing.solver.algorithms.network import functions as nf


class Solution:
    def __init__(self, hyperpath_root: HyperpathNode) -> None:
        """Initializes a Solution instance.

        Args:
            hyperpath_root (HyperpathNode): Root hypernode of the hyperpath.
        """
        self.hyperpath_root = hyperpath_root
        self._decoded_path = self._decode_path()

    def _decode_path(self):
        """Decodes the hyperpath and returns the individual movement in order

        Returns:
            list: List of strings representing the movement for each body component in ther order of
            LH, RH, LF, RF, where they stand for left-hand, right-hand, left-foot, right-foot, respectively.
            e.g. [-, A2->A3, -, -] represents ri\ght-hand movement from node A2 to node A3, where the
            other body components stay still, which is represented by -.
        """
        cur = self.hyperpath_root
        decoded_path = []
        while not cur.is_terminal():
            next = cur.next
            decoded_path.append(nf.extract_moves(cur, next))
            cur = cur.next
        
        return decoded_path

    @property
    def decoded_path(self):
        self._decoded_path = self._decode_path()
        return self._decoded_path