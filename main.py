from Managers.DataManager import DataManager
from Managers.FlowManager import FlowManager
from Managers.SessionManager import SessionManager
from Managers.UIManager import UIManager


# initialize data
data_manager = DataManager()

# start managers
session_manager = SessionManager()
ui_manager = UIManager()
flow_manager = FlowManager(data_manager, ui_manager, session_manager)

# start workflow
flow_manager.start_flow()

# write data at shutdown
data_manager.write_data()