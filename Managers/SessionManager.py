from typing import Self
from Entries.User import User
from Managers.EntryManagers.UserManager import UserManager
from Utils.Singleton import Singleton


class SessionManager(metaclass=Singleton):
    def __init__(self, user: User=None):
        self.user = user
        return

    @classmethod
    def login(cls) -> Self:
        while True:
            try:
                email = input("Enter email:")
                user = UserManager().search(email=email)
                password = input("Enter password:")
                if user.check_password(password):
                    return SessionManager(user)
            except ValueError as e:
                print(e)

    def logout(self) -> None:
        self.user = None
        return