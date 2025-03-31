from typing import List
import random

def selection_sort(numbers: List[int]) -> List[int]:

    len_numbers = len(numbers)

    for i in range(len_numbers):
        temp_num_index = i
        for x in range(i+1, len_numbers):
            if numbers[x] < numbers[temp_num_index]:
                temp_num_index = x
        numbers[i], numbers[temp_num_index] = numbers[temp_num_index], numbers[i]
    return numbers


if __name__ == '__main__':
    numbers = [random.randint(0,1000) for _ in range(5)]
    print(numbers)
    numbers = selection_sort(numbers)
    print(numbers)
