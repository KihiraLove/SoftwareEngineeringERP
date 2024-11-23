from Entries.Bases.UserBase import UserBase
from Enums.UserType import UserType, parse_user_type


class User(UserBase):
    # Don't forget to document this
    def __init__(self, id: int, name: str, email: str, password: str, user_type: UserType) -> None:
        super().__init__(id, name, email, password, user_type)
        return

    def __repr__(self):
        return (f"{{"
                f"\"id\": \"{self.id}\","
                f"\"name\": \"{self.name}\","
                f"\"email\": \"{self.email}\","
                f"\"password\": \"{self.password}\","
                f"\"user_type\": \"{self.user_type}\""
                f"}}")

    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_password(self) -> str:
        return self.password

    def get_user_type(self) -> UserType:
        return self.user_type


def from_string(string_array: list[str]) -> User:
    id = int(string_array[0])
    name = string_array[1]
    email = string_array[2]
    password = string_array[3]
    user_type = parse_user_type(string_array[4])
    return User(id, name, email, password, user_type)