from enum import Enum

class UserType(Enum):
    """
    Enum for user types
    """
    MANAGER = 1
    SALES_PERSON = 2
    WAREHOUSE_MANAGER = 3
    WAREHOUSE_WORKER = 4