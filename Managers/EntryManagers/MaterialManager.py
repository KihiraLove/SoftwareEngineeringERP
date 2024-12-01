from Entries.Material import Material
from Utils.Singleton import Singleton


class MaterialManager(metaclass=Singleton):
    """
    Singleton class that holds data for all Materials
    """
    def __init__(self, data: list[Material|object]=None):
        """
        Constructor for MaterialManager, to access existing singleton, create this without parameters
        :param data: None
        """
        self.data = data
        return

    def create_material(self):
        return

    def names_and_ids(self) -> list[str]:
        names_ids = []
        for material in self.data:
            names_ids.append(f"{material.name} ({material.id})")
        return names_ids

def create(data: list[Material|object]) -> MaterialManager:
    """
    Constructor for MaterialManager, do not use this to access existing singleton, use __init__ method instead
    :param data: list of Material objects
    :return: returns created singleton instance for MaterialManager
    """
    return MaterialManager(data)