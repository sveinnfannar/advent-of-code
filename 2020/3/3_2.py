
def count_trees(slope_x, slope_y):
    c = 0
    x = 0
    lines = open('input.txt').read().splitlines()
    for y in range(0, len(lines), slope_y):
        line = lines[y]
        if line[(x % len(line))] == '#':
            c += 1
        x += slope_x
    return c


print(count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2))
