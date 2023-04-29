
from .interfaces.observer import Observer

import itertools


class ToolHandler(Observer):

    def __init__(self):
        super(ToolHandler, self)

    @property
    def class_name(self):
        return '[]'

    def execute_app(self, message):
        arrays: list = message["arrays"]
        print("execute matrix flow")
        collection: str = input("Enter your collection like 1_2-3_4 ... : ")
        _arrays = collection.split('-')
        matrix = []
        for i in range(0, len(arrays)):
            matrix.append([])
            for j in range(0, len(arrays)):
                matrix[i].append(0)
        for element in _arrays:
            _elements = element.split("_")
            first_element = int(_elements[0])
            second_element = int(_elements[1])
            if(first_element in arrays and second_element in arrays):
                matrix[first_element-1][second_element-1] = 1

        return matrix

