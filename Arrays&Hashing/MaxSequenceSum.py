"""
1. Maximun subarray sum sum
Input: [1, -2, 3, 6, -1, 2, 4, -5, 2]
Output: 14 (3, 6, -1, 2, 4)

2. Maximum circular subarray sum
Input: [1, -2, 3, 6, -1, 2, 4, -5, 2]
Output: 15 (2, 1, -2, 3, 6, -1, 2, 4)
"""

from typing import List

def get_max_sequence_sum(numbers: List[int]) -> int:
    result_sequence_num, sum_sequnece_num = 0, 0

    for number in numbers:
        temp_sequence_num = sum_sequnece_num + number

        # check if sum_sequnece_num variable change or not
        if temp_sequence_num < number:
            sum_sequnece_num = number
        else:
            sum_sequnece_num = temp_sequence_num

        if result_sequence_num < sum_sequnece_num:
            result_sequence_num = sum_sequnece_num

    return result_sequence_num


if __name__ == '__main__':

    print(get_max_sequence_sum([1, -2, 3, 6, -1, 2, 4, -5, 2]))