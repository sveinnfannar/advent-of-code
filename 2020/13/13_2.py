# coding: utf-8

from functools import reduce
import math

# for i, x in xs:
#     print(f'(a + {i}) % {x} == 0 and \\')
# exit()


# Eval function for real input
def eval_real(a):
    return (a + 0) % 29 == 0 and \
           (a + 19) % 41 == 0 and \
           (a + 29) % 661 == 0 and \
           (a + 42) % 13 == 0 and \
           (a + 43) % 17 == 0 and \
           (a + 52) % 23 == 0 and \
           (a + 60) % 521 == 0 and \
           (a + 66) % 37 == 0 and \
           (a + 79) % 19 == 0


# Eval function for test input
def eval_test(x):
    return x % 7 == 0 and \
           (x + 1) % 13 == 0 and \
           (x + 4) % 59 == 0 and \
           (x + 6) % 31 == 0 and \
           (x + 7) % 19 == 0


# Eval function for test input (rewritten to isolate x)
def eval_test_rewritten(x):
    return x % 7 == 0 and \
           x % 13 == (13 - 1) and \
           x % 59 == (59 - 4) and \
           x % 31 == (31 - 6) and \
           x % 19 == (19 - 7)


# https://rosettacode.org/wiki/Chinese_remainder_theorem
def chinese_remainder(n, a):
    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1: return 1
        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0: x1 += b0
        return x1

    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def bruteforce(xs, eval_fn):
    ts = 0
    while True:
        if eval_fn(ts):
            return ts
        ts += xs[0][1]


def iterative_lcm(times):
    earliest_time = int(times[0])
    increment = earliest_time
    for i in range(1, len(times)):
        if times[i] == 'x':
            continue
        cur_time = int(times[i])
        # while earliest_time % cur_time != (cur_time - i):
        while (earliest_time + i) % cur_time != 0:
            earliest_time += increment
        increment = math.lcm(increment, cur_time)
    return earliest_time


lines = open('input.test').read().splitlines()
bus_times = lines[1].split(',')
xs = [(i, int(x)) for i, x in enumerate(bus_times) if x != 'x']
print(xs)

primes = [x[1] for x in xs]
remainders = [x[1] - x[0] for x in xs]
print(bruteforce(xs, eval_test))
print(bruteforce(xs, eval_test_rewritten))
# print(bruteforce(xs, eval_real)) # Will just heat up the CPU for real input, bruteforce is futile
print(chinese_remainder(primes, remainders))
print(iterative_lcm(bus_times))
