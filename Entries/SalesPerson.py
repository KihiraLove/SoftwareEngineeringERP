from Entries.Bases.SalesPersonBase import SalesPersonBase


class BusinessPartner(SalesPersonBase):
    # Don't forget to document this
    def __init__(self, id: int, name: str, phone_number: str, email: str, is_internal: bool) -> None:
        super().__init__(id, name, phone_number, email, is_internal)
        return

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