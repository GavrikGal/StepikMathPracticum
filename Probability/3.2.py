import numpy as np
from numpy.typing import ArrayLike


class Strip:
    def __init__(self, length: int):
        self.length = length

    def cut(self, count: int = 2) -> ArrayLike:
        # cut_points = np.random.uniform(0, self.length, count - 1)
        # x1 = np.append(cut_points, self.length)
        # x1.sort()
        # x2 = np.append(cut_points, 0)
        # x2.sort()
        # slices = x1 - x2

        cut_points = np.random.uniform(0, self.length, count - 1)
        cut_points.sort()
        slices = np.diff(cut_points, prepend=0, append=self.length)

        return slices


def probability(length: int, expected_value: int,
                cut_count: int = 2) -> float:
    results = np.array([Strip(length).cut(cut_count) for _ in range(100000)])
    return len(results[results.max(axis=1) >= expected_value])/len(results)


L = int(input())
N = int(input())
M = int(input())


print(f'{round(probability(L, M, N) * 100, 1)}%')