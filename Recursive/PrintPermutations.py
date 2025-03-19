# from itertools import permutations
# for i in permutations([1,2,3]):
#     print(i)
from typing import List

"""
Input: [1,2,3]

Output:
(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)
"""


def all_perms(elements: List[int]) -> List[List[int]]:
    result = []

    if len(elements) <= 1:
        return [elements]

    for pem in all_perms(elements[1:]):
        for i in range(len(elements)):
            result.append(pem[:i] + elements[0:1] + pem[i:])

    return result

if __name__ == '__main__':
    for l in (all_perms([1,2,3,4])):
        print(l)