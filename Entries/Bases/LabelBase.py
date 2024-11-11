from dataclasses import dataclass


@dataclass
class LabelBase:
    def __init__(self, id: int) -> None:
        self.id = id
        return