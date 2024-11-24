from typing import Self
from Entries.SalesPerson import SalesPerson
from Utils.Singleton import Singleton


class SalesPersonManager(metaclass=Singleton):
    """
    Singleton class that holds data for all SalesPersons
    """
    def __init__(self, data: list[SalesPerson|object]=None):
        """
        Constructor for SalesPersonManager, to access existing singleton, create this without parameters
        :param data: None
        """
        self.data = data
        return

    @classmethod
    def create(cls, data: list[SalesPerson|object]) -> Self:
        """
        Constructor for SalesPersonManager, do not use this to access existing singleton, use __init__ method instead
        :param data: list of SalesPerson objects
        :return: returns created singleton instance for SalesPersonManager
        """
        return cls(data)