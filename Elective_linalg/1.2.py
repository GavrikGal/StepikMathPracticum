import numpy as np


def two_linear_equation(str1: str, str2: str) -> str:
    a11, a12, b1 = map(int, str1.split())
    a21, a22, b2 = map(int, str2.split())

    matrix = np.array([[a11, a12],
                       [a21, a22]])
    vect = np.array([b1, b2])

    det = np.linalg.det(matrix)

    if det == 0:
        return 'Матрица системы вырожденная'

    x, y = np.linalg.solve(matrix, vect)

    result = map(str, (x, y))

    return ' '.join(result)


str1 = input()
str2 = input()

result = two_linear_equation(str1, str2)
print(result)
