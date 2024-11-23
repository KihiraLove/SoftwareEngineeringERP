from Entries.Bases.SalesPersonBase import SalesPersonBase


class SalesPerson(SalesPersonBase):
    # Don't forget to document this
    def __init__(self, id: int, name: str, phone_number: str, email: str, is_internal: bool) -> None:
        super().__init__(id, name, phone_number, email, is_internal)
        return

    def __repr__(self):
        return (f"{{"
                f"\"id\": \"{self.id}\","
                f"\"name\": \"{self.name}\","
                f"\"phone_number\": \"{self.phone_number}\","
                f"\"email\": \"{self.email}\","
                f"\"is_internal\": \"{self.is_internal}\""
                f"}}")

    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_phone_number(self) -> str:
        return self.phone_number

    def get_email(self) -> str:
        return self.email

    def get_is_internal(self) -> bool:
        return self.is_internal


def from_string(string_array: list[str]) -> SalesPerson:
    id = int(string_array[0])
    name = string_array[1]
    phone_number = string_array[2]
    email = string_array[3]
    is_internal = True if string_array[4] == "True" else False
    return SalesPerson(id, name, phone_number, email, is_internal)