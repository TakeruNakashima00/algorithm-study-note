from typing import List

def order_even_first_odd_last_v1(numbers: List[int]) -> None:
    even_list = []
    odd_list = []

    for i in numbers:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    numbers[:] = even_list + odd_list


def order_even_first_odd_last_v2(numbers: List[int]) -> None:
    left, right = 0, len(numbers) -1

    while left < right:
        if numbers[left] % 2 == 0:
            left += 1
        else:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            right -= 1



if __name__ == '__main__':
    numbers = [0,1,3,4,2,4,5,1,6,9,8]
    order_even_first_odd_last_v2(numbers)
    print(numbers)

# v1: [0, 4, 2, 4, 6, 8, 1, 3, 5, 1, 9]
# v2: [0, 8, 6, 4, 2, 4, 1, 5, 9, 3, 1]