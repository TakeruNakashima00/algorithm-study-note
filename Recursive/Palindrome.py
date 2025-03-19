"""
1. Check Palindrome
aba => True
abc => False
racecar => True

2. Find Palindrome
abcracecarbda => cec, aceca, racecar
"""

# s = "racecar"
# print(s == ''.join(reversed(s)))
# print(s == s[::-1])


def check_palindrome(char: str) -> bool:
    len_char = len(char)
    if not len_char:
        return False
    if len_char == 1:
        return True

    l, r = 0, len_char -1

    while l < r:
        if char[l] != char[r]:
            return False
        else:
            l += 1
            r -= 1
    return True


def find_palindrome(strings: str, left: int, right: int):
    result = []
    while 0 <= left and right <= len(strings) -1:
        if strings[left] != strings[right]:
            break
        result.append(strings[left: right+1])
        left -= 1
        right += 1
    return result

def find_all_palindrome(strings: str):
    result = []
    len_strings = len(strings)
    if not len_strings:
        return result
    if len_strings == 1:
        result.append(result)

    # aba
    # abba
    for i in range(1, len_strings-1):
        [result.append(s) for s in find_palindrome(strings, i-1, i+1)]
        [result.append(s) for s in find_palindrome(strings, i-1, i)]
    return result

if __name__ == '__main__':
    print(find_all_palindrome('cabbac'))