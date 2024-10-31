from dataclasses import dataclass
from xmlrpc.client import DateTime


@dataclass
class SalesOrderBase:
    """
    Data class, do not use directly
    """
    def __init__(self, id: int, date: DateTime, status: str) -> None:
        self.id = id
        self.date = date
        self.status = status