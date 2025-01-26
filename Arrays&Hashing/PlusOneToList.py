
"""
[1] => [2] 12
[2,3] => [2,4] 24
[8,9] => [9,0] 90
[9,9] => [1,0,0] 100
[1,2,3] => [1,2,4] 124
[7,8,9] => [7,9,0] 790
[9,9,9] => [1,0,0,0] 1000
[9,9,9,9] => [1,0,0,0,0] 10000
[0,0,9,9,9,9] => [1,0,0,0,0] 10000
"""
from typing import List

# def plus_one_to_list(numbers: List[int]) -> List[int]:
#     return int(''.join([str(num) for num in numbers])) + 1


def remove_zeo(numbers: List[int]) -> None:
    if numbers and numbers[0] == 0:
        numbers.pop(0)
        remove_zeo(numbers)

def list_to_int(numbers: List[int]) -> int:
    sum_numbers = 0
    for i, num in enumerate(reversed(numbers)):
        print("i:",i)
        print("num:",num)
        sum_numbers += num * (10 ** i)
    return sum_numbers

def plus_one_to_list(numbers: List[int]) -> int:
    i = len(numbers) -1
    numbers[i] += 1
    while 0 < i:
        if numbers[i] != 10:
            remove_zeo(numbers)
            break
        # 7, 8, 9 => 7, 9, 10
        numbers[i] = 0
        numbers[i-1] += 1

        i -= 1
    else:
        if numbers[0] == 10:
            numbers[0] = 1
            numbers.append(0)

    return list_to_int(numbers)

if __name__ == '__main__':
    numbers = [9,9,9]
    print(plus_one_to_list(numbers))


"""
numbers:[List[int]] => numbers:intに変換

numbers : [1,2,3]
index:    [10**0, 10**1, 10**2]

pattern
- one place
    just plus one
    when 10, one place 0, tens place +1
- remove 0 in list by recursive
- when 0 in list[10], append 0 last value in list
"""