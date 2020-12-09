# coding: utf-8
from itertools import combinations

N = 25
xs = [int(x) for x in open('input.txt').read().splitlines()]

def find_comb(x, lookback):
    for a, b in combinations(lookback, 2):
        if a + b == x:
            return True
    return False

for i in range(N, len(xs) - N):
    x = xs[i]
    lookback = xs[i - N:i]
    if (not find_comb(x, lookback)):
        print(x)
        exit()
