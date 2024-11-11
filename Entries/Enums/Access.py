from dataclasses import dataclass
from enum import Enum

class Access(Enum):
    CREATE_BUSINESS_PARTNER = 1
    CREATE_MATERIAL = 2
    CREATE_USER = 3
    CREATE_SALES_ORDER = 4
    CREATE_STORAGE_BIN = 5
    RECEIVE_GOODS = 6
    WAREHOUSE_TASK = 7

@dataclass
class AccessList:
    def __init__(self):
        self.manager_access: set[Access] = {
                                            Access.CREATE_BUSINESS_PARTNER,
                                            Access.CREATE_MATERIAL,
                                            Access.CREATE_USER,
                                            Access.CREATE_SALES_ORDER,
                                            Access.CREATE_STORAGE_BIN,
                                            Access.RECEIVE_GOODS}

        self.sales_person_access: set[Access] = {
                                            Access.CREATE_BUSINESS_PARTNER,
                                            Access.CREATE_SALES_ORDER}

        self.warehouse_manager_access: set[Access] = {
                                            Access.CREATE_STORAGE_BIN,
                                            Access.RECEIVE_GOODS,
                                            Access.WAREHOUSE_TASK}

        self.warehouse_worker_access: set[Access] = {
                                            Access.WAREHOUSE_TASK}