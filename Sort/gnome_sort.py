from typing import List
import random

def gnome_sort(numbers: List[int]) -> List[int]:
    current_pointer, len_numbers = 0, len(numbers)

    while current_pointer != len_numbers-1:

        if numbers[current_pointer] < numbers[current_pointer+1]:
            current_pointer += 1
        else:
            numbers[current_pointer], numbers[current_pointer+1] = numbers[current_pointer+1], numbers[current_pointer]
            if current_pointer != 0:
                current_pointer -= 1
    return numbers

if __name__ == '__main__':
    numbers = [random.randint(0,1000) for _ in range(10)]
    print(numbers)
    numbers = gnome_sort(numbers)
    print(numbers)
