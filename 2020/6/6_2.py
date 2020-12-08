# coding: utf-8
import doctest
import math
import itertools
from collections import Counter
import re

sum = 0
for group in open('input.txt').read().split('\n\n'):
    anss = group.strip().split('\n')
    s = set(list(anss[0]))
    for a in anss[1:]:
        s = s.intersection(set(list(a)))
    # print(s)
    sum += len(s)
print(sum)

# if __name__ == "__main__":
#     doctest.testmod()