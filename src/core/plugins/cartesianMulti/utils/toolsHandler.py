import itertools


class ToolHandler:
    def __init__(self, arrays:list):
        super(ToolHandler,self)
        self.arrays:list = arrays
        self.__array = []

    def execute_app(self):
        print("execute cartesian multiplication")

        for element in itertools.product(*self.arrays):
            self.__array.append(element)
        return self.__array
