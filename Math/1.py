from typing import List

data = list(map(int, input().split()))


def can_be_equal(data: List[int]):
    if len(data) < 2:
        print('Ошибка. Кучек слишком мало, чтобы можно было решить задачу.')
        return

    if len(data) == 2:
        if data[0] == data[1]:
            m, n = get_step_count(data)
            print(m, n)
            return
        else:
            print('Кучки нельзя уравнять')
            return

    if len(data) % 2 == 0:
        if sum(data) % 2 == 0:
            m, n = get_step_count(data)
            print(m, n)
            return
        else:
            print('Кучки нельзя уравнять')
            return
    else:
        m, n = get_step_count(data)
        print(m, n)
        return


def get_step_count(data: List[int]):
    m = 0
    equal = False
    while not equal:
        for elem in data[1:]:
            if data[0] == elem:
                equal = True
            else:
                equal = False
                break
        if equal:
            break

        data.sort()
        data[0] += 1
        data[1] += 1
        m += 1

    n = data[0]
    return m, n


can_be_equal(data)

