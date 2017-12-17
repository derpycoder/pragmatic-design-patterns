from .ifactory import IFactory
from autos.null_car import NullCar


class NullFactory(IFactory):
    def create_auto(self):
        self.null_car = NullCar('')

        return self.null_car
