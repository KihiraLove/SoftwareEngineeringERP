from Entries.SalesItem import SalesItem
from Utils.Singleton import Singleton


class SalesItemManager(metaclass=Singleton):
    """
    Singleton class that holds data for all SalesItems
    """
    def __init__(self, data: list[SalesItem|object]=None):
        """
        Constructor for SalesItemManager, to access existing singleton, create this without parameters
        :param data: None
        """
        self.data = data
        return

    def create_sales_item(self, sales_item: SalesItem) -> None:
        return


def create(data: list[SalesItem|object]) -> SalesItemManager:
    """
    Constructor for SalesItemManager, do not use this to access existing singleton, use __init__ method instead
    :param data: list of SalesItem objects
    :return: returns created singleton instance for SalesItemManager
    """
    return SalesItemManager(data)