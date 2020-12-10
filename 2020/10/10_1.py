# coding: utf-8
from collections import Counter

xs = [0] + sorted([int(x) for x in open('input.txt').read().splitlines()])

res = Counter()
for i in range(len(xs) - 1):
    a = xs[i]
    b = xs[i + 1]
    res[b - a] += 1
print(res)

print(res[1] * (res[3] + 1))