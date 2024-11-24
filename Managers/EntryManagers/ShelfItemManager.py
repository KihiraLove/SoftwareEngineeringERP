from typing import Self
from Entries.ShelfItem import ShelfItem
from Utils.Singleton import Singleton


class ShelfItemManager(metaclass=Singleton):
    """
    Singleton class that holds data for all ShelfItems
    """
    def __init__(self, data: list[ShelfItem|object]=None):
        """
        Constructor for ShelfItemManager, to access existing singleton, create this without parameters
        :param data: None
        """
        self.data = data
        return

    @classmethod
    def create(cls, data: list[ShelfItem|object]) -> Self:
        """
        Constructor for ShelfItemManager, do not use this to access existing singleton, use __init__ method instead
        :param data: list of ShelfItem objects
        :return: returns created singleton instance for ShelfItemManager
        """
        return cls(data)