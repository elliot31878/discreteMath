
class ToolHandler:
    def __init__(self, arrays: list):
        super(ToolHandler,self)
        self.arrays: list = arrays

    def execute_app(self):
        print("execute cartesian relations")
        return self.warShall(self.arrays)

    def warShall(self, matrix: list):
        assert (len(row) == len(matrix) for row in matrix)
        n = len(matrix)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])
        return matrix
