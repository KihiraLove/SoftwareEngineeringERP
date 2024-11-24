from Entries.ShelfItem import ShelfItem
from Utils.Singleton import Singleton


class ShelfItemManager(metaclass=Singleton):
    def __init__(self, shelf_items: list[ShelfItem|object]):
        self.shelf_items = shelf_items