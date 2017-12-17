from .ifactory import IFactory
from autos.tesla import Tesla


class TeslaFactory(IFactory):
    def create_auto(self):
        self.tesla = Tesla('Tesla Model S')

        return self.tesla
