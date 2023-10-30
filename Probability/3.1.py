import random

import numpy as np
from numpy.typing import ArrayLike


class Strip:
    def __init__(self, length: int):
        self.length = length

    def cut(self) -> ArrayLike:
        first = random.random() * self.length
        second = self.length - first
        return np.array((first, second))


def probability(length: int, expected_value: int) -> float:
    results = np.array([Strip(length).cut() for _ in range(100000)])
    return len(results[results.max(axis=1) >= expected_value])/len(results)


L = int(input())
M = int(input())

print(f'{round(probability(L, M) * 100, 1)}%')