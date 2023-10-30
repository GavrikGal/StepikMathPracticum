import random

expected = list('🂡🂱🃁🃑')

cards = list(input())
# cards = list('🂡🂱🃁🃑🃖')

success = 0
iter_count = 100000
for _ in range(iter_count):
    random.shuffle(cards)
    hits = 0
    for card in cards:
        if card in expected:
            hits += 1
            if hits == len(expected):
                break
        else:
            hits = 0
    if hits == len(expected):
        success += 1

probability = success / iter_count

print(f'{round(probability * 100, 2)}%')

