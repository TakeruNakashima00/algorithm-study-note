import operator
from typing import List


def snake_string_v1(chars: str) -> List[List[str]]:
    result = [[],[],[]]
    result_indexes = {0,1,2}
    insert_index = 1

    for i, s in enumerate(chars):
        if i % 4 == 1:
            insert_index = 0
        elif i % 2 == 0:
            insert_index = 1
        elif i % 4 == 3:
            insert_index = 2
        result[insert_index].append(s)

        # add '' to not set list
        for result_index in result_indexes - {insert_index}:
            result[result_index].append(' ')
    return result

def snake_string_v2(chars: str, depth: int) -> List[List[int]]:
    result = [[] for _ in range(depth)]
    result_indexes = {i for i in range(depth)}
    insert_index = int(depth / 2)

    op = operator.neg
    for s in chars:
        result[insert_index].append(s)
        for result_index in result_indexes - {insert_index}:
            result[result_index].append(' ')
        if insert_index <= 0:
            op = operator.pos
        if insert_index >= depth -1:
            op = operator.neg
        insert_index += op(1)

    return result


if __name__ == '__main__':
    numbers = [str(i) for _ in range(5) for i in range(10)]
    strings = ''.join(numbers)
    for line in snake_string_v1(strings):
        print(''.join(line))

    import string
    alphabet = [s for _ in range(2) for s in string.ascii_lowercase]
    for line in snake_string_v2(alphabet, 10):
        print(''.join(line))

"""
# python set can substract
{"0","1","2"} - {"1"} = {"0","2"}


# how to make "0123456789" in python
numbers = [str(i) for i in range(10)] ["0","1","2","3","4","5","6","7","8","9"]
strings = ''.join(numbers) "0123456789"


# list comprehension
l = []
for j in range(5):
    for i in range(10):
        l.append(i)

[str(i) for j in range(5) for i in range(10)]

"""