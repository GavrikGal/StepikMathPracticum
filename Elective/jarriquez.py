def normalize(text: str):
    replacing = [' ', ',', '.', ';', ':', '!', '?', "'", '"', '\n']
    for mark in replacing:
        text = text.replace(mark, '')
    return text.upper()


def caesar(text: str, key: int, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    text = normalize(text)
    new_text = ''.join([alphabet[(alphabet.index(char) + key) % len(alphabet)] for char in text])
    return new_text


def bruteforce(text, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    for key in range(-1, -len(alphabet), -1):
        print(caesar(text, key, alphabet))


def jarriquez_encryption(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                         reverse=False):
    text = normalize(text)
    key = str(key)
    new_text = []
    n = -1 if reverse else 1
    for i, char in enumerate(text):
        new_text.append(alphabet[(alphabet.index(char) + n * int(key[i % len(key)])) % len(alphabet)])
    new_text = ''.join(new_text)
    return new_text


text = 'ЧУЦИЮЛКВУФКНЙУГУТССКЩДФИПЮРЯЛЦР'
key = 423
alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
reverse = True
# print(caesar(text, 3))
# print(jarriquez_encryption(text, key, alphabet=alphabet, reverse=reverse))

text = '''ТЛБЛДУЭППТКЛФЧУВНУПБКЗИХТЛТТЫХНЛОИНУВЖММИНПФНПШОКЧЛЕРНТФНАХЖИДМЯКЛТУБЖИУЕЖЕАХЛГЩЕЕ

ЪУВНГАХИЯШПЙАОЦЦПВТЛБФТТИИНДИДНЧЮОНЯОФВТЕАТФУШБЛРЮЮЧЖДРУУШГЕХУРПЧЕУВАЭУОЙБДБНОЛСКЦБ

САОЦЦПВИШЮТППЦЧНЖОИНШВРЗЕЗКЗСБЮНЙРКПСЪЖФФШНЦЗРСЭШЦПЖСЙНГЭФФВЫМЖИЛРОЩСЗЮЙФШФДЖО

ИЗТРМООЙБНФГОЩЧФЖООКОФВЙСЭФЖУЬХИСЦЖГИЪЖДШПРМЖПУПГЦНВКБНРЕКИБШМЦХЙИАМФЛУЬЙИСЗРТЕС'''

text = normalize(text)
alphabet = list(set(text))
alphabet.sort()
alphabet = ''.join(alphabet)
print(alphabet)
perhaps_word = [normalize('алмаз'), normalize("Дакоста")]

while True:
    for key in range(999, 999999):
        founded = 0
        new_text = jarriquez_encryption(text, key, alphabet=alphabet,
                                        reverse=True)
        for word in perhaps_word:
            if word in new_text:
                founded += 1
        if founded == len(perhaps_word):
            print(new_text)
            print(key)
            break

