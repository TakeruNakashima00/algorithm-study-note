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


if __name__ == '__main__':
    numbers = [str(i) for _ in range(5) for i in range(10)]
    strings = ''.join(numbers)
    for line in snake_string_v1(strings):
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