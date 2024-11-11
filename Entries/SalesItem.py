from Entries.Bases.SalesItemBase import SalesItemBase


class SalesItem(SalesItemBase):
    def __init__(self, id: int, amount: int, material_id: int, sales_order_id: int) -> None:
        super().__init__(id, amount)
        self.material_id = material_id
        self.sales_order_id = sales_order_id
        return

    def get_id(self) -> int:
        return self.id

    def get_amount(self) -> int:
        return self.amount

    def get_material_id(self) -> int:
        return self.material_id

    def get_sales_order_id(self) -> int:
        return self.sales_order_id