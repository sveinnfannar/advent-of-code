# coding: utf-8
import doctest
import math
import itertools
from collections import Counter
import re

vcount = 0
for line in open('input.txt').readlines():
    first, pw = line.split(":")
    pw = pw.strip()
    range, letter = first.split(" ")
    letter = letter.strip()
    min, max = range.split('-')
    min = int(min)
    max = int(max)

    c = len([x for x in pw if x == letter])
    valid = min <= c <= max
    if valid:
        vcount += 1
print(vcount)
