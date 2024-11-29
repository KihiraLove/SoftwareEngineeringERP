from PySimpleGUI import Window
from Enums.AccessType import AccessType
from Managers.AccessList import AccessList
from Managers.SessionManager import SessionManager
from Utils.Singleton import Singleton
import PySimpleGUI as sg


class UIManager(metaclass=Singleton):
    def __init__(self):
        self.window = None
        return

    @staticmethod
    def create_login_window() -> Window:
        """
        Creates UI for logging in using PySimpleGUI
        :return: created window
        """
        layout = [
            [sg.Text("Email:", size=(10, 1)), sg.Input(key="-email-", size=(25, 1))],
            [sg.Text("Password:", size=(10, 1)), sg.Input(key="-password-", password_char="*", size=(25, 1))],
            [sg.Button("Login", bind_return_key=True), sg.Button("Cancel")]
        ]

        # Create the window
        window = sg.Window("Login", layout, finalize=True)

        return window

    @staticmethod
    def create_main_window() -> Window:
        session_manager = SessionManager()
        access_list = AccessList()
        logged_in_users_type = session_manager.current_users_type()
        layout = []
        if access_list.has_access(logged_in_users_type, AccessType.CREATE_SALES_ORDER):
            layout.append([sg.Button("Sales Orders", size=(15, 2), key="-SALES-", pad=(20, 20))])
        layout.append([
            [sg.Push(),
             sg.Button("Logout", size=(10, 1), key="-LOGOUT-", pad=(5, 20)),
             sg.Button("Exit", size=(10, 1), key="-EXIT-", pad=(20, 20))]
        ])

        # Create the window
        window = sg.Window(
            "Main Window",
            layout,
            size=(1000, 700),
            element_justification="left",  # Left-align elements by default
            margins=(0, 0),  # Remove internal PySimpleGUI margins (handled in padding)
            finalize=True
        )

        return window
