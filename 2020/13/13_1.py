# coding: utf-8
import doctest
import math
import itertools
from collections import Counter
import re

lines = open('input.txt').read().splitlines()

start = ts = int(lines[0])
xs = [int(x) for x in lines[1].split(',') if x != 'x']
print(ts, xs)

while True:
    for x in xs:
        if ts % x == 0:
            print(ts - start, x, (ts - start) * x)
            exit()
    ts += 1
