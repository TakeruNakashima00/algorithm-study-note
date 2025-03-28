"""
Input: plain_text: "ATTACK SILICON VALLEY", key: "HELLO"
"""
import string

ALPHABET = string.ascii_uppercase

def generateKey(plain_text: int, key: str) -> str:
    plain_text_len = len(plain_text)

    for i in range(0, plain_text_len):
        if len(key) == plain_text_len:
            break
        key += key[i]
    return key

def encypto(plain_text, key) -> str:
    print(key)
    result = ''

    for i, char in enumerate(plain_text):
        if char not in ALPHABET:
            result += char
            continue
        index = (ALPHABET.index(char) + ALPHABET.index(key[i])) % len(ALPHABET)
        result += ALPHABET[index]
    return result

def decypto(encypted_text, key) -> str:
    result = ''

    for i, char in enumerate(encypted_text):
        if char not in ALPHABET:
            result += char
            continue
        index = (ALPHABET.index(char) - ALPHABET.index(key[i]) + len(ALPHABET)) % len(ALPHABET)
        result += ALPHABET[index]
    return result


if __name__ == '__main__':
    t = 'ATTACK SILICON VALLEY'
    k = generateKey(t, 'HELLO')
    e = encypto(t, k)
    print(e)
    d = decypto(e, k)
    print(d)

