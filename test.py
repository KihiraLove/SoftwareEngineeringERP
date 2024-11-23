from datetime import datetime

from Entries.User import User
from Enums.UserType import UserType
from Utils import Config

date = datetime.now().strftime(Config.TIME_FORMAT)
time_str = "2024-11-23 14:56:01"
date2 = datetime.strptime(time_str, Config.TIME_FORMAT)
print(date)
print(date2)

user_type = UserType.MANAGER
print(user_type)

from Entries.BusinessPartner import BusinessPartner
from Managers.FileManager import serialize, clean_up_json_to_string_list, deserialize

bp = BusinessPartner(0, "co", "adr", None)
bp2 = BusinessPartner(1, "co2", "adr2", None)
bpl = [bp, bp2]
jsons = serialize(bpl)
print(jsons)

user1 = User(0, "Nikola Tesla", "nikola.tesla@electricity.rs", "1234iloveelectrons", UserType.MANAGER)
user_string = user1.__repr__()
print(user_string)
user_string = clean_up_json_to_string_list(user_string)
s = True
print(s)


bp_string = bp.__repr__()
bp_string_list = clean_up_json_to_string_list(bp_string)
bp_rebuilt = BusinessPartner.from_string(bp_string_list)
print(bp)
print(bp_rebuilt)

obj = deserialize(bp_string, BusinessPartner)[0]
print(type(obj))