from dataclasses import dataclass

@dataclass
class User:
    """
    Data class, do not use directly
    """
    def __init__(self, id: int, name: str, min_stock: int, stock: int) -> None:
        self.id = id
        self.name = name
        self.min_stock = min_stock
        self.stock = stock