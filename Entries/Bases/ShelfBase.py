from dataclasses import dataclass


@dataclass
class ShelfBase:
    """
    Data class, do not use directly
    """
    def __init__(self, id: int, location: str) -> None:
        self.id = id
        self.location = location
        return