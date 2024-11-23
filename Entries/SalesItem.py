from typing import Self
from Entries.Bases.SalesItemBase import SalesItemBase


class SalesItem(SalesItemBase):
    """
    Data class for Sales Item type
    """
    def __init__(self, id: int, amount: int, material_id: int, sales_order_id: int) -> None:
        super().__init__(id, amount)
        self.material_id = material_id
        self.sales_order_id = sales_order_id
        return

    def __repr__(self):
        return (f"{{"
                f"\"id\": \"{self.id}\","
                f"\"amount\": \"{self.amount}\","
                f"\"material_id\": \"{self.material_id}\","
                f"\"sales_order_id\": \"{self.sales_order_id}\""
                f"}}")

    def get_id(self) -> int:
        return self.id

    def get_amount(self) -> int:
        return self.amount

    def get_material_id(self) -> int:
        return self.material_id

    def get_sales_order_id(self) -> int:
        return self.sales_order_id

    @classmethod
    def from_string_list(cls, string_list: list[str]) -> Self:
        id = int(string_list[0])
        amount = int(string_list[1])
        material_id = int(string_list[2]) if string_list[3] != "None" else None
        sales_order_id = int(string_list[3]) if string_list[3] != "None" else None
        return SalesItem(id, amount, material_id, sales_order_id)