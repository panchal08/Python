import functools
l = [0, 2, 5, 10, 15, 20, 25, 30]
l3 = functools.reduce(lambda x, y: x + y, l)
print(l3)
