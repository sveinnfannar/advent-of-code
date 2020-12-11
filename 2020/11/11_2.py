# coding: utf-8
import doctest
import math
import itertools
from collections import defaultdict
import re
import copy

adjacent = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def is_set(seats, y, x, offset):
    ox, oy = offset
    ny = y + oy
    nx = x + ox
    if 0 <= ny < len(seats) and 0 <= nx < len(seats[0]):
        v = seats[ny][nx]
        if v == '.':
            return is_set(seats, ny, nx, offset)
        return v == '#'
    else:
        return False


def step(seats):
    new = copy.deepcopy(seats)
    for y in range(len(seats)):
        for x in range(len(seats[0])):
            taken = 0
            for offset in adjacent:
                if is_set(seats, y, x, offset):
                    taken += 1

            curr = seats[y][x]
            if curr == 'L' and taken == 0:
                new[y][x] = '#'
            elif curr == '#' and taken >= 5:
                new[y][x] = 'L'

    return new


def count_taken(seats):
    count = 0
    for y in range(len(seats)):
        for x in range(len(seats[0])):
            if seats[y][x] == '#':
                count += 1
    return count


def draw(seats):
    for line in seats:
        print(''.join(line))
    print()


seats = []
for y, line in enumerate(open('input.txt').read().splitlines()):
    seats.append(list(line))

draw(seats)
prev_taken = -1
while True:
    seats = step(seats)
    taken = count_taken(seats)
    # draw(seats)
    print(taken)
    if taken == prev_taken:
        break
    prev_taken = taken
