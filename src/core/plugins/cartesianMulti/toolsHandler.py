
from .interfaces.observer import Observer

import itertools


class ToolHandler(Observer):

    def __init__(self):
        super(ToolHandler, self)

    @property
    def class_name(self):
        return '@'

    def execute_app(self, message):
        arrays:list = message["arrays"]
        __array = []
        for element in itertools.product(*arrays):
            __array.append(element)
        return __array
