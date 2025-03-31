from typing import List
import random

def cocktail_sort(numbers: List[int]) -> List[int]:

    start, end = 0, len(numbers) -1

    swapped = True
    while swapped:
        swapped = False

        for i in range(start, end):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True

        if not swapped:
            break

        end -= 1

        for i in range(end -1, start -1, -1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True

        start += 1
    return numbers


if __name__ == '__main__':
    numbers = [random.randint(0,1000) for _ in range(5)]
    print(numbers)
    numbers = cocktail_sort(numbers)
    print(numbers)