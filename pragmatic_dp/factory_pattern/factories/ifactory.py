from abc import ABCMeta, abstractmethod


class IFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_auto(self):
        pass
