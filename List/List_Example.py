from functools import reduce
import math
l = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

print(len(l))


def remove(l1):
    for n in l1:
        if n ^ 1 != n + 1: l1.remove(n)
    return l1


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(id(l1), l1)
# l1 = remove(l1)
[l1.remove(n) for n in l1 if n ^ 1 != n+1]
print(id(l1), l1)


# l1 = list(filter(lambda x: x ^ 1 == x+1, l1))
# print(id(l1))
# print(l1)



def test(*args, **kwargs):
    print(args, kwargs)

test()


def remove(l1):
    a= [l1.remove(n) for n in l1 if n ^ 1 != n + 1]
    return l1
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(id(l1), l1)
x= lambda a: remove(a)
print(id(l1), x(l1))