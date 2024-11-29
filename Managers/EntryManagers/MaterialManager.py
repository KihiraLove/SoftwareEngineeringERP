from typing import Self
from Entries.Material import Material
from Utils.Singleton import Singleton


class MaterialManager(metaclass=Singleton):
    """
    Singleton class that holds data for all Materials
    """
    def __init__(self, data: list[Material|object]=None):
        """
        Constructor for MaterialManager, to access existing singleton, create this without parameters
        :param data: None
        """
        self.data = data
        return

    @classmethod
    def create(cls, data: list[Material|object]) -> Self:
        """
        Constructor for MaterialManager, do not use this to access existing singleton, use __init__ method instead
        :param data: list of Material objects
        :return: returns created singleton instance for MaterialManager
        """
        return cls(data)

    def create_material(self):
        return