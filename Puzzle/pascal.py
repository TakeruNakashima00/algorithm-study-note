from typing import List

def generate_pascal_traiangle(depth: int) -> List[List[int]]:

    data = [[1] * (i+1) for i in range(depth)]
    # [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1]] ex, depth=5
    for line in range(2, depth):
        for i in range(1, line):
            data[line][i] = data[line-1][i-1] + data[line-1][i]
    return data

def print_pascal(data: List[List[int]]) -> None:
    max_digit = len(str(max(data[-1])))
    width = max_digit + (max_digit % 2 ) + 2
    for index, line in enumerate(data):
        numbers = ''.join([str(x).center(width, ' ') for x in line])
        print(' ' * int(width/2) * (len(data) - index), numbers)

if __name__ == '__main__':
    print_pascal(generate_pascal_traiangle(10))