"""
Input: X: [1, 2, 3, 4, 4, 5, 5, 8, 10] Y: [4, 5, 5, 5, 6, 7, 8, 8, 10]
 =>    X: [1, 2, 3, 4, 4, 10]          Y: [5, 5, 5, 6, 7, 8, 8, 10]
"""

from typing import List
from collections import Counter

def min_count_remove(x: List[int], y: List[int]) -> None:
    # count_x = {}
    # count_y = {}
    # for i in x:
    #     count_x[i] = count_x.get(i, 0) + 1
    # for i in y:
    #     count_y[i] = count_y.get(i, 0) + 1

    counter_x = Counter(x)
    counter_y = Counter(y)
    print(counter_x)
    print(counter_y)

    for key_x, value_x in counter_x.items():
        value_y = counter_y.get(key_x)
        if value_y:
            if value_x < value_y:
                x[:] = [i for i in x if i != key_x]
            elif value_x > value_y:
                y[:] = [i for i in y if i != key_x]

if __name__ == '__main__':
    x = [1, 2, 3, 4, 4, 5, 5, 8, 10]
    y = [4, 5, 5, 5, 6, 7, 8, 8, 10]
    print(x)
    print(y)
    min_count_remove(x, y)
    print(x)
    print(y)



"""
HashTable/MinCountRemove.py
[1, 2, 3, 4, 4, 5, 5, 8, 10]
[4, 5, 5, 5, 6, 7, 8, 8, 10]
Counter({4: 2, 5: 2, 1: 1, 2: 1, 3: 1, 8: 1, 10: 1})
Counter({5: 3, 8: 2, 4: 1, 6: 1, 7: 1, 10: 1})
[1, 2, 3, 4, 4, 10]
[5, 5, 5, 6, 7, 8, 8, 10]"""