def data():
    yield 'A'
    yield 'B'
    yield 'C'


g = data()
print(type(g))
print(g.__next__())
print(g.__next__())
print(g.__next__())


def generate(num):
    while num > 0:
        yield num**num
        num -= 1


g1 = generate(5)

print(type(g1))

l1 = list(g1)
print(l1)

g1 = generate(5)
for x in g1:
    print(x)