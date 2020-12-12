# coding: utf-8
import doctest
import math


def rot(wp, deg):
    """
    >>> rot((1, 0), 90)
    (0, 1)
    >>> rot((100, 0), 90)
    (0, 100)
    >>> rot((1, 1), 90)
    (-1, 1)
    >>> rot((10, 4), -90)
    (4, -10)
    """
    wx, wy = wp
    dist = math.sqrt(wy**2 + wx**2)
    angle = math.atan2(wy, wx)
    new_angle = angle + math.radians(deg)
    wx = round(math.cos(new_angle) * dist)
    wy = round(math.sin(new_angle) * dist)
    return wx, wy


x, y = 0, 0
wx, wy = 10, 1
for line in open('input.txt').read().splitlines():
    d, n = line[0], int(line[1:])
    if d == 'N':
        wy += n
    if d == 'S':
        wy -= n
    if d == 'E':
        wx += n
    if d == 'W':
        wx -= n
    if d == 'L':
        wx, wy = rot((wx, wy), n)
    if d == 'R':
        wx, wy = rot((wx, wy), -n)
    if d == 'F':
        x += wx * n
        y += wy * n

print(abs(x) + abs(y))


if __name__ == "__main__":
    doctest.testmod()