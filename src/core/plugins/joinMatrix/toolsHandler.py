
from .interfaces.observer import Observer

import itertools


class ToolHandler(Observer):

    def __init__(self):
        super(ToolHandler, self)

    @property
    def class_name(self):
        return 'v'

    def execute_app(self, message):
        arrays: list = message["arrays"]
        return self.join(arrays[0], arrays[1])

    def join(self, matrixA: list ,matrixB: list):
        matrixR: list = matrixA
        n = len(matrixA)
        for i in range(n):
            for j in range(n):
                matrixR[i][j] = matrixA[i][j] or matrixB[i][j]
        return matrixR
