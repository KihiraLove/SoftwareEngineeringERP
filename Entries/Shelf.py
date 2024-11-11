from Entries.Bases.ShelfBase import ShelfBase


class Shelf(ShelfBase):
    # Don't forget to document this
    def __init__(self, id: int, location: str) -> None:
        super().__init__(id, location)
        return

    def get_id(self) -> int:
        return self.id

    def get_location(self) -> str:
        return self.location