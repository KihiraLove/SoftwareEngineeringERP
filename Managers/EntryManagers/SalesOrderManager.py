from typing import Self
from Entries.SalesOrder import SalesOrder
from Utils.Singleton import Singleton


class SalesOrderManager(metaclass=Singleton):
    """
    Singleton class that holds data for all SalesOrders
    """
    def __init__(self, data: list[SalesOrder|object]=None):
        """
        Constructor for SalesOrderManager, to access existing singleton, create this without parameters
        :param data: None
        """
        self.data = data
        return

    @classmethod
    def create(cls, data: list[SalesOrder|object]) -> Self:
        """
        Constructor for SalesOrderManager, do not use this to access existing singleton, use __init__ method instead
        :param data: list of SalesOrder objects
        :return: returns created singleton instance for SalesOrderManager
        """
        return cls(data)