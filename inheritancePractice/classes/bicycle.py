from abc import ABC
from src.classes.land import Land


class Bicycle(Land, ABC):
    def __init__(self, name: str, price: int, has_motor: bool, exercise_bike: bool):
        super().__init__(name, price, has_motor)
        self.exercise_bike = exercise_bike

    def display_data(self):
        print(self.name + " - " + str(self.price) + " - " + str(self.has_motor) + " - " + str(self.exercise_bike))
