from abc import abstractmethod, ABC

class Observer(ABC):

    @abstractmethod
    def execute_app(self, message:dict):
        pass
    @abstractmethod
    def class_name(self):
        pass