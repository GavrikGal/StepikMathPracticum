import re

S = input()

words = re.split('[^a-z]', S.lower())

print(words)