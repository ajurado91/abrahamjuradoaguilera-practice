import abc


class Transport:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    @abc.abstractmethod
    def get_name(self):
        return self.name

    @abc.abstractmethod
    def get_price(self):
        return self.price
