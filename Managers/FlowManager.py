from Enums.StatusKey import StatusKey
from Managers.DataManager import DataManager
from Managers.SessionManager import SessionManager
from Managers.UIManager import UIManager
import PySimpleGUI as sg


class FlowManager:
    def __init__(self, data_manager: DataManager, ui_manager: UIManager, session_manager: SessionManager):
        self.data_manager = data_manager
        self.ui_manager = ui_manager
        self.session_manager = session_manager
        return

    def start_flow(self):
        """
        Enter function into workflow
        :return: None
        """
        while True:
            status = None
            if not self.session_manager.logged_in():
                status = self.login_flow()

            if status == StatusKey.EXIT:
                break
        return

    def login_flow(self) -> StatusKey:
        """
        UI flow to log in user
        :return: StatusKey whether the log in was successful or the user closed the window
        """
        window = self.ui_manager.create_login_window()
        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancel"):
                window.close()
                return StatusKey.EXIT

            if event == "Login":
                status = self.session_manager.login(email=values["email"], password=values["password"])

                if status == StatusKey.CORRECT:
                    window.close()
                    return StatusKey.CORRECT
                elif status == StatusKey.EMAIL_CORRECT:
                    window["-MESSAGE-"].update("Invalid password.")
                else:
                    window["-MESSAGE-"].update("Invalid email.")