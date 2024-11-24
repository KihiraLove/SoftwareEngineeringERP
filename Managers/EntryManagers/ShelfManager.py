from Entries.Shelf import Shelf
from Utils.Singleton import Singleton


class ShelfManager(metaclass=Singleton):
    def __init__(self, shelves: list[Shelf|object]):
        self.shelves = shelves