import numpy as np
from numpy.typing import ArrayLike


def roll_dices(dice_count: int, side_count: int) -> ArrayLike:
    dices = range(1, side_count + 1)
    result = np.random.choice(dices, dice_count)
    return result


def probability(dice_count: int, side_count: int,
                expected_value: int) -> float:
    results = np.array([sum(roll_dices(dice_count, side_count))
                        for _ in range(100000)])
    return len(results[results >= expected_value])/len(results)


n = int(input())
m = int(input())
k = int(input())

print(f'{round(probability(n, m, k) * 100, 1)}%')
