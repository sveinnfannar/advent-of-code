# coding: utf-8
from itertools import combinations

xs = [int(x) for x in open('input.txt').read().splitlines()]
print(next(xs[i] for i in range(25, len(xs) - 25) if
           not any(a + b == xs[i] for a, b in combinations(xs[i - 25:i], 2))))
