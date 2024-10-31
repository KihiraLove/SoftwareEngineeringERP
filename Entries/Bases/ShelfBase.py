from dataclasses import dataclass

@dataclass
class ShelfBase:
    """
    Data class, do not use directly
    """
    def __init__(self, id: int) -> None:
        self.id = id