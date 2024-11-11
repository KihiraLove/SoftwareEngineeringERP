from Entries.Bases.UserBase import UserBase


class User(UserBase):
    # Don't forget to document this
    def __init__(self, id: int, name: str, password: str, user_type: str) -> None:
        super().__init__(id, name, password, user_type)