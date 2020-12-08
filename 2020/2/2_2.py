# coding: utf-8
import doctest
import math
import itertools
from collections import Counter
import re

vcount = 0
for line in open('input.txt').readlines():
    min, max, letter, pw = re.search("(\d+)-(\d+) (\w): (\w+)", line).groups()
    first, pw = line.split(":")
    pw = pw.strip()
    range, letter = first.split(" ")
    letter = letter.strip()
    min, max = range.split('-')
    min = int(min)
    max = int(max)

    c = len([x for x in pw if x == letter])
    a, b = (pw[min - 1] == letter), (pw[max - 1] == letter)
    valid = a ^ b
    print(min, max, letter, pw, c, valid)
    if valid:
        vcount += 1

print(vcount)


# if __name__ == "__main__":
#     doctest.testmod()