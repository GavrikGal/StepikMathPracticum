from random import choice


def dice_probability(n: int) -> str:
    dices = range(1, n+1)
    results = [choice(dices) for _ in range(100000)]
    probability = results.count(1) / len(results)
    return f'{round(probability * 100, 1)}%'


dice_count = int(input())

print(dice_probability(dice_count))
