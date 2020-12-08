# coding: utf-8
import doctest
import math
import itertools
from collections import Counter
import re

count = 0
for p in open('input.txt').read().split('\n\n'):
    fs = [p.split(':')[0] for p in p.replace('\n', ' ').split(' ')]
    if len(fs) == 8 or (len(fs) == 7 and 'cid' not in fs):
        print(fs, 'valid')
        count += 1
print(count)

# for line in open('input.test').readlines():
#     print(re.search("(\d+)-(\d+) (\w): (\w+)", line).groups())

# if __name__ == "__main__":
#     doctest.testmod()