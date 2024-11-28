from PySimpleGUI import Window

from Utils.Singleton import Singleton
import PySimpleGUI as sg


class UIManager(metaclass=Singleton):
    def __init__(self):
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