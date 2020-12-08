# coding: utf-8
import math

xs = [int(x) for x in open('input.txt').readlines()]


def find():
    for i, x in enumerate(xs):
        for j, y in enumerate(xs):
            for k, z in enumerate(xs):
                if i != j and j != k:
                    if x+y+z == 2020:
                        print(x*y*z)
                        return
find()
