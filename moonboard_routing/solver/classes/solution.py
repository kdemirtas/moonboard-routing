class Solution:
    def __init__(self, hyperpath: list) -> None:
        """Initializes a Solution instance.

        Args:
            hyperpath (list): List of HyperNodes from start to destination.
        """
        self.hyperpath = hyperpath
        self._decoded_path = self._decode_path(self.hyperpath)

    def _decode_path(self):
        # Decodes the hyperpath and returns the individual movement in order
        pass

    @property
    def decoded_path(self):
        return self._decode_path