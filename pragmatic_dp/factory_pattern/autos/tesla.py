from .iauto import IAuto


class Tesla(IAuto):
    def __init__(self, car_name):
        self._carname = car_name

    def start(self):
        print(f"{self._carname} barely makes any noise.")

    def stop(self):
        print(f"{self._carname} stops within moments")
