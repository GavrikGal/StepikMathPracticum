import numpy as np
from typing import List


def linear_equation(strings: List[str]) -> str:
    lead_vars = []
    free_vars = []

    for string in strings:
        variables = list(map(float, string.split()))
        lead_vars.append(variables[:-1])
        free_vars.extend(variables[-1:])

    matrix = np.array(lead_vars)
    vect = np.array(free_vars)

    det = np.linalg.det(matrix)

    if det == 0:
        return 'Матрица системы вырожденная'

    result = np.linalg.solve(matrix, vect)
    result = map(str, result)

    return ' '.join(result)


num_of_strings = int(input())

strings = []
for _ in range(num_of_strings):
    strings.append(input())

result = linear_equation(strings)
print(result)
