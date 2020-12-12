xs = sorted(int(x) for x in open('input.txt').read().splitlines())
xs = [0] + xs + [max(xs) + 3]
m = {0: 1}
for x in xs[1:]:
    m[x] = sum(m[y] for y in xs if x - 4 < y < x)
print(max(m.values()))
