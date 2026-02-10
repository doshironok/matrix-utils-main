def diagonal_sums(matrix):
    n = len(matrix)
    if not all(len(row) == n for row in matrix):
        raise ValueError("Матрица должна быть квадратной")
    main_diag = sum(matrix[i][i] for i in range(n))
    anti_diag = sum(matrix[i][n - 1 - i] for i in range(n))
    return main_diag, anti_diag