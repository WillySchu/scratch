def fn(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    return fn(n - 1) + fn(n - 2) + fn(n - 3)


print fn(7)
