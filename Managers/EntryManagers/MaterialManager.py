from Entries.Material import Material
from Utils.Singleton import Singleton


class MaterialManager(metaclass=Singleton):
    def __init__(self, materials: list[Material|object]):
        self.materials = materials