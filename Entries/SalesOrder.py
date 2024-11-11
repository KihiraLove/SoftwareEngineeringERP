from xmlrpc.client import DateTime

from Entries.Bases.SalesOrderBase import SalesOrderBase


class Shelf(SalesOrderBase):
    # Don't forget to document this
    def __init__(self, id: int, date: DateTime, status: str, is_inbound: bool, business_partner_id: int) -> None:
        super().__init__(id, date, status, is_inbound)
        self.business_partner_id = business_partner_id