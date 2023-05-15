
class ToolHandler:
    def __init__(self, arrays: list):
        super(ToolHandler,self)
        self.arrays: list = arrays

    def execute_app(self):
        print("execute cartesian relations")
        return self.join(self.arrays[0], self.arrays[1])

    def join(self, matrixA: list ,matrixB: list):
        matrixR: list = matrixA
        n = len(matrixA)
        for i in range(n):
            for j in range(n):
                matrixR[i][j] = matrixA[i][j] or matrixB[i][j]
        return matrixR
