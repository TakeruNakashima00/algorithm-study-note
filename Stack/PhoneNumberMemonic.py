"""
Input: 568-379-8466 output [..., 'LOVEPYTHON], ...]
"""
from typing import List

NUM_ALPHABET_MAPPING = {
    0: '+',
    1: '@',
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PQRS',
    8: 'TUV',
    9: 'WXYZ'
}

# '23'
def phone_memonic_v1(phone_number: str) -> List[str]:
    phone_number = [int(s) for s in phone_number.replace('-','')]
    candidate = []
    tmp = [''] * len(phone_number)
    # ['A']
    def find_candidate_alphabet(digit: int=0) -> None:
        if digit == len(phone_number):
            candidate.append(''.join(tmp))
        else:
            for char in NUM_ALPHABET_MAPPING[phone_number[digit]]:
                tmp[digit] = char
                find_candidate_alphabet(digit+1)
    find_candidate_alphabet()
    return candidate


if __name__ == '__main__':
    print(phone_memonic_v1('23'))


"""
Solution
- Consider HashMap
- Convert str into List. By using ''.join(list) To use hashTable
- Convert List into str. By using [x for x in str]
- DFS(Depth First Search)
    think of finish statement
    using timing is search into depth
"""