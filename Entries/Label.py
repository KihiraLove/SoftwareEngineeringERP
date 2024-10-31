from Entries.Bases.LabelBase import LabelBase


class Label(LabelBase):
    def __init__(self, id: int, sales_order_id: int) -> None:
        super().__init__(id)
        self.sales_order_id = sales_order_id