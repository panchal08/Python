class Tuple:

    t = (1, 2, 3, 4, 5)
    print(t)
    print(type(t))
    print(t.count(2))
    print(len(t))

    t1 = 1, 2, 3, 6, 2, 1, 0, 5
    print(type(t1))
    print(sorted(t1,reverse=True))
    print(min(t1))
    print(max(t1))


    s = set('Python')
    v = {'a', 'i', 'o', 'e', 'u'}
    d = s.intersection(v)
    print(d)
