"""
Input: Hello World
Output: Khoor Zruog
"""

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



print(caesar_cipher("Hello World", 3))


"""
lower character
ord('a') : 97
ord('z') : 122

upper character
ord('A') : 65
ord('Z') : 90
"""