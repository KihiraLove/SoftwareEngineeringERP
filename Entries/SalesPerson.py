from Entries.Bases.SalesPersonBase import SalesPersonBase


class BusinessPartner(SalesPersonBase):
    # Don't forget to document this
    def __init__(self, id: int, name: str, phone_number: str, email: str, is_internal: bool) -> None:
        super().__init__(id, name, phone_number, email, is_internal)