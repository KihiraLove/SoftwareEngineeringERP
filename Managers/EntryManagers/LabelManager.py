from typing import Self
from Entries.Label import Label
from Utils.Singleton import Singleton


class LabelManager(metaclass=Singleton):
    """
    Singleton class that holds data for all Labels
    """
    def __init__(self, data: list[Label|object]=None):
        """
        Constructor for LabelManager, to access existing singleton, create this without parameters
        :param data: None
        """
        self.data = data
        return

    @classmethod
    def create(cls, data: list[Label|object]) -> Self:
        """
        Constructor for LabelManager, do not use this to access existing singleton, use __init__ method instead
        :param data: list of Label objects
        :return: returns created singleton instance for LabelManager
        """
        return cls(data)