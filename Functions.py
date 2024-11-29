from Managers.EntryManagers.LabelManager import LabelManager
from Managers.EntryManagers.MaterialManager import MaterialManager
from Managers.EntryManagers.SalesItemManager import SalesItemManager
from Managers.EntryManagers.SalesOrderManager import SalesOrderManager
from Managers.EntryManagers.WarehouseTaskManager import WarehouseTaskManager


def make_sales_order():
    MaterialManager.create_material()
    SalesItemManager.create_sales_item()
    SalesOrderManager.create_sales_order()
    LabelManager.create_label()
    WarehouseTaskManager.create_warehouse_task()