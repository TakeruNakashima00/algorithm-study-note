"""
Input: plain_text: "ATTACK SILICON VALLEY", key: "HELLO"
"""
import string


def generateKey(plain_text_len: int, key: str) -> str:

    for i in range(0, plain_text_len):
        if len(key) == plain_text_len:
            break
        key += key[i]
    return key

def vigenere_cipher(plain_text, key) -> str:
    alphabet = string.ascii_uppercase
    key = generateKey(len(plain_text), key)
    print(key)
    result = ''

    # cypto
    for i, char in enumerate(plain_text):
        print(i)
        if char not in alphabet:
            result += char
            continue
        index = (alphabet.index(char) + alphabet.index(key[i])) % len(alphabet)
        result += alphabet[index]
    return result


if __name__ == '__main__':
    print(vigenere_cipher("ATTACK SILICON VALLEY", "HELLO"))

