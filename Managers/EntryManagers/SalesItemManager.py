from Entries.SalesItem import SalesItem
from Utils.Singleton import Singleton


class SalesItemManager(metaclass=Singleton):
    def __init__(self, sales_items: list[SalesItem|object]):
        self.sales_items = sales_items