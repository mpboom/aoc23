import re
import functools
import operator
import collections


with open('input.txt') as fp:
    data = fp.read().splitlines()


impossible_games = set()
powers = []
for i, game in enumerate(data):
    sets = []
    minimums = collections.defaultdict(list)
    for single_set in game.split(';'):
        for (color, maximum) in (('red', 12), ('green', 13), ('blue', 14)):
            match = re.search(f'(\d+) {color}', single_set)
            if not match:
                continue
            match = match[1]
            if int(match) > maximum:
                impossible_games.add(i + 1)
            minimums[color].append(int(match))
    powers.append(functools.reduce(operator.mul, map(max, minimums.values()), 1))


# Part I
print(sum(set(range(1, len(data) + 1)) - impossible_games))

# Part II
print(sum(powers))
