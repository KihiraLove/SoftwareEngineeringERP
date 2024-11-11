from Entries.Bases.BusinessPartnerBase import BusinessPartnerBase


class BusinessPartner(BusinessPartnerBase):
    # Don't forget to document this
    def __init__(self, id: int, company: str, address: str, sales_person_id: int) -> None:
        super().__init__(id, company, address)
        self.sales_person_id = sales_person_id
        return

    def get_id(self) -> int:
        return self.id

    def get_company(self) -> str:
        return self.company

    def get_address(self) -> str:
        return self.address

    def get_sales_person_id(self) -> int:
        return self.sales_person_id