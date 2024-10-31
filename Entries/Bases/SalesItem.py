from Entries.Bases.SalesItemBase import SalesItemBase


class SalesItem(SalesItemBase):
    def __init__(self, id: int, amount: int, material_id: int, sales_order_id: int) -> None:
        super().__init__(id, amount)
        self.material_id = material_id
        self.sales_order_id = sales_order_id