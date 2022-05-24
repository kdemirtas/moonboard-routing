from moonboard_routing.solver.classes.graph import HyperpathNode


class Solution:
    def __init__(self, hyperpath_root: HyperpathNode) -> None:
        """Initializes a Solution instance.

        Args:
            hyperpath_root (HyperpathNode): Root hypernode of the hyperpath.
        """
        self.hyperpath_root = hyperpath_root
        self._decoded_path = self._decode_path(self.hyperpath_root)

    def _decode_path(self):
        # Decodes the hyperpath and returns the individual movement in order
        pass

    @property
    def decoded_path(self):
        return self._decode_path