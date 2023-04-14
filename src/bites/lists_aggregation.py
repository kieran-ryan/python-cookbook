keys = ["a", "b", "c"]
vals = [1, 2, 3]
zipped = dict(zip(keys, vals))

print(zipped)
# {'a': 1, 'b': 2, 'c': 3}

print(*zip(keys, vals))
# ('a', 1) ('b', 2) ('c', 3)
