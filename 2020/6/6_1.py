# coding: utf-8
import doctest
import math
import itertools
from collections import Counter
import re

sum = 0
for group in open('input.txt').read().split('\n\n'):
    s = set(list(group.replace('\n', '')))
    sum += len(s)
print(sum)

# if __name__ == "__main__":
#     doctest.testmod()