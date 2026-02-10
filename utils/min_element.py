def find_min(matrix):
    min_val = float('inf')
    min_i, min_j = -1, -1
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val < min_val:
                min_val = val
                min_i, min_j = i, j
    return min_val, min_i, min_j