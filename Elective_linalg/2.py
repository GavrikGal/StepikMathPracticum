import numpy as np


def two_linear_equation(str1: str, str2: str, str3: str) -> str:
    a11, a12, a13, b1 = map(int, str1.split())
    a21, a22, a23, b2 = map(int, str2.split())
    a31, a32, a33, b3 = map(int, str3.split())

    matrix = np.array([[a11, a12, a13],
                       [a21, a22, a23],
                       [a31, a32, a33]])
    vect = np.array([b1, b2, b3])

    det = np.linalg.det(matrix)

    if det == 0:
        return 'Матрица системы вырожденная'

    x, y, z = np.linalg.solve(matrix, vect)

    result = map(str, (x, y, z))

    return ' '.join(result)


str1 = input()
str2 = input()
str3 = input()

result = two_linear_equation(str1, str2, str3)
print(result)
