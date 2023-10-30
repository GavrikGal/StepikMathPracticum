# from typing import List, Union
#
# class Rotor:
#     type: int
#     input: str
#     output: str
#     shift_step: int
#     shift_rotate_pos: int
#
#     def __init__(self, n: int, shift_step: int):
#         rotors = {0: ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 0),
#                   1: ('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 17),
#                   2: ('AJDKSIRUXBLHWTMCQGZNPYFVOE', 5),
#                   3: ('BDFHJLCPRTXVZNYEIWGAKMUSQO', 22),
#                   4: ('ESOVPZJAYQUIRHXLNFTGKDCMWB', 10),
#                   5: ('VZBRGITYUPSDNHLXAWMJQOFECK', 0),
#                   6: ('JPGVOUMFYQBENHZRDKASXLICTW', 0),     # 0 or 13
#                   7: ('NZJHGRCXMYSWBOUFAIVLPEKQDT', 0),     # 0 or 13
#                   8: ('FKQHTLXOCBJSPDZRAMEWNIUYGV', 0)      # 0 or 13
#                   # 'beta': 'LEYJVCNIXWPBQMDRTAKZGFUHOS',
#                   # 'gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD'
#                   }
#         self.type = n
#         self.input = rotors[0][0]
#         self.output = rotors[n][0]
#         self.shift_rotate_pos = rotors[n][1]
#         self.shift_step = shift_step
#
#     def encrypt(self, symbol: str, reverse: bool = False):
#         input_ = self.input
#         output_ = self.output
#
#         if reverse:
#             input_, output_ = output_, input_
#
#         cript_symbol = self.shift(symbol, self.shift_step)
#         cript_symbol = output_[input_.index(cript_symbol)]
#         cript_symbol = self.shift(cript_symbol, self.shift_step, reverse=True)
#         return cript_symbol
#
#     def rotate(self, need_to_rotate: bool):
#         if need_to_rotate:
#             self.shift_step += 1
#             self.shift_step %= 26
#
#     def next_need_to_rotate(self) -> bool:
#         ...
#
#     def is_needed_to_rotate(self) -> bool:
#         ...
#
#     @staticmethod
#     def shift(char: str, key: int, reverse: bool = False):
#         alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#         if reverse:
#             key *= -1
#         return alphabet[(alphabet.index(char) + key) % len(alphabet)]
#
#     def __repr__(self):
#         return f'Rotor: (type = {self.type}, shift = {self.shift_step})'
#
#
# class Reflector:
#     input: str
#     output: str
#
#     def __init__(self, n: int):
#         reflectors = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
#                       1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT'}
#         self.input = reflectors[0]
#         self.output = reflectors[n]
#
#     def reflect(self, symbol: str) -> str:
#         return self.output[self.input.index(symbol)]
#
#
# def normalize(text: str):
#     replacing = [' ', ',', '.', ';', ':', '!', '?', "'", '"', '\n', '\t']
#     for mark in replacing:
#         text = text.replace(mark, '')
#     return text.upper()
#
#
# def validate_pairs(pairs: str):
#     pairs = normalize(pairs)
#     if len(pairs) == len(set(pairs)):
#         return True
#     # for i, char in enumerate(pairs):
#     #     if char in pairs[i+1:]:
#     #         return False
#     return False
#
#
# def change(char, pair):
#     index = abs(pair.index(char) - 1)
#     return pair[index]
#
#
# def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3, pairs=""):
#
#     if not validate_pairs(pairs):
#         return "Извините, невозможно произвести коммутацию"
#
#     pairs = pairs.split()
#     pairs = list(map(normalize, pairs))
#
#     text = normalize(text)
#     new_text = []
#     rotor1 = Rotor(rot1, shift1)
#     rotor2 = Rotor(rot2, shift2)
#     rotor3 = Rotor(rot3, shift3)
#
#     reflector = Reflector(ref)
#
#     for char in text:
#         for pair in pairs:
#             if char in pair:
#                 char = change(char, pair)
#
#         rotor3.rotate()
#         if rotor2.shift_step == rotor2.shift_rotate_pos - 1:
#             rotor2.rotate()
#             rotor1.rotate()
#         char = rotor3.encrypt(char, reverse=False)
#
#         if rotor3.shift_step == rotor3.shift_rotate_pos:
#             rotor2.rotate()
#         char = rotor2.encrypt(char, reverse=False)
#         char = rotor1.encrypt(char, reverse=False)
#
#         char = reflector.reflect(char)
#
#         char = rotor1.encrypt(char, reverse=True)
#         char = rotor2.encrypt(char, reverse=True)
#         char = rotor3.encrypt(char, reverse=True)
#
#         for pair in pairs:
#             if char in pair:
#                 char = change(char, pair)
#
#         new_text.append(char)
#     return ''.join(new_text)
#
#
# class PairValidationError(ValueError):
#     ...
#
#
# class Commutator:
#     pairs: List[str]
#
#     def __init__(self, pairs: str):
#         self.__validate_pairs(pairs)
#         self.pairs = list(map(normalize, pairs.split()))
#
#     def commute(self, symbol: str) -> str:
#         for pair in self.pairs:
#             if symbol in pair:
#                 symbol = self.__commute_pair(symbol, pair)
#         return symbol
#
#     @staticmethod
#     def __validate_pairs(pairs: str):
#         pairs = normalize(pairs)
#         if len(pairs) == len(set(pairs)):
#             return True
#         raise PairValidationError("Повторяющиеся значения в коммутационных парах")
#
#     @staticmethod
#     def __commute_pair(char, pair):
#         index = abs(pair.index(char) - 1)
#         return pair[index]
#
#
# class Enigma:
#     prev_rotor: Union[None, Rotor]
#
#     def __init__(self, ref, pairs="", *args):
#         self.commutator = Commutator(pairs)
#         self.reflector = Reflector(ref)
#         self.rotors = [Rotor(rot, shift) for rot, shift in list(zip(*[iter(args)] * 2))]
#         self.right_rotor = self.rotors[-1]
#         self.left_rotor = self.rotors[0]
#         self.current_rotor = self.right_rotor
#         self.prev_rotor = None
#
#     def encrypt(self, symbol: str) -> str:
#         symbol = self.commutator.commute(symbol)
#
#         for rotor in self.rotors[::-1]:
#             self.current_rotor = rotor
#             # print(symbol)
#             # print(f'{rotor}')
#             if rotor is self.right_rotor:
#                 rotor.rotate()
#             # if rotor is not self.right_rotor and rotor is not self.left_rotor:
#             #     if rotor.shift_step == rotor.shift_rotate_pos - 1:
#             #         rotor.rotate()
#             #         next_rotor = self.rotors[self.rotors.index(rotor) - 1]
#             #         next_rotor.rotate()
#             # if rotor is not self.left_rotor:
#             #     if rotor.shift_step == rotor.shift_rotate_pos:
#             #         next_rotor = self.rotors[self.rotors.index(rotor) - 1]
#             #         next_rotor.rotate()
#             if rotor is not self.right_rotor:
#                 if self.prev_rotor.shift_step == self.prev_rotor.shift_rotate_pos:
#                     rotor.rotate()
#                 if rotor is not self.left_rotor:
#                     if self.current_rotor.shift_step == self.current_rotor.shift_rotate_pos - 1:
#                         rotor.rotate()
#                         next_rotor = self.rotors[self.rotors.index(rotor) - 1]
#                         next_rotor.rotate()
#
#
#             symbol = rotor.encrypt(symbol, reverse=False)
#
#             self.prev_rotor = rotor
#
#         symbol = self.reflector.reflect(symbol)
#
#         for rotor in self.rotors:
#             symbol = rotor.encrypt(symbol, reverse=True)
#
#         symbol = self.commutator.commute(symbol)
#         return symbol
#
#
#
# def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3, pairs=""):
#     try:
#         enigma_ = Enigma(ref, pairs, rot1, shift1, rot2, shift2, rot3, shift3)
#         text = normalize(text)
#         new_text = []
#         for char in text:
#             new_text.append(enigma_.encrypt(char))
#         return ''.join(new_text)
#
#     except PairValidationError:
#         return "Извините, невозможно произвести коммутацию"
#
#
# # print('text = A; result =', enigma('A', 1, 1, 0, 2, 0, 3, 0, ''), '\n')
# # print('text = A; result =', enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC'), '\n')
# # print('text = A; result =', enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC qd'), '\n')
# # print('text = A; result =', enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC qd az'), '\n')
# # print('text = A; result =', enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC qd za'), '\n')
# print('text = AAAAAAA; result =', enigma('AAAAAAA', 1, 1, 0, 2, 0, 3, 0), '\n')
# print(enigma('AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA', 1, 2, 3, 2, 3, 2, 3))
#
# # print('text = AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA A; result =', enigma('AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA A', 1, 1, 0, 2, 0, 3, 0), '\n')
#
