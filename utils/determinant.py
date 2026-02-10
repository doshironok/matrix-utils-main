def determinant(matrix):
    from copy import deepcopy
    n = len(matrix)
    if not all(len(row) == n for row in matrix):
        raise ValueError("Матрица должна быть квадратной")
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    det = 0
    for c in range(n):
        minor = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(minor)
    return det