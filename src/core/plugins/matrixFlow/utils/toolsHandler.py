
class ToolHandler:
    def __init__(self, arrays: list):
        super(ToolHandler,self)
        self.arrays: list = arrays

    def execute_app(self):
        print("execute matrix flow")
        collection: str = input("Enter your collection like 1_2-3_4 ... : ")
        _arrays = collection.split('-')
        matrix = []
        for i in range(0,len(self.arrays)):
            matrix.append([])
            for j in range(0,len(self.arrays)):
                matrix[i].append(0)
        for element in _arrays:
            _elements = element.split("_")
            first_element = int(_elements[0])
            second_element = int(_elements[1])
            if(first_element in self.arrays and second_element in self.arrays):
                matrix[first_element, second_element]=1

        return matrix
