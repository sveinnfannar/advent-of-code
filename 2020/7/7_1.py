# coding: utf-8
import doctest
import math
import itertools
from collections import defaultdict
import re

# shiny gold

# (\w+ \w+) bags contain (\d+) (\w+ \w+) bag(s, (\d+) (\w+ \w+) bags)*
# pale chartreuse bags contain 5 dim violet bags, 4 muted aqua bags.

bags = defaultdict(list)

for line in open('input.txt').readlines():
    # print(line)
    cols = [c for (_, c) in re.findall("(\d+ )?(\w+ \w+) bag", line)]

    for c in cols[1:]:
        bags[c].append(cols[0])

print(bags)

seen = set()
def find(c):
    global seen
    print(c)
    for nc in bags[c]:
        seen.add(nc)
        find(nc)

find('shiny gold')
print(len(seen))

# if __name__ == "__main__":
#     doctest.testmod()