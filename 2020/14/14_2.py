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
mask = 0


def replace(addr, mask, perm):
    for i, c in enumerate(mask):
        if c == 'X':
            ii = 35 - i
            if perm[0] == '1':
                addr |= (1 << ii)
            else:
                addr &= (m36 ^ (1 << ii))
            perm = perm[1:]
    return addr

for line in open('input.txt').read().splitlines():
    parts = line.split(' = ')
    if parts[0] == 'mask':
        mask = parts[1]
        print(mask)
    else:
        addr = ints(parts[0])[0]
        addr |= int(mask.replace('X', '0'), 2) & m36
        addrs = set()

        xc = len(re.sub('[01]', '', mask))
        perms = [bin(x | 1<<xc)[-xc:] for x in range(2**xc)]
        for perm in perms:
            addrs.add(replace(addr, mask, perm))

        num = int(parts[1])
        for a in sorted(addrs):
            mem[a] = num
            print(f'mem[{a}] = mem[{bin(a)}] = {num}')
print(sum(mem.values()))
