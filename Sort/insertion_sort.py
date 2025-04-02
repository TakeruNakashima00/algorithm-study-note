from typing import List
import random


def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)

    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i -1
        while j >= 0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]
            j -= 1

        numbers[j+1] = temp
    return numbers

if __name__ == '__main__':
    numbers = [random.randint(1, 1000) for _ in range(6)]
    numbers = insertion_sort(numbers)
    print(numbers)
