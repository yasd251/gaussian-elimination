# Python script for gaussian matrix (very rough version)
'''
The desired end matrix comes in the following form:
[. . . | .]
[0 . . | .]
[0 0 . | .]

Second row transformation: A=-R1/R2
Third row first transformation: B=-R1/R3
Third row second transformation: C=-R2/R3

A*R2 + R1 = 0
B*R3 + R1 = 0
C*R3 + R2 = 0

Well, this might not work for all edge cases, but assume that this is a suitable general formula for the time-being

This only works when the input is correct, there is no input sanitisation or any initial checks for if the system of equations is 
feasible in the first place
'''

main_matrix = []

def extract_coefficients(input_equation: str):
    # normally the equation will look something like: 2x+3y+6z=5
    # split from = to get LHS and RHS
    full_equation = input_equation.split('=')
    
    result = int(full_equation[1])

    LHS = full_equation[0]
    coefficients = LHS.split('+')
    x = int(coefficients[0].split('x')[0])
    y = int(coefficients[1].split('y')[0])
    z = int(coefficients[2].split('z')[0])
    return [x, y, z, result]

for i in range (0, 3):
    input_equation = input(f"Enter equation {i+1} here: ")
    row = extract_coefficients(input_equation)
    main_matrix.append(row)

print(main_matrix)

def scalar_multiplication(matrix: list, coefficient: int, main_row_index: int, secondary_row_index: int):
    for i in range(0, 4):
        matrix[main_row_index][i] = (coefficient*matrix[main_row_index][i])+matrix[secondary_row_index][i]
    return matrix

def first_transformation(main_matrix):
    # find first A coefficient from the R2C1 and R1C1
    A = -(main_matrix[0][0])/(main_matrix[1][0])
    main_matrix = scalar_multiplication(main_matrix, A, 1, 0)
    return main_matrix

def second_transformation(matrix):
    # find B coefficient from the R3C1 and R1C1
    B = -(matrix[0][0])/(matrix[2][0])
    matrix = scalar_multiplication(matrix, B, 2, 0)
    return matrix

def third_transformation(matrix):
    # find C coefficient from the R3C2 and R2C2
    C = -(matrix[1][1])/(matrix[2][1])
    matrix = scalar_multiplication(matrix, C, 2, 1)
    return matrix

eliminated_matrix = third_transformation(
                        second_transformation(
                            first_transformation(main_matrix)
                        )
                    )

z = eliminated_matrix[2][3]/eliminated_matrix[2][2]
y = (eliminated_matrix[1][3]-(eliminated_matrix[1][2]*z))/eliminated_matrix[1][1]
x = (eliminated_matrix[0][3]-(eliminated_matrix[0][1]*y)-(eliminated_matrix[0][2]*z)) / eliminated_matrix[0][0]

print((x,y,z))

# solving for z = matrix[2][3] / matrix[2][2]
# solving for y = ([1][3]-([1][2]*z))/[1][1]
# solving for x = ([0][3]-([0][2]*z)-([0][1]*y)) / [0][0]