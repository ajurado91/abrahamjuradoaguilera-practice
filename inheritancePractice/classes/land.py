import abc
from abc import ABC
from src.classes.transport import Transport


class Land (Transport, ABC):
    def __init__(self, name: str, price: int, has_motor: bool):
        super().__init__(name, price)
        self.has_motor = has_motor

    def display_data(self):
        print(self.name + " - " + str(self.price) + " - " + str(self.has_motor))
