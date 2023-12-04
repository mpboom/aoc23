import itertools as it


with open('input.txt') as fp:
    data = [
        len(set(l.split(': ')[-1].split(' |')[0].split(' ')) & set(l.split('|')[-1].split(' ')))
        for l in fp.read().replace('  ', ' ').splitlines()
    ]

cards = [1 for _ in range(len(data))]
for ((i, copies), j) in it.chain(*(
    zip(it.repeat((i, copies), copies), it.count()) for i, copies in enumerate(data)
)):
    cards[i + j + 1] += cards[i]


# Part I
print(sum(int(2 ** (x - 1)) for x in data))

# Part II
print(sum(cards))
