from Enums.AccessType import AccessType
from Enums.StatusKey import StatusKey
from Managers.AccessList import AccessList
from Managers.EntryManagers.BusinessPartnerManager import BusinessPartnerManager
from Managers.EntryManagers.SalesOrderManager import SalesOrderManager
from Managers.SessionManager import SessionManager
from Utils.Singleton import Singleton
import PySimpleGUI as sg


class UIManager(metaclass=Singleton):
    def __init__(self):
        self.window = None
        self.dynamic_row_count = 1
        return

    def close_window(self) -> None:
        """
        Closes the UI window
        :return: None
        """
        self.window.close()

    def read_window(self) -> tuple:
        """
        Read actions and inputs from UI window
        :return: events and values
        """
        return self.window.read()

    @staticmethod
    def show_message(title: str, message: str) -> None:
        """
        Shows a message as new popup window
        :param title: title of popup window
        :param message: message to show
        :return: None
        """
        sg.popup(message, title=title)

    def create_login_window(self) -> None:
        """
        Creates UI for logging in using PySimpleGUI
        :return: created window
        """
        if self.window is not None:
            self.window.close()

        layout = [
            [sg.Text("Email:", size=(10, 1)), sg.Input(key="-email-", size=(25, 1))],
            [sg.Text("Password:", size=(10, 1)), sg.Input(key="-password-", password_char="*", size=(25, 1))],
            [sg.Button("Login", bind_return_key=True), sg.Button("Cancel")]
        ]

        self.window = sg.Window("Login", layout, finalize=True)

    def update_window(self, status: StatusKey|None):
        if status is StatusKey.ADD_ROW:
            new_row = [
                sg.Combo(["Item 1", "Item 2", "Item 3"], size=(20, 1), key=f"-ITEM-{self.dynamic_row_count}-"),
                sg.Input(size=(20, 1), key=f"-MATERIAL-{self.dynamic_row_count}-")
            ]
            self.window.extend_layout(self.window["-DYNAMIC_ROWS-"], [new_row])
            self.dynamic_row_count += 1
            return
        self.close_window()
        layout = []
        if status is None:
            return
        if status is StatusKey.MAIN:
            layout = self._create_main_layout()
        if status is StatusKey.SALES_ORDER:
            layout = self._create_sales_order_layout()

        self.window = sg.Window(
            "Main Window",
            layout,
            size=(800, 600),
            element_justification="left",
            margins=(0, 0),
            finalize=True
        )
        return

    @staticmethod
    def _create_main_layout():
        session_manager = SessionManager()
        access_list = AccessList()
        logged_in_users_type = session_manager.current_users_type()
        layout = []
        if access_list.has_access(logged_in_users_type, AccessType.CREATE_SALES_ORDER):
            layout.append([sg.Button("Sales Orders", size=(20, 2), key="-SALES-", pad=(20, 20))])
        layout.append([
            [sg.VPush()],
            [sg.VPush(),
             sg.Push(),
             sg.Button("Logout", size=(20, 2), key="-LOGOUT-", pad=(20, 20)),
             sg.Button("Exit", size=(20, 2), key="-EXIT-", pad=(20, 20))]
        ])
        return layout

    @staticmethod
    def _create_sales_order_layout():
        """
        Creates a PySimpleGUI layout with the following structure:
        1. Title row.
        2. ID (readonly) and Business Partners dropdown.
        3. Date field.
        4. Dynamic row creation for items (dropdown + input field for material).
        5. Bottom row with Save, Discard, and Exit buttons.
        """
        # Initial dynamic layout (empty at the start)
        so_manager = SalesOrderManager()
        id = len(so_manager.data)
        bp_manager = BusinessPartnerManager()
        business_partners = bp_manager.names()

        dynamic_rows = [[
            sg.Combo(["Item 1", "Item 2", "Item 3"], size=(20, 1), key=f"-ITEM-0-"),
            sg.Input(size=(20, 1), key=f"-MATERIAL-0-")
        ]]

        # Static layout
        layout = [
            [sg.Text("Create Sales Order", font=("Helvetica", 16), justification="center", expand_x=True)],
            [sg.Text("ID:", size=(15, 1)), sg.Input(id, readonly=True, size=(20, 1), key="-ID-")],
            [sg.Text("Business Partners:", size=(15, 1)),
             sg.Combo(business_partners, size=(20, 1), key="-BUSINESS_PARTNER-")],
            [sg.Text("Date:", size=(15, 1)), sg.Input("", size=(20, 1), key="-DATE-"),
             sg.CalendarButton("Select Date", target="-DATE-", format="%Y-%m-%d")],
            [sg.Text("Items:", size=(15, 1))],
            [sg.Column(dynamic_rows, key="-DYNAMIC_ROWS-", vertical_scroll_only=True, size=(500, 200),
                       scrollable=True, expand_x=True)],
            [sg.Button("Add Item", key="-ADD_ITEM-"), sg.Button("Submit"), sg.Button("Cancel")],
            [sg.HorizontalSeparator()],
            [sg.Button("Save", key="-SAVE-", size=(10, 1)), sg.Button("Discard", key="-DISCARD-", size=(10, 1)),
             sg.Button("Exit", key="-EXIT-", size=(10, 1))]
        ]

        return layout


