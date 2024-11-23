from enum import Enum

class UserType(Enum):
    """
    Enum for user types
    """
    MANAGER = 1
    SALES_PERSON = 2
    WAREHOUSE_MANAGER = 3
    WAREHOUSE_WORKER = 4

    def __str__(self):
        return self.name


def parse_user_type(user_string: str) -> UserType:
    if user_string == 'MANAGER':
        return UserType.MANAGER
    elif user_string == 'SALES_PERSON':
        return UserType.SALES_PERSON
    elif user_string == 'WAREHOUSE_MANAGER':
        return UserType.WAREHOUSE_MANAGER
    elif user_string == 'WAREHOUSE_WORKER':
        return UserType.WAREHOUSE_WORKER
    raise ValueError('Invalid user type')