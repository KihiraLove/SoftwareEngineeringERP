from xmlrpc.client import DateTime

from Entries.Bases.SalesOrderBase import SalesOrderBase


class Shelf(SalesOrderBase):
    # Don't forget to document this
    def __init__(self, id: int, date: DateTime, status: str, is_inbound: bool, business_partner_id: int) -> None:
        super().__init__(id, date, status, is_inbound)
        self.business_partner_id = business_partner_id
        return

    def get_id(self) -> int:
        return self.id

    def get_date(self) -> DateTime:
        return self.date

    def get_status(self) -> str:
        return self.status

    def get_is_inbound(self) -> bool:
        return self.is_inbound

    def get_business_partner_id(self) -> int:
        return self.business_partner_id