from Entries.Bases.LabelBase import LabelBase


class Label(LabelBase):
    # Don't forget to document this
    def __init__(self, id: int, sales_order_id: int) -> None:
        super().__init__(id)
        self.sales_order_id = sales_order_id
        return

    def get_id(self) -> int:
        return self.id

    def get_sales_order_id(self) -> int:
        return self.sales_order_id