from Entries.User import User
from Utils.Singleton import Singleton


class UserManager(metaclass=Singleton):
    def __init__(self, users: list[User|object]):
        self.users = users