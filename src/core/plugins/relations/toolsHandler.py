
from .interfaces.observer import Observer

import itertools


class ToolHandler(Observer):

    def __init__(self):
        super(ToolHandler, self)

    @property
    def class_name(self):
        return '->'

    def execute_app(self, message):
        arrays: list = message["arrays"]
        return self.relations_between_two_array(arrays[0], arrays[1])

    def relations_between_two_array(self, arrayFirst: list, arraySecond: list) -> list:
        size_first: int = len(arrayFirst)-1
        size_second: int = len(arraySecond)-1
        max_size: int = size_first
        if max_size < size_second:
            max_size = size_second
        first_index: int = 0
        second_index: int = 0
        result_array: list = []
        for i in range(0, max_size+1):
            if size_first < first_index:
                first_index = 0
            if size_second < second_index:
                second_index = 0
            result_array.append((arrayFirst[first_index], arraySecond[second_index]))
            first_index += 1
            second_index += 1
        return result_array
