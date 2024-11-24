from Entries.Label import Label
from Utils.Singleton import Singleton


class LabelManager(metaclass=Singleton):
    def __init__(self, labels: list[Label|object]):
        self.labels = labels