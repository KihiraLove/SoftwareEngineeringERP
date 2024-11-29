from enum import Enum


class StatusKey(Enum):
    """
    Enum for UI window statuses
    """
    EXIT = 1
    EMAIL_CORRECT = 2
    INCORRECT = 3
    CORRECT = 4
    LOGOUT = 5
    SALES_ORDER = 6