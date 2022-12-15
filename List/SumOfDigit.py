l1 = [12, 65, 23, 86, 10]
l2 = []
for item in l1:
    s = 0
    for n in str(item):
        s += int(n)
    l2.append(s)
print(l2)

