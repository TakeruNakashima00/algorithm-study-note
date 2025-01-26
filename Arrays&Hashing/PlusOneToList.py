
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


if __name__ == '__main__':
    numbers = [0,0,9,9,9,9]
    print(plus_one_to_list(numbers))