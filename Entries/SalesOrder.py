from dataclasses import dataclass
from xmlrpc.client import DateTime


@dataclass
class Material:
    """
    Data class, do not use directly
    """
    def __init__(self, id: int, bp_id: int, material: str, amount: int, date: DateTime, status: str) -> None:
        self.id = id
        self.bp_id = bp_id
        self.material = material
        self.amount = amount
        self.date = date
        self.status = status