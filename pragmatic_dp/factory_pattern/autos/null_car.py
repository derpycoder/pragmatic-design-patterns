from .iauto import IAuto


class NullCar(IAuto):
    def __init__(self, car_name):
        self._carname = car_name

    def start(self):
        print(f'Unknown Vehichle {self._carname}')

    def stop(self):
        print(f'Vehicle Stopped')
