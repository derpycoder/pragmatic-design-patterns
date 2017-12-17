from .iauto import IAuto


class DodgeSRT(IAuto):
    def __init__(self, car_name):
        self._carname = car_name

    def start(self):
        print(f"{self._carname} Growls")

    def stop(self):
        print(f"{self._carname} Screeches to a stop!")
