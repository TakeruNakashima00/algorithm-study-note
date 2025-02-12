"""
Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

[2, 3, 5, 7, 11, 13, 17, 19]
"""


def is_prime_number_v1(num: int) -> bool:

    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True



if __name__ == '__main__':
    print(is_prime_number_v1(19))