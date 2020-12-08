# coding: utf-8
import doctest
import math
import itertools
from collections import defaultdict
import re

# shiny gold

# pale chartreuse bags contain 5 dim violet bags, 4 muted aqua bags.

bags = defaultdict(list)
for line in open('input.test').readlines():
    bgs = re.findall("(\d+ )?(\w+ \w+) bag", line)
    # print([(int(n), c) for (n, c) in bgs[1:] if c != 'no other'])

    bc = bgs[0][1]
    for (n, c) in bgs[1:]:
        if c != 'no other':
            bags[bc].append((c, n))


def count_bags(bag):
    return 1 + sum(int(n) * count_bags(c) for c, n in bags[bag])

print(count_bags('shiny gold') - 1)

# if __name__ == "__main__":
#     doctest.testmod()