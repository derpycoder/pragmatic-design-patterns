from .ifactory import IFactory
from autos.dodge_srt import DodgeSRT


class DodgeFactory(IFactory):
    def create_auto(self):
        self.dodge_srt = DodgeSRT('Dodge SRT')

        return self.dodge_srt
