from Entries.Bases.ShelfBase import ShelfBase


class Shelf(ShelfBase):
    def __init__(self, id: int) -> None:
        super().__init__(id)