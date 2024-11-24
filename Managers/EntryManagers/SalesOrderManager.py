from Entries.SalesOrder import SalesOrder
from Utils.Singleton import Singleton


class SalesOrderManager(metaclass=Singleton):
    def __init__(self, sales_orders: list[SalesOrder|object]):
        self.sales_orders = sales_orders