class Matrix:
    def __init__(self, rows, cols, matrix):
        self.rows = rows
        self.cols = cols
        self.matrix = matrix

    def multiply(self):
        b = [[0] * self.rows for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.rows):
                for k in range(self.cols):
                    b[i][j] += (self.matrix[i][k] * self.matrix[j][k])
        return Matrix(self.rows, self.rows, b)

    def __str__(self):
        return "\n".join(" ".join(map(str, i)) for i in self.matrix)


for T in range(int(input())):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    print (Matrix(n, m, a).multiply())
