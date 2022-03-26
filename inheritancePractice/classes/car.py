from abc import ABC
from src.classes.land import Land


class Car(Land, ABC):
    def __init__(self, name: str, price: int, has_motor: bool, use_gas: bool):
        super().__init__(name, price, has_motor)
        self.use_gas = use_gas

    def display_data(self):
        print(self.name + " - " + str(self.price) + " - " + str(self.has_motor) + " - " + str(self.use_gas))
        