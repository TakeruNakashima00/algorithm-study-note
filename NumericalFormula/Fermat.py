from typing import Tuple, List
import sys
import time

def fermat_last_theorem_v1(max_num: int, square_num: int) -> List[Tuple[int, int, int]]:
    result = []
    if square_num < 2:
        return result

    max_z = int(pow((max_num-1) ** 2 + (max_num) ** 2, 1.0/square_num))
    for x in range(1, max_num +1):
        for y in range(x +1, max_num +1):
            for z in range(y+1, max_z):
                if pow(x, square_num) + pow(y, square_num) == pow(z, square_num):
                    result.append((x,y,z))
    return result

def fermat_last_theorem_v2(max_num: int, square_num: int) -> List[Tuple[int, int, int]]:
    result = []
    if square_num < 2:
        return result

    for x in range(1, max_num +1):
        for y in range(x +1, max_num +1):
            pow_sum = pow(x, square_num) + pow(y, square_num)

            if pow_sum > sys.maxsize:
                raise ValueError()

            z = pow(pow_sum, 1.0/square_num)
            # if (x**2 + y**2)**(1/2) is integer
            if not z.is_integer():
                continue
            z = int(z)

            if pow_sum == pow(z, square_num):
                result.append((x,y,z))

    return result

if __name__ ==  '__main__':
    start1 = time.time()
    print('v1', fermat_last_theorem_v1(20, 2))
    print('v1', 'time =', time.time() - start1)

    start2 = time.time()
    print('v2', fermat_last_theorem_v2(20, 2))
    print('v2', 'time =', time.time() - start2)