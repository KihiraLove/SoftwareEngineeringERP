from typing import Self
from Entries.User import User
from Utils.Singleton import Singleton


class UserManager(metaclass=Singleton):
    """
    Singleton class that holds data for all Users
    """
    def __init__(self, data: list[User|object]=None):
        """
        Constructor for UserManager, to access existing singleton, create this without parameters
        :param data: None
        """
        self.data = data
        return

    @classmethod
    def create(cls, data: list[User|object]) -> Self:
        """
        Constructor for UserManager, do not use this to access existing singleton, use __init__ method instead
        :param data: list of User objects
        :return: returns created singleton instance for UserManager
        """
        return cls(data)