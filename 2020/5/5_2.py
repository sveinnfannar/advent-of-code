# coding: utf-8
import re

ids = set()
for line in open('input.txt').read().splitlines():
    x = int(re.sub('[BR]', '1', re.sub('[FL]', '0', line)), 2)
    ids.add(x)

for x in range(127*8*7):
    if x not in ids and x - 1 in ids and x + 1 in ids:
        print(x)
