import numpy as np
from typing import List


def linear_equation(strings: List[str]) -> str:
    lead_vars = []
    free_vars = []

    for string in strings:
        variables = list(map(int, string.split()))
        lead_vars.append(variables[:-1])
        free_vars.extend(variables[-1:])

    matrix = np.array(lead_vars)
    vect = np.array(free_vars)

    det = np.linalg.det(matrix)

    if det == 0:
        return 'Такой класс не существует'

    result = np.linalg.solve(matrix, vect)

    for var in result:
        if (var < 0) or (var % 1 != 0):
            return 'Такой класс не существует'

    result = map(int, result)
    result = map(str, result)

    return ' '.join(result)


num_of_strings = 2

a, b = map(int, input().split())

strings = [f'1 1 {a}', f'1 -1 {b}']

result = linear_equation(strings)
print(result)
