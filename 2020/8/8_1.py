# coding: utf-8
import doctest
import math
import itertools
from collections import Counter
import re

p = []
for line in open('input.txt').readlines():
    inst, num = line.split()
    num = int(num)
    p.append((inst, num))


acc = 0
pc = 0
seen = set()
while True:
    if pc in seen:
        print(acc)
        break
    seen.add(pc)
    inst, num = p[pc]
    print(inst, num)
    if inst == 'nop':
        pc += 1
        continue
    elif inst == 'acc':
        acc += num
        pc += 1
    elif inst == 'jmp':
        pc += num


# if __name__ == "__main__":
#     doctest.testmod()