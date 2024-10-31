from Entries.Bases.BusinessPartnerBase import BusinessPartnerBase


class BusinessPartner(BusinessPartnerBase):
    # Don't forget to document this
    def __init__(self, id: int, company: str, address: str, sales_person_id: int) -> None:
        super().__init__(id, company, address)
        self.sales_person_id = sales_person_id