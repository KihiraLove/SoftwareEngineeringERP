from dataclasses import dataclass

from Enums.UserType import UserType


@dataclass
class UserBase:
    """
    Data class, do not use directly
    """
    def __init__(self, id: int, name: str, password: str, user_type: UserType) -> None:
        self.id = id
        self.name = name
        self.password = password
        self.user_type = user_type
        return