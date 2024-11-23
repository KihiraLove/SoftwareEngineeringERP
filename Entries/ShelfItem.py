from Entries.Bases.ShelfItemBase import ShelfItemBase


class ShelfItem(ShelfItemBase):
    def __init__(self, id: int, amount: int, shelf_id: int, material_id: int) -> None:
        super().__init__(id, amount)
        self.shelf_id = shelf_id
        self.material_id = material_id
        return

    def __repr__(self):
        return (f"{{"
                f"\"id\": \"{self.id}\","
                f"\"amount\": \"{self.amount}\","
                f"\"shelf_id\": \"{self.shelf_id}\","
                f"\"material_id\": \"{self.material_id}\""
                f"}}")

    def get_id(self) -> int:
        return self.id

    def get_amount(self) -> int:
        return self.amount

    def get_shelf_id(self) -> int:
        return self.shelf_id

    def get_material_id(self) -> int:
        return self.material_id


def from_string(string_array: list[str]) -> ShelfItem:
    id = int(string_array[0])
    amount = int(string_array[1])
    shelf_id = int(string_array[2]) if string_array[2] != "None" else None
    material_id = int(string_array[3]) if string_array[3] != "None" else None
    return ShelfItem(id, amount, shelf_id, material_id)