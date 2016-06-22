from math import sqrt
import timeit

def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step

def is_prime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))

def next_prime(num):
    if (not num & 1) and (num != 2):
        num += 1
    if is_prime(num):
        num += 1
    while True:
        if is_prime(num):
            break
        num += 1
    return num

def list_primes(n):
    start = timeit.default_timer()
    num = 2
    li = [2]

    while len(li) < n:
        num = next_prime(num)
        li.append(num)

    end = timeit.default_timer()

    print(end - start)

    return li
