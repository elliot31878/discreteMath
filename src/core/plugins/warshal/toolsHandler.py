
from .interfaces.observer import Observer

import itertools


class ToolHandler(Observer):

    def __init__(self):
        super(ToolHandler, self)

    @property
    def class_name(self):
        return 'w'

    def execute_app(self, message):
        arrays: list = message["arrays"]
        return self.warShall(arrays)

    def warShall(self, matrix: list):
        assert (len(row) == len(matrix) for row in matrix)
        n = len(matrix)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])
        return matrix
