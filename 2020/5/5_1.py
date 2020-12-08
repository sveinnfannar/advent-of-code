# coding: utf-8
import re

res = 0
for line in open('input.txt').read().splitlines():
    x = int(re.sub('[BR]', '1', re.sub('[FL]', '0', line)), 2)
    if x > res:
        res = x

print(res)
