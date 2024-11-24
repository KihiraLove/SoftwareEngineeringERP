from Entries.WarehouseTask import WarehouseTask
from Utils.Singleton import Singleton


class WarehouseTaskManager(metaclass=Singleton):
    def __init__(self, data: list[WarehouseTask|object]=None):
        self.data = data