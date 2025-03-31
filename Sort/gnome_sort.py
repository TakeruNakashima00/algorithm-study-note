from typing import List
import random

def gnome_sort(numbers: List[int]) -> List[int]:
    index, len_numbers = 0, len(numbers)

    while index < len_numbers:

        if index == 0:
            index += 1
        elif numbers[index] >= numbers[index-1]:
            index += 1
        else:
            numbers[index], numbers[index-1] = numbers[index-1], numbers[index]
            index -= 1

    return numbers

if __name__ == '__main__':
    numbers = [random.randint(0,1000) for _ in range(10)]
    print(numbers)
    numbers = gnome_sort(numbers)
    print(numbers)
