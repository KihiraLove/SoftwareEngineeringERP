from Managers.FileManager import write_to_file
from Utils.Types import TYPES

for name in TYPES.keys():
    if name == "BusinessPartner":
        continue
    file_path = "./Managers/EntryManagers/" + TYPES[name].manager_type + ".py"
    content = f"""from typing import Self
from Entries.{name} import {name}
from Utils.Singleton import Singleton


class {name}Manager(metaclass=Singleton):
    \"\"\"
    Singleton class that holds data for all {name}s
    \"\"\"
    def __init__(self, data: list[{name}|object]=None):
        \"\"\"
        Constructor for {name}Manager, to access existing singleton, create this without parameters
        :param data: None
        \"\"\"
        self.data = data
        return

    @classmethod
    def create(cls, data: list[{name}|object]) -> Self:
        \"\"\"
        Constructor for {name}Manager, do not use this to access existing singleton, use __init__ method instead
        :param data: list of {name} objects
        :return: returns created singleton instance for {name}Manager
        \"\"\"
        return cls(data)"""

    write_to_file(file_path, content)