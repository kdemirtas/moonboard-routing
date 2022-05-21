class MoveInfeasibleError(Exception):
    def __init__(self, message: str, errors: list) -> None:
        super().__init__(message, errors)


class Solution:
    def __init__(self, hyperpath: list) -> None:
        pass

