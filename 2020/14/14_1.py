# coding: utf-8
import doctest
import math
import itertools
from collections import Counter
import re

def ints(s):
    return list(map(int, re.findall(r"-?\d+", s)))

mem = {}
m36 = (1 << 36) - 1
mask_1 = 0
mask_0 = 0
for line in open('input.txt').read().splitlines():
    parts = line.split(' = ')
    if parts[0] == 'mask':
        mask_0 = int(parts[1].replace('X', '1'), 2) & m36
        mask_1 = int(parts[1].replace('X', '0'), 2) & m36
        print(bin(mask_0), bin(mask_1))
    else:
        addr = ints(parts[0])[0]
        num = int(parts[1])
        mem[addr] = num & mask_0 | mask_1
        print(addr, mem[addr])
print(sum(mem.values()))
