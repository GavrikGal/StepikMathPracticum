import numpy as np
from typing import List


def check_even(num_list: List[int]) -> int:
    even = 1
    for i, num in enumerate(num_list):
        next_num_list = num_list[i+1:]
        for next_num in next_num_list:
            even *= next_num - num
    return int(even/abs(even))


def get_win_num_list(n: int, m: int) -> List[int]:
    num_list = [num for num in range(1, m*n)]
    num_list.append(0)
    num_list = np.array(num_list).reshape((m, n))
    for i, row in enumerate(num_list):
        if i % 2 != 0:
            num_list[i] = row[::-1]
    num_list = num_list.flatten().tolist()
    num_list.pop(num_list.index(0))
    return num_list


n, m = map(int, input().split())
win_number_list = get_win_num_list(n, m)

number_list = []
for _ in range(n):
    number_list.extend(map(int, input().split()))


if check_even(win_number_list) == check_even(number_list):
    print('Бинго!')
else:
    print('Не повезло...')
