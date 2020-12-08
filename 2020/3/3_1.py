# coding: utf-8
import doctest
import math
import itertools
from collections import Counter
import re

import doctest
import math

c = 0

for y, line in enumerate(open('input.txt').read().splitlines()):
    x = y * 3
    if line[(x % len(line))] == '#':
        c += 1

print(c)


# if __name__ == "__main__":
#     doctest.testmod()