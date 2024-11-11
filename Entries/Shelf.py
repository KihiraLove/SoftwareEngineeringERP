from Entries.Bases.ShelfBase import ShelfBase


class Shelf(ShelfBase):
    # Don't forget to document this
    def __init__(self, id: int) -> None:
        super().__init__(id)