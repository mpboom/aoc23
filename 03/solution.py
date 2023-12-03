import itertools
from collections import defaultdict


with open('input.txt') as fp:
    data = fp.read().splitlines()


data = list(map(list, data))
total = 0
total_gears = defaultdict(list)
for y, row in enumerate(data):
    current_number = ''
    for x, char in enumerate(row + ['.']):
        if not char.isdigit():
            if current_number:
                valid = False
                gears = set()
                points = [(q, y) for q in range(x - 1, x - len(current_number) - 1, -1)]
                for (x_p, y_p) in points:
                    for (x_t, y_t) in itertools.product([0, 1, -1], [0, 1, -1]):
                        x_x = x_t + x_p
                        y_y = y_t + y_p
                        if not (0 <= x_x < len(data[0]) and 0 <= y_y < len(data)):
                            continue
                        c = data[y_y][x_x]
                        if not (c.isdigit() or c == '.'):
                            valid = True
                        if c == '*':
                            gears.add((x_x, y_y))
                total += int(current_number) if valid else 0
                for gear in gears:
                    total_gears[gear].append(int(current_number))
                current_number = ''
        else:
            current_number += char


# Part I
print(total)

# Part II
print(sum(map(lambda g: g[0] * g[1] if len(g) == 2 else 0, total_gears.values())))
