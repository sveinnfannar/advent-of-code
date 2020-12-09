# coding: utf-8

xs = [int(x) for x in open('input.txt').read().splitlines()]

for i in range(len(xs)):
    for j in range(i, len(xs)):
        s = sum(xs[i:j])
        if s == 29221323:
            print(min(xs[i:j]) + max(xs[i:j]))
            exit()
        elif s > 29221323:
            break

