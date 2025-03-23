"""
Input: Hello World
Output: Khoor Zruog
"""
import string
from typing import Generator, Tuple

def caesar_cipher(text: str, shift: int) -> str:
    result = ""

    for char in text:
        if char.islower():
            alphabet_len = ord('z') - ord('a') + 1
            result += chr((ord(char) + shift - ord('a')) % alphabet_len + ord('a'))
        elif char.isupper():
            alphabet_len = ord('Z') - ord('A') + 1
            result += chr((ord(char) + shift - ord('A')) % alphabet_len + ord('A'))
        else:
            result += char
    return result


def caesar_cipher_hack(text: str) -> Generator[Tuple[int, str], None, None]:

    alphabet_len = ord('Z') - ord('A') + 1

    for candidate_shift in range(1, alphabet_len + 1):
        reverted = ''
        for char in text:
            if char.islower():
                alphabet = string.ascii_lowercase
            elif char.isupper():
                alphabet = string.ascii_uppercase
            else:
                reverted += char
                continue
            index = alphabet.index(char) - candidate_shift

            if index < 0:
                index += alphabet_len
            reverted += alphabet[index]
        yield candidate_shift, reverted

encypted_string = caesar_cipher("Hello World", 3)

for candidate in caesar_cipher_hack(encypted_string):
    print(candidate)


"""
lower character
ord('a') : 97
ord('z') : 122

upper character
ord('A') : 65
ord('Z') : 90
"""