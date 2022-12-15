class SwapElement:

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
