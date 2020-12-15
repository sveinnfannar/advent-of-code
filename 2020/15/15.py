# coding: utf-8
import doctest
import math
import itertools
from collections import Counter
import re


def run(input, iterations):
    xs = {int(x): i for i, x in enumerate(input[:-1])}
    last = input[-1]
    for i in range(len(xs), iterations - 1):
        if last in xs:
            x = i - xs[last]
            xs[last] = i
            last = x
        else:
            xs[last] = i
            last = 0
    return last


test = [0, 3, 6]
input = [7, 12, 1, 0, 16, 2]
print(run(test, 2020))
print(run(input, 2020))
print(run(input, 30000000)) # ~5 sec
