from abc import abstractmethod, ABC


class Observer(ABC):

    @abstractmethod
    def notify(self, message:dict):
        pass

    @abstractmethod
    def class_name(self):
        pass
