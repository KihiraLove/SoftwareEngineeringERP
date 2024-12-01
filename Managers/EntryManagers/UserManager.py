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

    def search(self, email: str=None, id: int=None ) -> User:
        """
        Search for User by email or id
        :param email: query option
        :param id: query option
        :return: found user by email or id
        """
        if email is None and id is None:
            raise ValueError("Either email or id must be provided")
        elif email is not None:
            for user in self.data:
                if user.email == email:
                    return user
            raise ValueError(f"User {email} not found")
        elif id is not None:
            for user in self.data:
                if user.id == id:
                    return user
            raise ValueError(f"User id {id} not found")


def create(data: list[User|object]) -> UserManager:
    """
    Constructor for UserManager, do not use this to access existing singleton, use __init__ method instead
    :param data: list of User objects
    :return: returns created singleton instance for UserManager
    """
    return UserManager(data)