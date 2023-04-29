
from interfaces.subjects import Subjects
from interfaces.observer import Observer

from typing import Set


class ConcentrateHandlers(Subjects):
    _observers:Set = set()

    def __init__(self):
        pass

    def notification(self, message:dict,to:str):
        for item in self._observers:
            if item.class_name == to:
                return item.execute_app(message)

    def inject(self, observer:Observer):
        for item in self._observers:
            if item == observer:
                return
        self._observers.add(observer)

    def dispose(self,observer:Observer):
        pass
