from Entries.SalesPerson import SalesPerson
from Utils.Singleton import Singleton


class SalesPersonManager(metaclass=Singleton):
    def __init__(self, sales_persons: list[SalesPerson|object]):
        self.sales_persons = sales_persons