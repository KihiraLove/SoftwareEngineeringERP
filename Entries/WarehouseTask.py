from xmlrpc.client import DateTime

from Entries.Bases.WarehouseTaskBase import WarehouseTaskBase


class Shelf(WarehouseTaskBase):
    # Don't forget to document this
    def __init__(self, id: int, date: DateTime, status: str, sales_order_id: int, user_id: int) -> None:
        super().__init__(id, date, status)
        self.sales_order_id = sales_order_id
        self.user_id = user_id
