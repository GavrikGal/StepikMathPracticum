from random import shuffle, seed


def disc_generator(alphabet):
    list_ = list(str(alphabet))
    shuffle(list_)
    return ''.join(list_)

def normalize(text: str):
    replacing = [' ', ',', '.', ';', ':', '!', '?', "'", '"', '\n']
    for mark in replacing:
        text = text.replace(mark, '')
    return text.upper()

def caesar(text: str, key: int, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ',
           reverse=False):
    if reverse:
        key *= -1
    text = normalize(text)
    new_text = ''.join([alphabet[(alphabet.index(char) + key) % len(alphabet)] for char in text])
    return new_text

clear_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
n = 36
text = 'ДЮИЖЖНККЩЖТЮШМЦНЩЦДЕМХННОЭЛАПОВЖМЯЬБГЙПМЩХАВЫЖВНМСНЯВНЮДХЖГЖГХФЫСДХЯЖЕСТЬЗШШ'
seed(42)
discs = [disc_generator(clear_alphabet) for _ in range(n)]


def jefferson_encryption(text, discs, step, reverse=False):
    text = normalize(text)
    if reverse:
        step *= -1

    new_text = []
    for i, char in enumerate(text):
        disc_index = i % len(discs)
        new_char = discs[disc_index][(discs[disc_index].index(char)
                                      + step) % len(discs[disc_index])]
        new_text.append(new_char)

    return ''.join(new_text)



print(jefferson_encryption(text, discs, 4, reverse=True))
print(discs)

