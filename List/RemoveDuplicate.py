l1 = [35, 6, 2, 43, 10, 11, 10, 43, 1]
l2 = []
l3 = []

print(l1)

for item in l1:
    if item not in l2:
        l2.append(item)
print(l2)

for item in l1:
    if not l3.__contains__(item):
        l3.append(item)
print(l3)

s1 = set(l1)
print(list(s1))