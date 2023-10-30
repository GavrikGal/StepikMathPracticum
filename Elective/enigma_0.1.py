# class Rotor:
#     input: str
#     output: str
#     shift: int
#     pos: int = 0
#
#     def __init__(self, n, shift):
#         ROTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
#                   1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
#                   2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
#                   3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
#                   4: 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
#                   5: 'VZBRGITYUPSDNHLXAWMJQOFECK',
#                   6: 'JPGVOUMFYQBENHZRDKASXLICTW',
#                   7: 'NZJHGRCXMYSWBOUFAIVLPEKQDT',
#                   8: 'FKQHTLXOCBJSPDZRAMEWNIUYGV',
#                   'beta': 'LEYJVCNIXWPBQMDRTAKZGFUHOS',
#                   'gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD'
#                   }
#         self.input = ROTORS[0]
#         self.output = ROTORS[n]
#         self.shift = shift
#
#     def cript(self, symbol, reverse=False):
#         input_ = self.input
#         output_ = self.output
#         if reverse:
#             input_, output_ = output_, input_
#         cript_symbol = shift(symbol, self.shift)
#         cript_symbol = output_[input_.index(cript_symbol)]
#         cript_symbol = shift(cript_symbol, self.shift, reverse=True)
#         return cript_symbol
#
#     @staticmethod
#     def shift(char: str, key: int, reverse=False):
#         alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#         if reverse:
#             key *= -1
#         return alphabet[(alphabet.index(char) + key) % len(alphabet)]
#
#
# def rotor(symbol, n, reverse=False):
#     ROTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
#               1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
#               2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
#               3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
#               4: 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
#               5: 'VZBRGITYUPSDNHLXAWMJQOFECK',
#               6: 'JPGVOUMFYQBENHZRDKASXLICTW',
#               7: 'NZJHGRCXMYSWBOUFAIVLPEKQDT',
#               8: 'FKQHTLXOCBJSPDZRAMEWNIUYGV',
#               'beta': 'LEYJVCNIXWPBQMDRTAKZGFUHOS',
#               'gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD'
#               }
#     input_rotor = 0
#     output_rotor = n
#     if reverse:
#         input_rotor, output_rotor = output_rotor, input_rotor
#     alph = ROTORS[input_rotor]
#     cript = ROTORS[output_rotor]
#     return cript[alph.index(symbol)]
#
#
# def reflector(symbol, n):
#     REFLECTOR = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
#                  1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT'}
#     alph = REFLECTOR[0]
#     cript = REFLECTOR[n]
#     return cript[alph.index(symbol)]
#
#
# def normalize(text: str):
#     replacing = [' ', ',', '.', ';', ':', '!', '?', "'", '"', '\n', '\t']
#     for mark in replacing:
#         text = text.replace(mark, '')
#     return text.upper()
#
#
# def shift(char: str, key: int, reverse=False):
#     alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     if reverse:
#         key *= -1
#     return alphabet[(alphabet.index(char) + key) % len(alphabet)]
#
#
# def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3):
#     text = normalize(text)
#     new_text = []
#
#     rotor1 = Rotor(rot1, shift1)
#     rotor2 = Rotor(rot2, shift2)
#     rotor3 = Rotor(rot3, shift3)
#
#     for char in text:
#         # char = shift(char, shift3, reverse=False)
#         char = rotor3.cript(char, reverse=False)
#         # char = shift(char, shift3, reverse=True)
#
#         # char = shift(char, shift2, reverse=False)
#         char = rotor2.cript(char, reverse=False)
#         # char = shift(char, shift2, reverse=True)
#
#         # char = shift(char, shift1, reverse=False)
#         char = rotor1.cript(char, reverse=False)
#         # char = shift(char, shift1, reverse=True)
#
#         char = reflector(char, ref)
#
#         # char = shift(char, shift1, reverse=False)
#         char = rotor1.cript(char, reverse=True)
#         # char = shift(char, shift1, reverse=True)
#
#         # char = shift(char, shift2, reverse=False)
#         char = rotor2.cript(char, reverse=True)
#         # char = shift(char, shift2, reverse=True)
#
#         # char = shift(char, shift3, reverse=False)
#         char = rotor3.cript(char, reverse=True)
#         # char = shift(char, shift3, reverse=True)
#         new_text.append(char)
#     return ''.join(new_text)
#
#
# print(enigma('AYIQQLXZMFHQUHQCH', 1, 1, -1, 2, 2, 3, -1))
#
