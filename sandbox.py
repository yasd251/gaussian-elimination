def scalar_multiplication(matrix: list, coefficient: int, main_row_index: int, secondary_row_index: int):
    for i in range(0, 4):
        matrix[main_row_index][i] = (coefficient*matrix[main_row_index][i])+matrix[secondary_row_index][i]
    return matrix

