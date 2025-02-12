from typing import List, Generator

"""
loop
"""
def get_prime_number_v1(num: int) -> List[int]:
    primes = []
    for x in range(2, num+1):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            primes.append(x)
    return primes

"""
cache
"""
def get_prime_number_v2(num: int) -> List[int]:
    primes = []
    cache = {}

    for x in range(2, num+1):
        isPrime = cache.get(x)
        if isPrime is False:
            continue
        primes.append(x)
        cache[x] = True

        for y in range(2*x, num+1, x):
            cache[y] = False
    return primes

"""
cache&generator
"""
def get_prime_number_v3(num: int) -> Generator[int, None, None]:
    cache = {}

    for x in range(2, num+1):
        isPrime = cache.get(x)
        if isPrime is False:
            continue
        yield x
        cache[x] = True

        for y in range(2*x, num+1, x):
            cache[y] = False

if __name__ == '__main__':
    import time
    start = time.time()
    print(get_prime_number_v1(50))
    print(time.time() - start)

    start = time.time()
    print(get_prime_number_v2(50))
    print(time.time() - start)

    start = time.time()
    print([i for i in get_prime_number_v3(50)])
    print(time.time() - start)
