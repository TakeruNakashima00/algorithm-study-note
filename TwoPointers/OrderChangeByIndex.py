from typing import List

"""
Input: ['h', 'y', 'n', 'p', 't' , 'o'], [3, 1, 5, 0, 2, 4]
Output: python
"""

def order_change_by_index_v1(chars: List[str], indexes: List[int]) -> str:

    temp = [None] * len(chars)
    for i, index in enumerate(indexes):
        temp[index] = chars[i]
    return ''.join(temp)


def order_change_by_index_v2(chars: List[str], indexes: List[int]) -> str:

    i, len_indexes = 0, len(indexes)

    while i < len_indexes:
        while i != indexes[i]:
            index = indexes[i]
            indexes[i], indexes[index] = indexes[index], indexes[i]
            chars[i], chars[index] = chars[index], chars[i]
        i += 1
    return ''.join(chars)


if __name__ == '__main__':
    w = ['h', 'y', 'n', 'p', 't' , 'o']
    i = [3, 1, 5, 0, 2, 4]
    print(order_change_by_index_v2(w, i))