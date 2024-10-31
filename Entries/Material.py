from Entries.Bases.MaterialBase import MaterialBase


class Material(MaterialBase):
    def __init__(self, id: int, ext_id: int, name: str, min_stock: int, stock: int) -> None:
        super().__init__(id, ext_id, name, min_stock, stock)