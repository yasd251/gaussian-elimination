# Gaussian elimination algorithm

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
coefficient_A = 0
coefficient_B = 0
coefficient_C = 0

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
    return (x, y, z, result)

for i in range (0, 3):
    input_equation = input(f"Enter equation {i+1} here: ")
    row = extract_coefficients(input_equation)
    print(row)
    main_matrix.append(row)

def first_transformation():
    # find first A coefficient from the R2C1 and R1C1
    A = -(main_matrix[0][0])/(main_matrix[1][0])
    return A
print(first_transformation())
