# coding: utf-8
import doctest
import math
from itertools import takewhile
from collections import Counter
import re
from util import *


xs = sorted([int(x) for x in open('input.txt').read().splitlines()])
device = max(xs) + 3
xs = [0] + xs + [device]


@Memoize
def chains(target, curr = 0):
    if curr == target:
        return 1
    avail = list(filter(lambda x: 0 < x - curr <= 3, xs))
    if len(avail) == 0:
        return 0
    return sum([chains(target, x) for x in avail])


print(chains(device))

