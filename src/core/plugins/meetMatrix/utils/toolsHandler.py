
class ToolHandler:
    def __init__(self, arrays: list):
        super(ToolHandler,self)
        self.arrays: list = arrays

    def execute_app(self):
        print("execute cartesian relations")
        return self.meet(self.arrays[0], self.arrays[1])

    def meet(self, matrixA: list ,matrixB: list):
        matrixR: list = matrixA
        n = len(matrixA)
        for i in range(n):
            for j in range(n):
                matrixR[i][j] = matrixA[i][j] and matrixB[i][j]
        return matrixR
