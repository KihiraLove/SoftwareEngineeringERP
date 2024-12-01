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
            if not self.session_manager.logged_in():
                status = self.login_flow()
            else:
                status = self.main_flow()
            if status == StatusKey.EXIT:
                self.ui_manager.close_window()
                break
        return

    def login_flow(self) -> StatusKey:
        """
        UI flow to log in user
        :return: StatusKey whether the log in was successful or the user closed the window
        """
        self.ui_manager.create_login_window()
        while True:
            event, values = self.ui_manager.read_window()
            if event in (sg.WINDOW_CLOSED, "Cancel"):
                return StatusKey.EXIT
            if event == "Login":
                #status = self.session_manager.login(email=values["-email-"], password=values["-password-"])
                # added for quick login
                status = self.session_manager.login("admin", "1234")
                if status == StatusKey.CORRECT:
                    return StatusKey.CORRECT
                elif status == StatusKey.EMAIL_CORRECT:
                    self.ui_manager.show_message("Error", "Invalid password.")
                else:
                    self.ui_manager.show_message("Error", "Invalid email.")

    def main_flow(self) -> StatusKey:
        status = StatusKey.MAIN
        while True:
            self.ui_manager.update_window(status)
            event, values = self.ui_manager.read_window()

            if event in (sg.WINDOW_CLOSED, "-EXIT-"):
                return StatusKey.EXIT
            elif event == "-LOGOUT-":
                self.session_manager.logout()
                return StatusKey.LOGOUT
            elif event == "-SALES-":
                status = StatusKey.SALES_ORDER
            elif event == "-MAIN-":
                status = StatusKey.MAIN
            elif event == "-ADD_ITEM-":
                status = StatusKey.ADD_ROW
            elif event == "SUBMIT_SALES_ORDER":
                status = StatusKey.MAIN