def kidds_encryption(text, reverse=False):
    text = text.lower()
    alphabet = 'ethosnairfdlmbyguvcp'
    cript = '8;4‡)*56(1†092:3?¶-.'

    if reverse:
        alphabet, cript = cript, alphabet

    new_text = []
    for char in text:
        if char in alphabet:
            new_text.append(cript[alphabet.index(char)])
    return ''.join(new_text)



print(kidds_encryption('000', True))