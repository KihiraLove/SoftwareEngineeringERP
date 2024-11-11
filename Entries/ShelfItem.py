from Entries.Bases.ShelfItemBase import ShelfItemBase


class ShelfItem(ShelfItemBase):
    def __init__(self, id: int, amount: int, shelf_id: int, material_id: int) -> None:
        super().__init__(id, amount)
        self.shelf_id = shelf_id
        self.material_id = material_id
        return

    def get_id(self) -> int:
        return self.id

    def get_amount(self) -> int:
        return self.amount

    def get_shelf_id(self) -> int:
        return self.shelf_id

    def get_material_id(self) -> int:
        return self.material_id