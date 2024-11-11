from Entries.Bases.ShelfItemBase import ShelfItemBase


class ShelfItem(ShelfItemBase):
    def __init__(self, id: int, amount: int, shelf_id: int, material_id: int) -> None:
        super().__init__(id, amount)
        self.shelf_id = shelf_id
        self.material_id = material_id