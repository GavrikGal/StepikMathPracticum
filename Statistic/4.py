import random
import numpy as np


def gen():
    return random.randint(0, 100)


sample = [gen() for _ in range(100000)]

mean = np.round(np.mean(sample), 2)
std = np.round(np.std(sample, ddof=1), 2)

print(f'Mean: {mean}')
print(f'Sd: {std}')
