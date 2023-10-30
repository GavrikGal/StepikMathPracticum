import numpy as np
from typing import List


def get_x_degree_list(x: float, n: int) -> List[float]:
    xs = []
    for degree in range(n+1):
        xs.append(x**degree)
    return xs


def linear_equation(strings: List[str]) -> str:
    variables = []

    for string in strings:
        xy = list(map(float, string.split()))
        variables.append(xy)

    degrees = len(strings) - 1

    xs = []
    ys = []
    for x, y in variables:
        xs.append(get_x_degree_list(x, degrees))
        ys.append(y)

    matrix = np.array(xs)
    vect = np.array(ys)

    det = np.linalg.det(matrix)

    if det == 0:
        return 'Матрица системы вырожденная'

    result = np.linalg.solve(matrix, vect)
    result = map(str, result)

    return ' '.join(result)


M = int(input())

strings = []
for _ in range(M):
    strings.append(input())

result = linear_equation(strings)
print(result)


