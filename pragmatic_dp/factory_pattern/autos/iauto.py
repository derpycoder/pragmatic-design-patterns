from abc import ABCMeta, abstractmethod

class IAuto(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
