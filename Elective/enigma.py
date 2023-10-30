from typing import List


class Rotor:
    type: int
    input: str
    output: str
    shift_step: int
    shift_rotate_pos: int
    need_rotation: bool

    def __init__(self, n: int, shift_step: int):
        rotors = {0: ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 0),
                  1: ('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 17),
                  2: ('AJDKSIRUXBLHWTMCQGZNPYFVOE', 5),
                  3: ('BDFHJLCPRTXVZNYEIWGAKMUSQO', 22),
                  4: ('ESOVPZJAYQUIRHXLNFTGKDCMWB', 10),
                  5: ('VZBRGITYUPSDNHLXAWMJQOFECK', 0),
                  6: ('JPGVOUMFYQBENHZRDKASXLICTW', 0),     # 0 or 13
                  7: ('NZJHGRCXMYSWBOUFAIVLPEKQDT', 0),     # 0 or 13
                  8: ('FKQHTLXOCBJSPDZRAMEWNIUYGV', 0)      # 0 or 13
                  # 'beta': 'LEYJVCNIXWPBQMDRTAKZGFUHOS',
                  # 'gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD'
                  }
        self.type = n
        self.input = rotors[0][0]
        self.output = rotors[n][0]
        self.shift_rotate_pos = rotors[n][1]
        self.shift_step = shift_step
        self.need_rotation = False

    def encrypt(self, symbol: str, reverse: bool = False):
        input_ = self.input
        output_ = self.output

        if reverse:
            input_, output_ = output_, input_

        cript_symbol = self.shift(symbol, self.shift_step)
        cript_symbol = output_[input_.index(cript_symbol)]
        cript_symbol = self.shift(cript_symbol, self.shift_step, reverse=True)
        return cript_symbol

    def rotate(self):
        self.shift_step += 1
        self.shift_step %= 26
        self.need_rotation = False

    def hook_next(self) -> bool:
        return self.shift_step == self.shift_rotate_pos - 1

    @staticmethod
    def shift(char: str, key: int, reverse: bool = False):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if reverse:
            key *= -1
        return alphabet[(alphabet.index(char) + key) % len(alphabet)]

    def __repr__(self):
        return f'Rotor: (type = {self.type}, shift = {self.shift_step}, hook = {self.shift_rotate_pos})'


class Reflector:
    input: str
    output: str

    def __init__(self, n: int):
        reflectors = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                      1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT'}
        self.input = reflectors[0]
        self.output = reflectors[n]

    def reflect(self, symbol: str) -> str:
        return self.output[self.input.index(symbol)]


def normalize(text: str):
    replacing = [' ', ',', '.', ';', ':', '!', '?', "'", '"', '\n', '\t']
    for mark in replacing:
        text = text.replace(mark, '')
    return text.upper()


class PairValidationError(ValueError):
    ...


class Commutator:
    pairs: List[str]

    def __init__(self, pairs: str):
        self.__validate_pairs(pairs)
        self.pairs = list(map(normalize, pairs.split()))

    def commute(self, symbol: str) -> str:
        for pair in self.pairs:
            if symbol in pair:
                symbol = self.__commute_pair(symbol, pair)
        return symbol

    @staticmethod
    def __validate_pairs(pairs: str):
        pairs = normalize(pairs)
        if len(pairs) == len(set(pairs)):
            return True
        raise PairValidationError("Повторяющиеся значения в коммутационных парах")

    @staticmethod
    def __commute_pair(char, pair):
        index = abs(pair.index(char) - 1)
        return pair[index]


class RotationHandler:
    def __init__(self, rotors: List[Rotor]):
        self.rotors = rotors
        self.right_rotor = rotors[-1]

        self.right_rotor.need_rotation = True

    def rotate(self):
        for rotor in self.rotors[::-1]:
            if rotor.need_rotation:
                rotor.rotate()

            if rotor.hook_next():
                rotor.need_rotation = True

        self.__check_hook()
        self.right_rotor.need_rotation = True

    def __check_hook(self):
        is_hooked = False
        for rotor in self.rotors[::-1]:
            if is_hooked:
                rotor.need_rotation = True
                is_hooked = False
            if rotor.hook_next():
                is_hooked = True


class Counter:
    def __init__(self):
        self.count: int = 0
        self.space: bool = False
        self.space_freq: int = 0

    def add_space_to(self, char: str) -> str:
        if self.space and self.count % self.space_freq == 0:
            char += ' '
        return char

    def inc(self):
        self.count += 1


class Enigma:
    def __init__(self, ref, pairs="", *args):
        self.commutator = Commutator(pairs)
        self.reflector = Reflector(ref)
        self.rotors = [Rotor(rot, shift) for rot, shift in list(zip(*[iter(args)] * 2))]
        self.handler = RotationHandler(self.rotors)
        self.spaces_enable = False
        self.symbol_count = 0
        self.spaces_freq = 0
        self.counter = Counter()

    def encrypt(self, symbol: str) -> str:
        symbol = self.commutator.commute(symbol)

        self.handler.rotate()

        for rotor in self.rotors[::-1]:
            symbol = rotor.encrypt(symbol, reverse=False)

        symbol = self.reflector.reflect(symbol)

        for rotor in self.rotors:
            symbol = rotor.encrypt(symbol, reverse=True)

        symbol = self.commutator.commute(symbol)

        self.counter.inc()
        if self.counter.space:
            symbol = self.counter.add_space_to(symbol)

        return symbol

    def enable_spaces(self, enable: bool, n: int):
        self.counter.space = enable
        self.counter.space_freq = n


def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3, pairs=""):
    try:
        enigma_ = Enigma(ref, pairs, rot1, shift1, rot2, shift2, rot3, shift3)
        enigma_.enable_spaces(False, 5)
        text = normalize(text)
        new_text = []
        for char in text:
            new_text.append(enigma_.encrypt(char))
        return ''.join(new_text)

    except PairValidationError:
        return "Извините, невозможно произвести коммутацию"


print(enigma('AAAAA'*21, 1, 1, 0, 2, 0, 3, 0))
