# coding: utf-8
import doctest
import math
import itertools
from collections import Counter
import re


def run(p):
    acc = 0
    pc = 0
    seen = set()
    while pc < len(p):
        inst, num = p[pc]
        seen.add(pc)
        # print(inst, num)
        if inst == 'nop':
            pc += 1
            continue
        elif inst == 'acc':
            acc += num
            pc += 1
        elif inst == 'jmp':
            pc += num

        if pc in seen:
            return False
    print(acc)
    return True


p = []
for line in open('input.txt').readlines():
    inst, num = line.split()
    num = int(num)
    p.append((inst, num))


for i in range(len(p)):
    inst, num = original = p[i]
    if inst == 'jmp':
        p[i] = ('nop', num)
    elif inst == 'nop':
        p[i] = ('jmp', num)

    if run(p):
        break
    p[i] = original


# if __name__ == "__main__":
#     doctest.testmod()