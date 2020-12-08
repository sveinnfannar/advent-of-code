# coding: utf-8
import doctest
import math
import itertools
from collections import Counter
import re

xs = [int(x) for x in open('input.test').read().splitlines()]

for line in open('input.test').read().splitlines():
    print(re.search("(\d+)-(\d+) (\w): (\w+)", line).groups())
