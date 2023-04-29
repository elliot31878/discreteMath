import numpy as np

class ToolHandler:
    def __init__(self, arrays: list):
        super(ToolHandler,self)
        self.arrays: list = arrays
        self.result = []

    def execute_app(self):
        print("execute cartesian logical matrix multiplication")
        return self.multiplication_matrix(0, 1, len(self.arrays))


    def multiplication_matrix(self, first_index:int , last_index:int, main_size: int):

        _main_size = main_size
        if _main_size <= 0:
            return self.result

        if first_index != -1:
            first_array = np.array(self.arrays[first_index], dtype=bool)
            second_array = np.array(self.arrays[last_index], dtype=bool)
            self.result = np.dot(first_array,second_array)
        else:
            first_array = np.array( self.result, dtype=bool)
            second_array = np.array(self.arrays[last_index], dtype=bool)
            self.result = np.dot(first_array, second_array)

        if _main_size == 2:
            return self.result
        else:
            _main_size -= 2
            _first_index = first_index + 1
            _last_index = last_index + 1
            if _last_index == len(self.arrays)-1:
                return self.multiplication_matrix(-1,_last_index,_main_size)
            else:
                return self.multiplication_matrix(_first_index, _last_index, _main_size)
