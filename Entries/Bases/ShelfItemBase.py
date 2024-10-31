from dataclasses import dataclass

@dataclass
class ShelfItemBase:
    """
    Data class, do not use directly
    """
    def __init__(self, id: int, amount: int) -> None:
        self.id = id
        self.amount = amount