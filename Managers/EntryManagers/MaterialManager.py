from Entries.Material import Material
from Enums.StatusKey import StatusKey
from Managers.EntryManagers.SalesOrderManager import SalesOrderManager
from Utils.Time import generate_time
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

    def get_by_id(self, id: int) -> Material|None:
        for material in self.data:
            if material.get_id() == id:
                return material
        return None

    def subtract_material(self, id: int, amount: int) -> StatusKey:
        print(id)
        material = self.get_by_id(id)
        print(material)
        new_stock = material.stock - amount
        sales_order_manager = SalesOrderManager()
        status = StatusKey.ORDERED
        if new_stock < material.min_stock:
            required_amount = material.min_stock - new_stock + 100
            sales_order_manager.create_sales_order(generate_time(), "New", True, required_amount)
            status = StatusKey.AUTO_ORDER
        if new_stock < 0:
            status = StatusKey.DELAYED_ORDER

        material.stock = new_stock
        return status

    def names_ids_amounts(self) -> list[str]:
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