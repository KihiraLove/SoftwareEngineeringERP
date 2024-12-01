from Managers.DataManager import DataManager
from Managers.FlowManager import FlowManager
from Managers.SessionManager import SessionManager
from Managers.UIManager import UIManager
from Utils.GenerateData import generate_data_if_not_exist

# This isn't part of the software, it generates JSON files with dummy data to be used
generate_data_if_not_exist()


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