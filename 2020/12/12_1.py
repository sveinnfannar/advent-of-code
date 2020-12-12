# coding: utf-8
import math

x, y = 0, 0
dir = 0
for line in open('input.txt').read().splitlines():
    d, n = line[0], int(line[1:])
    if d == 'N':
        y += n
    if d == 'S':
        y -= n
    if d == 'E':
        x += n
    if d == 'W':
        x -= n
    if d == 'L':
        dir -= n
    if d == 'R':
        dir += n
    if d == 'F':
        x += int(math.cos(math.radians(dir)) * n)
        y += int(-math.sin(math.radians(dir)) * n)

print(abs(x) + abs(y))

