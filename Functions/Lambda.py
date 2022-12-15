l = [0, 2, 5, 10, 15, 20, 25, 30]
l1 = list(filter(lambda x: x ^ 1 == x + 1, l))
print(l1)