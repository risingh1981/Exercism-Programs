class Matrix:
    def __init__(self, matrix_string):
        self.matrix = Matrix.extract(matrix_string)

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        generateCol = []
        for row in self.matrix:
            generateCol.append(row[index - 1])
        return generateCol
    
    @staticmethod
    def extract(matrix_str):
        matrix_arr = matrix_str.split("\n")
        i = 0
        for row in matrix_arr:
            matrix_arr[i] = list(map(int, row.split(" ")))
            i += 1
        return matrix_arr

