from dataclasses import dataclass

@dataclass
class User:
    """
    Data class, do not use directly
    """
    def __init__(self, id: int, name: str, password: str, access: list[str]) -> None:
        self.id = id
        self.name = name
        self.password = password
        self.access = access
