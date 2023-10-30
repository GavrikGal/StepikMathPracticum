import numpy as np
from random import choice


def coins_flip(n: int) -> int:
    heads_tails = [0, 1]
    return sum([choice(heads_tails) for _ in range(n)])


def tails_probability(n: int, m: int) -> float:
    results = np.array([coins_flip(n) for _ in range(100000)])
    return len(results[results <= m])/len(results)


n = int(input())
m = int(input())
result = tails_probability(n, m)

print(f'{round(result * 100, 1)}%')