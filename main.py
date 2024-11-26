from Managers.DataManager import DataManager
from Managers.SessionManager import SessionManager

# initialize data
data_manager = DataManager()
session_manager = SessionManager()
session_manager.login()



session_manager.logout()
# write data at shutdown
data_manager.write_data()