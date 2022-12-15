"""
Python contains the following inbuilt data types
1. int
2. float
3.complex
4.bool
5.str
6.bytes
7.bytearray
8.range
9.list
10.tuple
11.set
12.frozenset
13.dict
14.None
"""

a = 10
print(a, type(a))

a = 3.1427
print(a, type(a))

af = float('%.2f'%a)
print(af, type(af))

af = '{:.2f}'.format(a)
print(af, type(af))

ch = chr(65)
print(ch)

i = ord(ch)
print(i)

print(float(bool(False)))

str_data = 'python'
print(str_data)

str1 = str_data[::-1]
print(str1)

str1 = str_data[::-1][::-1]

print(id(str1), id(str_data))

x = [1, 2, 8, 4, 5, 6, 7, 8, 9]
b = bytes(x)
print(type(b))
print(b[6])

b = bytearray(x)
b.append(5)
for item in b:
    print(item, end=' ')
print(type(b))

print(bool(1))

print(round(3.425366, 2))
print('%.2f'%3.425366)
print('{0:.2f}'.format(13.425366,2.12525))
print(f'{3.43532:.2f}')
print(str(3.43532)[0:4])

x = [2, 4, 6, 8]
b = bytes(x)
print(type(b))

l = list(b)
print(type(l))
print(l)

i = 10
j = 185634786547654775685476
k = 5.367578439
s1 = 'fs'
s2 = 'fcdcghfkjkjdsjfgjgheckvhjvdciljhvbhouhvnkjhf'

print(i.__sizeof__())
print(j.__sizeof__())
print(s1.__sizeof__())
print(s2.__sizeof__())
print(k.__sizeof__())

print(ord('+'))






