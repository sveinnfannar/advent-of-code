# coding: utf-8

print(sum(len(set.intersection(*map(set, g.split()))) for g in open('input.txt').read().split('\n\n')))
