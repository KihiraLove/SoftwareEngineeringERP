from Entries.Bases.MaterialBase import MaterialBase


class Material(MaterialBase):
    # Don't forget to document this
    def __init__(self, id: int, ext_id: int, name: str, min_stock: int, stock: int) -> None:
        super().__init__(id, ext_id, name, min_stock, stock)
        return

    def get_id(self) -> int:
        return self.id

    def get_ext_id(self) -> int:
        return self.ext_id

    def get_name(self) -> str:
        return self.name

    def get_min_stock(self) -> int:
        return self.min_stock

    def get_stock(self) -> int:
        return self.stock