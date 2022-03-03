# ____________________________________
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f'{n} is divisible by {x}')
            break
    else:
        print(f'{n} is a prime number')
# ____________________________________


# ____________________________________
for n in range(2, 10):
    # Generator that gives all the divisors of n:
    divisors = (x for x in range(2, n) if n % x == 0)
    # Take first divisor
    d = next(divisors, None)
    if d is None:
        print(n, 'is a prime number')
    else:
        print(f'{n} is divisible by {d}')
# ____________________________________


# ____________________________________
for n in range (2, 10):
    if any(x for x in range(2, n) if n % x == 0):
        # any(iterable) True if there's atl one value not False in the iterable
        print('n is no prime')
    else:
        print(n, 'is a prime number')
# ____________________________________