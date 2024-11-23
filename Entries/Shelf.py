from Entries.Bases.ShelfBase import ShelfBase


class Shelf(ShelfBase):
    # Don't forget to document this
    def __init__(self, id: int, location: str) -> None:
        super().__init__(id, location)
        return

    def __repr__(self):
        return (f"{{"
                f"\"id\": \"{self.id}\","
                f"\"location\": \"{self.location}\""
                f"}}")

    def get_id(self) -> int:
        return self.id

    def get_location(self) -> str:
        return self.location


def from_string(string_array: list[str]) -> Shelf:
    id = int(string_array[0])
    location = string_array[1]
    return Shelf(id, location)