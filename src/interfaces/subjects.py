from abc import abstractmethod,ABC

from .observer import Observer


class Subjects(ABC):
    @abstractmethod
    def notification(self,message:dict,to:str):
        pass

    @abstractmethod
    def inject(self,observer:Observer):
        pass

    @abstractmethod
    def dispose(self, observer:Observer):
        pass
