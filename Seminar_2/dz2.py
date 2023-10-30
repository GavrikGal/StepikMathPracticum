import math
from collections import defaultdict
from typing import List, Dict


def list_pull(L: List[object]):
    new_list = []
    for elem in L:
        if type(elem) is not list:
            new_list.append(elem)
        else:
            new_list.extend(list_pull(elem))
    return new_list


def list_deepcopy(L: List[object]) -> List[object]:
    new_list = []
    for elem in L:
        if isinstance(elem, list):
            new_list.append(list_deepcopy(elem))
        else:
            new_list.append(elem)
    return new_list


list_ = [['one'], [343, 2], [[9, 9, 9], [[666, 666], [[[[42]]]]]]]


def verbing(s: str):
    if len(s) < 3:
        return s
    if s[-3:] != 'ing':
        s += 'ing'
    else:
        s += 'ly'
    return s

# print(verbing('swiming'))


def front_back(a: str, b: str) -> str:
    a_half = math.ceil(len(a) / 2)
    b_half = math.ceil(len(b) / 2)
    return a[:a_half] + b[:b_half] + a[a_half:] + b[b_half:]

# print(front_back('abcde', 'xyz'))


def mimic_dict(string: str) -> Dict[str, List]:
    m_dict = defaultdict(list)
    key = ""
    for word in string.split():
        m_dict[key].append(word)
        key = word
    return dict(m_dict)

# print(mimic_dict("""a cat and a dog
# a fly"""))

from random import choice, seed
seed(42)


def print_mimic(mimic_dict: Dict[str, List[str]], word: str = "") -> str:
    word_count = 200
    text = []
    for _ in range(word_count):
        text.append(word)
        if word not in mimic_dict.keys():
            word = ""
        word = choice(mimic_dict[word])
    return ' '.join(text).strip()

text = """We are not what we should be
We are not what we need to be
But at least we are not what we used to be
  -- Football Coach"""

print(print_mimic(mimic_dict(text), ''))

