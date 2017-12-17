from inspect import getmembers, isclass, isabstract
import autos


class AutoFactory():
    autos = {}

    def __init__(self):
        self.load_autos()

    def load_autos(self):
        classes = getmembers(autos, lambda m: isclass(m) and not isabstract(m))

        for name, _type in classes:
            if isclass(_type) and issubclass(_type, autos.IAuto):
                self.autos.update([[name, _type]])

    def create_instance(self, car_name):
        if car_name in self.autos:
            return self.autos[car_name](car_name)
        else:
            return autos.NullCar(car_name)
