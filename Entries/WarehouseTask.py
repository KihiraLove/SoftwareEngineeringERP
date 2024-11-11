from xmlrpc.client import DateTime

from Entries.Bases.WarehouseTaskBase import WarehouseTaskBase


class Shelf(WarehouseTaskBase):
    # Don't forget to document this
    def __init__(self, id: int, date: DateTime, status: str, sales_order_id: int, user_id: int) -> None:
        super().__init__(id, date, status)
        self.sales_order_id = sales_order_id
        self.user_id = user_id
        return

    def get_id(self) -> int:
        return self.id

    def get_date(self) -> DateTime:
        return self.date

    def get_status(self) -> str:
        return self.status

    def get_sales_order_id(self) -> int:
        return self.sales_order_id

    def get_user_id(self) -> int:
        return self.user_id
