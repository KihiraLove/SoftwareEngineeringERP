from Entries.Bases.UserBase import UserBase
from Enums.UserType import UserType


class User(UserBase):
    # Don't forget to document this
    def __init__(self, id: int, name: str, password: str, user_type: UserType) -> None:
        super().__init__(id, name, password, user_type)
        return

    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_password(self) -> str:
        return self.password

    def get_user_type(self) -> UserType:
        return self.user_type