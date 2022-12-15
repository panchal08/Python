l1 = [1, 2, 3, 4, 'hello', 3.2, 'python']

print(l1)

for item in l1:
    print(item, end=' ')

l1.append(564)
print(l1)

print(len(l1))

l1.insert(4, 6)
print(l1)

l1.reverse()
print(l1)

data = 'python is a programming language'

print(' '.join(data.split()[::-1]))


print('start')
list_data = [2, 5, 1, 4, 8, 3]
print(list_data)
list_data.sort()
print(list_data)
# list_data.clear()
print(sum(list_data))

l3 = ['Apple', 'Dell', 'realme', 'hp', 'acer', 'ASUS', 'lenovo']
for index, item in enumerate(l3, start=1):
    print(index, item)

l1 = ['Apple', 'Dell', 'realme', 'hp', 'acer', 'ASUS', 'lenovo']
l2 = [item.replace('e', '-').replace('A', 'e').replace('-', 'A') for item in l1]

print(l2)
print(l1.index('Dell'))
# l1.append(l2)
l1.extend(l2)
print(l1)
print(id(l1))
l3 = l1.copy()
print(id(l3))

# f = 3.1478954564552
# print('%.2f'%f)
#
# print('{:.2f}'.format(f))
#
# print(f'{f:.2f}')
#
# print(round(f,2))



publicIp = ["9.255.255.255","126.255.255.255","169.253.255.255","172.15.255.255","191.0.1.255","192.88.98.255","192.167.255.255","198.17.255.255","223.255.255.255",]
print("126.255.255.255" in publicIp)
for ip in publicIp:
     print(ip)