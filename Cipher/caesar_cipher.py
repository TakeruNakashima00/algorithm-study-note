"""
Input: Hello World
Output: Khoor Zruog
"""
import string

def caesar(text: str, shift: int) -> str:
    result = ""
    alphabet = ""
    for char in text:

        if char.islower():
            alphabet = string.ascii_lowercase
        elif char.isupper():
            alphabet = string.ascii_uppercase
        else:
            result += char
            continue

        result += alphabet[(alphabet.index(char) + shift ) % len(alphabet)]
    return result


print(caesar("Hello World", 3))