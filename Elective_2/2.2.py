with open('dataset_48784_9 (1).txt') as file:
    lines = file.read().splitlines()

first_symbols = [word[0] for word in lines]

first_symbols = ' '.join(first_symbols)

print(first_symbols)